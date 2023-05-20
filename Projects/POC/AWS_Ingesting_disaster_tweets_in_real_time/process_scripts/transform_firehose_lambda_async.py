'''
    Format all tweets sent from kinesis firehose in lambda to consume in redshift.
'''
import base64
import re
import json
import time
import tarfile
import io
from functools import reduce
from datetime import datetime


from boto3 import Session

ENDPOINT_CLASSIFIER = ""
IAM_ROLE=""
CLASSIFIER= ""
BUCKET = "script-poc-case-1"
ACCESS_KEY = ""
SECRET_KEY = ""

session = Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="us-east-1"
)

s3 = session.client('s3')
comprehend = session.client("comprehend")

### UTILITY FUNCTION

##### Cleaning processing

def remove_urls(x):
  ''' Remove URLs from sentence'''
  word_list = x.split(" ")
  word_list = [ 
      word.lower() for word in word_list \
      if re.search("^http(s)*:\/\/", word) is None
    ]
  return " ".join(word_list)


def remove_arrobas(x):
  ''' Remove arrobas from sentence'''
  word_list = x.split(" ")
  clean_words = []
  for word in word_list:
    if re.search("^@", word) is None:
      clean_words.append(word.lower())
    else:
      clean_words.append("<user>")
  return " ".join(clean_words)


def remove_with_non_hashtag_value(x):
  ''' Remove hashtag value'''
  word_list = x.split(" ")
  clean_words = []
  for word in word_list:
    if re.search("^#", word) is None:
      clean_words.append(word.lower())

  return " ".join(clean_words)


def remove_puntuactions(x):
  return re.sub(r"[,.;@#?!&$-:'_]+\ *", " ", x)


def preserve_alphanumeric_characters(x):
  return re.sub(r'[^A-Za-z0-9 ]+', '', x)


def abs_transform_sentence(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)


cleaning_sentence = abs_transform_sentence(
        remove_arrobas, 
        remove_urls, 
        remove_with_non_hashtag_value,
        remove_puntuactions,
        preserve_alphanumeric_characters
    )


##### Handle classifier file: unzip file

def extract_targz(targz_file, filename):
    tar = tarfile.open(fileobj=targz_file)
    content_file = None
    rpta = []

    for member in tar.getmembers():
        if member.name == filename:
            f = tar.extractfile(member)
            content_file = f
            break

    for line in content_file.readlines():
        rpta.append(json.loads(line))
    return rpta


### MAIN FUNCTION
def lambda_handler(event, context):
    '''
        Create a bulk tweets to classify kind of disaster  in async mode.
        Average time: 6min by classifier. It's cheap.
    '''
    output = []
    sentences = []

    # STEP #1: preparing data to classifier
    for record in event['records']:
        record_dict = json.loads(base64.b64decode(record['data']).decode('latin9'))
        cleaning_tweet = cleaning_sentence(record_dict["text"])
        output.append((cleaning_tweet, record_dict["text"], record['recordId']))
        sentences.append(cleaning_tweet)

    sentences = "\n".join(sentences)

    key_file = "datalake/origin/" + datetime.now().strftime("%d-%m-%YT%H:%M:%S") + \
        "_bulk_tweets.txt"
    key_classifier_file = "datalake/classifier/" + \
        datetime.now().strftime("%d-%m-%YT%H:%M:%S") + "_bulk_tweets.txt"
    
    s3.put_object(
        Body=bytes(sentences, "latin9"), 
        Bucket=BUCKET, 
        Key=key_file
    )
    s3_uri_object = "s3://" + BUCKET + "/" + key_file
    s3_uri_classified_object = "s3://" + BUCKET + "/" + key_classifier_file
    
    # STEP #2: classify your data
    classifing_sentences_job = comprehend.start_document_classification_job(
        JobName="Classifier_data",
        DocumentClassifierArn=CLASSIFIER,
        InputDataConfig={
           "S3Uri": s3_uri_object,
           "InputFormat": "ONE_DOC_PER_LINE",
        },
        OutputDataConfig={
            "S3Uri": s3_uri_classified_object
        },
        DataAccessRoleArn=IAM_ROLE
    )
    job_id = classifing_sentences_job["JobId"]
    classifier_file = None
    iterTime = 400

    continue_classifing_work = True

    while continue_classifing_work == True or iterTime <= 0:
        status_classifier_job = comprehend.describe_document_classification_job(
            JobId=job_id
        )
        iterTime = iterTime - 1
        
        status = status_classifier_job["DocumentClassificationJobProperties"]["JobStatus"]

        if status == 'COMPLETED':
            print("completed job!")
            continue_classifing_work = False
            classifier_file = status_classifier_job["DocumentClassificationJobProperties"]["OutputDataConfig"]["S3Uri"]
            print(classifier_file)
        elif status == 'FAILED':
            continue_classifing_work = False
            print("Failed job :(")
            print(status_classifier_job["DocumentClassificationJobProperties"]["Message"])
        else:
            print("working in status: " + status)
        time.sleep(5)

    # STEP #3: read the file
    if classifier_file is not None:
        len_prefix_file = len(BUCKET) + 6
        key_file = classifier_file[len_prefix_file:]
        memory_file = io.BytesIO()
        s3.download_fileobj(BUCKET, key_file, memory_file) # on memory
        memory_file.seek(0)
        classifier_data = extract_targz(memory_file, 'predictions.jsonl') # on memory
        proccessed_rpta = []
        
        for classify_rpta, tweet in zip(classifier_data, output):
            process_rpta_sentence = {
                "tweet_text" : tweet[0],
                "label": classify_rpta["Classes"][0]["Name"],
                "classifier_score": classify_rpta["Classes"][0]["Score"],
                "bulk_name": classify_rpta["File"],
                "original_tweet_text": tweet[1],
                "classifier_rpta_location": classifier_file,
                "bulk_location": s3_uri_object
            }
            proccessed_rpta.append({
                'recordId': tweet[2],
                'result': 'Ok',
                "data": base64.b64encode(str(process_rpta_sentence).encode('utf-8')).decode('utf-8')
            })
        
        output = proccessed_rpta
    
    print(output)
            
    return {'records': output}
