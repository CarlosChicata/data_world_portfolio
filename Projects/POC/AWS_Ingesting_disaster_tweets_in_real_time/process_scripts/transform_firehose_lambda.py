'''
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


def lambda_handler_v2(event, context):
    output = []
    sentences = []

    # STEP #1: preparing data to classifier
    for record in event['records']:
        record_dict = json.loads(base64.b64decode(record['data']))
        cleaning_tweet = cleaning_sentence(record_dict["text"])
        output.append((cleaning_tweet, record_dict["text"], record['recordId']))
        sentences.append(cleaning_tweet)

    #sentences = "\n".join(sentences)

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

    for sentence in sentences:
        t1 = datetime.now()
        rpta_sentence = comprehend.classify_document(
            Text=sentence,
            EndpointArn=ENDPOINT_CLASSIFIER
        )
        t2 = datetime.now()
        print(rpta_sentence)
        delta = t2 - t1
        print(f"Time difference is {delta.total_seconds()} seconds")





input_data_test = {
    'records': [
        {'recordId': '49640491891290384533425070480178768347599342808133009458000000', 'approximateArrivalTimestamp': 1683343228611, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE1NCwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA1LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOC8yOS8xNSAxNDo0NiIsICJjaG9vc2Vfb25lIjogIlJlbGV2YW50IiwgImNob29zZV9vbmU6Y29uZmlkZW5jZSI6IDEuMCwgImNob29zZV9vbmVfZ29sZCI6IG51bGwsICJrZXl3b3JkIjogImFubmloaWxhdGVkIiwgImxvY2F0aW9uIjogbnVsbCwgInRleHQiOiAiQ29wIHB1bGxzIGRydW5rIGRyaXZlciB0byBzYWZldHkgU0VDT05EUyBiZWZvcmUgaGlzIGNhciBpcyBoaXQgYnkgdHJhaW4uIGh0dHA6Ly90LmNvL0YxQkFrcE55bjZcdTAwZTVcdTAwY2EgaHR0cDovL3QuY28vbFpYd29BeUU0eCB2aWEgQFZpcmFsU3BlbGwiLCAidHdlZXRpZCI6IDYuMjkwMDVlKzE3LCAidXNlcmlkIjogMjQ1MDAyNDIxLjB9', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480178768347599342808133009458', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343228611}}, 
        {'recordId': '49640491891290384533425070480179977273418957437307715634000000', 'approximateArrivalTimestamp': 1683343228613, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE1NSwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA1LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOS8xLzE1IDM6NTciLCAiY2hvb3NlX29uZSI6ICJOb3QgUmVsZXZhbnQiLCAiY2hvb3NlX29uZTpjb25maWRlbmNlIjogMC41OTg3LCAiY2hvb3NlX29uZV9nb2xkIjogbnVsbCwgImtleXdvcmQiOiAiYW5uaWhpbGF0ZWQiLCAibG9jYXRpb24iOiBudWxsLCAidGV4dCI6ICJCUk9PTyBIRSBKVVNUIEdPVCBBTk5JSElMQVRFRCBodHRwczovL3QuY28vVVI3UWtxRzF3ZiIsICJ0d2VldGlkIjogNi4yOTA1NGUrMTcsICJ1c2VyaWQiOiAxMTQxMzE2NTQ1LjB9', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480179977273418957437307715634', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343228613}}, 
        {'recordId': '49640491891290384533425070480181186199238572066482421810000000', 'approximateArrivalTimestamp': 1683343228613, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE1NiwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA1LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOC8yOC8xNSAyMDoxMCIsICJjaG9vc2Vfb25lIjogIlJlbGV2YW50IiwgImNob29zZV9vbmU6Y29uZmlkZW5jZSI6IDEuMCwgImNob29zZV9vbmVfZ29sZCI6IG51bGwsICJrZXl3b3JkIjogImFubmloaWxhdGVkIiwgImxvY2F0aW9uIjogIlN3YW5pbmcgQXJvdW5kIiwgInRleHQiOiAiQU5OSUhJTEFURUQgSU4gREFNQVNDVVM6IFNZUklBTiBBUk1ZIEdSSU5EUyBcdTAwODlcdTAwZGJcdTAwZjdBTExPT1NIIEFORCBISVMgR0FORyBJTlRPIFRIRSBNQU5VUkUgUElMRVxuaHR0cDovL3QuY28vN3Jha2hQM2JXbSIsICJ0d2VldGlkIjogNi4yOTAyMWUrMTcsICJ1c2VyaWQiOiAxNjcyMzg2MTAzLjB9', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480181186199238572066482421810', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343228613}}, 
        {'recordId': '49640491891290384533425070480182395125058186695657127986000000', 'approximateArrivalTimestamp': 1683343228613, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE1NywgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA1LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOS8xLzE1IDE0OjExIiwgImNob29zZV9vbmUiOiAiTm90IFJlbGV2YW50IiwgImNob29zZV9vbmU6Y29uZmlkZW5jZSI6IDAuNzk1MiwgImNob29zZV9vbmVfZ29sZCI6IG51bGwsICJrZXl3b3JkIjogImFubmloaWxhdGVkIiwgImxvY2F0aW9uIjogbnVsbCwgInRleHQiOiAiQHRoYXRkZXMgb2sgaSB3YXNuJ3QgY29tcGxldGVseSBmb3J0aHJpZ2h0IGkgbWF5IGhhdmUgYWxzbyBiZWVuIGluIGEgZm9vZCBjb21hIGJjIG9mIHRoZSBrZWJhYi90YWhpbmkvcGlja2xlcyBpIGFsc28gYW5uaWhpbGF0ZWQgdy9mcmllcyIsICJ0d2VldGlkIjogNi4yOTAzNWUrMTcsICJ1c2VyaWQiOiAyMzIwODQ4NjQuMH0=', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480182395125058186695657127986', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343228613}}, 
        {'recordId': '49640491891290384533425070480183604050877801324831834162000000', 'approximateArrivalTimestamp': 1683343228613, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE1OCwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA1LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOS8xLzE1IDEzOjQ0IiwgImNob29zZV9vbmUiOiAiTm90IFJlbGV2YW50IiwgImNob29zZV9vbmU6Y29uZmlkZW5jZSI6IDEuMCwgImNob29zZV9vbmVfZ29sZCI6IG51bGwsICJrZXl3b3JkIjogImFubmloaWxhdGVkIiwgImxvY2F0aW9uIjogIlNhbGVtLCBNQSIsICJ0ZXh0IjogIkBBbGJlcnRCcmVlciBoZSB3YXMgcHJvYmFibHkgYW5uaWhpbGF0ZWQgbmVlZGVkIGhpcyBERCIsICJ0d2VldGlkIjogNi4yOTA4NmUrMTcsICJ1c2VyaWQiOiAxOTU1MDU3MzAuMH0=', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480183604050877801324831834162', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343228613}}, 
        {'recordId': '49640491891290384533425070480184812976697415954006540338000000', 'approximateArrivalTimestamp': 1683343228613, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE1OSwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA1LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOC8yOC8xNSAxMTo0NCIsICJjaG9vc2Vfb25lIjogIk5vdCBSZWxldmFudCIsICJjaG9vc2Vfb25lOmNvbmZpZGVuY2UiOiAwLjYwMTgsICJjaG9vc2Vfb25lX2dvbGQiOiBudWxsLCAia2V5d29yZCI6ICJhbm5paGlsYXRlZCIsICJsb2NhdGlvbiI6ICJDaGljYWdvLCBJbGxpbm9pcyIsICJ0ZXh0IjogIiRHTUNSIG5vIGxvbmdlIHJHcmVlbiBtb3VudGFpbiBub3cgUmVkIE1vdW50YWluLi4uc3RvY2sgYW5uaWhpbGF0ZWQgYWZ0ZXIgaG91cnMiLCAidHdlZXRpZCI6IDYuMjkwMjhlKzE3LCAidXNlcmlkIjogMTI5Njk1Mjc0MS4wfQ==', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480184812976697415954006540338', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343228613}}, 
        {'recordId': '49640491891290384533425070480186021902517030583181246514000000', 'approximateArrivalTimestamp': 1683343228613, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE2MCwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA3LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOC8yNy8xNSAxNjoxNSIsICJjaG9vc2Vfb25lIjogIk5vdCBSZWxldmFudCIsICJjaG9vc2Vfb25lOmNvbmZpZGVuY2UiOiAxLjAsICJjaG9vc2Vfb25lX2dvbGQiOiBudWxsLCAia2V5d29yZCI6ICJhbm5paGlsYXRlZCIsICJsb2NhdGlvbiI6ICJMb25kb24iLCAidGV4dCI6ICJBIGZ1biBmaWxsZWQgaGFwcHktaG91ciBhdCBTaW1tb25zIGJhciBpbiBDYW1kZW4gd2l0aCB0aGlzIGhhbmRzb21lIG9uZSA/PyAoSSBnb3QgYW5uaWhpbGF0ZWQgYXBhcnQgZnJvbSB0aGlzIGdhbWUpIGh0dHA6Ly90LmNvLzRKTm82Nzdaa3YiLCAidHdlZXRpZCI6IDYuMjkwM2UrMTcsICJ1c2VyaWQiOiAyNTkyOTcyMzMuMH0=', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480186021902517030583181246514', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343228613}}, 
        {'recordId': '49640491891290384533425070480187230828336645212355952690000000', 'approximateArrivalTimestamp': 1683343228613, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE2MSwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA1LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOC8zMS8xNSAyMDowOCIsICJjaG9vc2Vfb25lIjogIk5vdCBSZWxldmFudCIsICJjaG9vc2Vfb25lOmNvbmZpZGVuY2UiOiAxLjAsICJjaG9vc2Vfb25lX2dvbGQiOiBudWxsLCAia2V5d29yZCI6ICJhbm5paGlsYXRlZCIsICJsb2NhdGlvbiI6ICJBbGJhbnkvTlkiLCAidGV4dCI6ICJKdWFubnkgQmVpc2JvbCBTci4gQW5uaWhpbGF0ZWQgdGhhdCBiYWxsLiAjTEdNIiwgInR3ZWV0aWQiOiA2LjI5MDkxZSsxNywgInVzZXJpZCI6IDM0ODQyNTYzLjB9', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480187230828336645212355952690', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343228613}}, 
        {'recordId': '49640491891290384533425070480188439754156259841530658866000000', 'approximateArrivalTimestamp': 1683343228613, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE2MiwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA1LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOC8yOC8xNSA5OjQ2IiwgImNob29zZV9vbmUiOiAiUmVsZXZhbnQiLCAiY2hvb3NlX29uZTpjb25maWRlbmNlIjogMC41OTcsICJjaG9vc2Vfb25lX2dvbGQiOiBudWxsLCAia2V5d29yZCI6ICJhbm5paGlsYXRpb24iLCAibG9jYXRpb24iOiAiQ2FsaWZvcm5pYSwgVVNBIiwgInRleHQiOiAiQHJ2ZnJpZWRtYW5uIEhlbGwgaXMganVzdCBhIGZyYWN0aW9uIG9mIGhpcyBiZWxpZWYgb2YgdG90YWwgYW5uaWhpbGF0aW9uIGRlc3RydWN0aW9uIG9mIFVTQSBATG9kaVNpbHZlcmFkbyBAcml0enlfamV3ZWxzIiwgInR3ZWV0aWQiOiA2LjI5MTExZSsxNywgInVzZXJpZCI6IDIzNzk4NDgyMC4wfQ==', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480188439754156259841530658866', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343228613}}, 
        {'recordId': '49640491891290384533425070480189648679975874470705365042000000', 'approximateArrivalTimestamp': 1683343228613, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE2MywgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA2LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOC8yNy8xNSAxNjoxMSIsICJjaG9vc2Vfb25lIjogIk5vdCBSZWxldmFudCIsICJjaG9vc2Vfb25lOmNvbmZpZGVuY2UiOiAwLjUwNSwgImNob29zZV9vbmVfZ29sZCI6IG51bGwsICJrZXl3b3JkIjogImFubmloaWxhdGlvbiIsICJsb2NhdGlvbiI6IG51bGwsICJ0ZXh0IjogIkBQT1RVUyBNYXliZSB3ZSBzaG91bGQgY2FsbCBJc3JhZWwgYW5kIHRlbGwgdGhlbSB3ZSdyZSBzb3JyeSBhcmUgUHJlcyBoYXMgc29sZCB0aGVtIGRvd24gdGhlIHJpdmVyIHRvIGFubmloaWxhdGlvbi4iLCAidHdlZXRpZCI6IDYuMjkxMDZlKzE3LCAidXNlcmlkIjogMjE1NTkyOTI3OC4wfQ==', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480189648679975874470705365042', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343228613}}, 
        {'recordId': '49640491891290384533425070480190857605795490886586466354000000', 'approximateArrivalTimestamp': 1683343254176, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE2NCwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA2LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOC8yNy8xNSAxNToyMyIsICJjaG9vc2Vfb25lIjogIk5vdCBSZWxldmFudCIsICJjaG9vc2Vfb25lOmNvbmZpZGVuY2UiOiAwLjgzMTcsICJjaG9vc2Vfb25lX2dvbGQiOiBudWxsLCAia2V5d29yZCI6ICJhbm5paGlsYXRpb24iLCAibG9jYXRpb24iOiBudWxsLCAidGV4dCI6ICJFdmlsZGVhZCAtIEFubmloaWxhdGlvbiBvZiBDaXZpbGl6YXRpb24gaHR0cDovL3QuY28vc1Bma0U1S3F1NCIsICJ0d2VldGlkIjogNi4yOTExM2UrMTcsICJ1c2VyaWQiOiAzNzEzNTA3OTMuMH0=', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480190857605795490886586466354', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343254176}}, 
        {'recordId': '49640491891290384533425070480192066531615105515761172530000000', 'approximateArrivalTimestamp': 1683343254178, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE2NSwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA1LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOC8yNy8xNSAyMjowOCIsICJjaG9vc2Vfb25lIjogIk5vdCBSZWxldmFudCIsICJjaG9vc2Vfb25lOmNvbmZpZGVuY2UiOiAxLjAsICJjaG9vc2Vfb25lX2dvbGQiOiBudWxsLCAia2V5d29yZCI6ICJhbm5paGlsYXRpb24iLCAibG9jYXRpb24iOiBudWxsLCAidGV4dCI6ICJVLlMgTmF0aW9uYWwgUGFyayBTZXJ2aWNlcyBUb250byBOYXRpb25hbCBGb3Jlc3Q6IFN0b3AgdGhlIEFubmloaWxhdGlvbiBvZiB0aGUgU2FsdCBSaXZlciBXaWxkIEhvcnNlLi4uIGh0dHA6Ly90LmNvLzZMb0pPb1JPdWsgdmlhIEBDaGFuZ2UiLCAidHdlZXRpZCI6IDYuMjkxZSsxNywgInVzZXJpZCI6IDMwNzA4NDA5MzMuMH0=', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480192066531615105515761172530', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343254178}}, 
        {'recordId': '49640491891290384533425070480193275457434720144935878706000000', 'approximateArrivalTimestamp': 1683343254178, 
        'data': 'eyJfdW5pdF9pZCI6IDc3ODI0NTE2NiwgIl9nb2xkZW4iOiBmYWxzZSwgIl91bml0X3N0YXRlIjogImZpbmFsaXplZCIsICJfdHJ1c3RlZF9qdWRnbWVudHMiOiA1LCAiX2xhc3RfanVkZ21lbnRfYXQiOiAiOC8zMS8xNSAxNjo0MyIsICJjaG9vc2Vfb25lIjogIlJlbGV2YW50IiwgImNob29zZV9vbmU6Y29uZmlkZW5jZSI6IDAuNzk5NCwgImNob29zZV9vbmVfZ29sZCI6IG51bGwsICJrZXl3b3JkIjogImFubmloaWxhdGlvbiIsICJsb2NhdGlvbiI6IG51bGwsICJ0ZXh0IjogIlBsZWFzZSBzaWduICZhbXA7IFJUIHRvIHNhdmUgI1NhbHRSaXZlcldpbGRIb3JzZXMgaHR0cDovL3QuY28vR0I4aXNwaWFSUCBodHRwOi8vdC5jby9CeDBsODdpTmM4IiwgInR3ZWV0aWQiOiA2LjI5MTA2ZSsxNywgInVzZXJpZCI6IDEwOTM5NTgxOTguMH0=', 'kinesisRecordMetadata': {'sequenceNumber': '49640491891290384533425070480193275457434720144935878706', 'subsequenceNumber': 0, 'partitionKey': '1', 'shardId': 'shardId-000000000003', 'approximateArrivalTimestamp': 1683343254178}}
    ]
}


lambda_handler_v2(input_data_test, None)


'''
import base64

print('Loading function')


def lambda_handler(event, context):
    output = []

    for record in event['records']:
        print(record['recordId'])
        print(record['data'])
        payload = base64.b64decode(record['data']).decode('latin9') + "\n"

        # Do custom processing on the payload here

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(payload.encode('latin9')).decode('latin9')
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
'''
