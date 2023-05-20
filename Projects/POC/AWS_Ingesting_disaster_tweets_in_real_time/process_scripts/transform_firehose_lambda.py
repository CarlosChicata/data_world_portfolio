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
        classify a bulk tweets to classify kind of disaster.
        Average: 1min. It's expensive.
    '''
    output = []

    # STEP #1: preparing data to classifier
    for record in event['records']:
        record_dict = json.loads(base64.b64decode(record['data']).decode('latin9'))
        cleaning_tweet = cleaning_sentence(record_dict["text"])

        # STEP #2: classife tweet
        t1 = datetime.now()
        classifier_rpta = comprehend.classify_document(
            Text=cleaning_tweet,
            EndpointArn=ENDPOINT_CLASSIFIER
        )
        t2 = datetime.now()
        delta = t2 - t1
        row_data = {
            "original_text": record_dict["text"],
            "cleaning_text": cleaning_tweet,
            "disaster_label": classifier_rpta["Classes"][0]["Name"],
            "classifier_score": classifier_rpta["Classes"][0]["Score"],
            "arrived_datetime_from_kinesis": record["approximateArrivalTimestamp"],
            "processing_time": delta.total_seconds()
        }
        # STEP #3: add in response kinesis
        output.append({
            'recordId': record["recordId"],
            'result': 'Ok',
            "data": base64.b64encode(str(row_data).encode('utf-8')).decode('utf-8')
        })
        
    print(output)

    return {'records': output}

