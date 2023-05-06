'''
    Process to emulate the send of tweets in real time enviroment.
    It sends tweets of list in JSON format to AWS kinesis data firehose directly
'''
import time
import json
import random


import requests
import pandas as pd
import numpy as np
from boto3 import Session


ACCESS_KEY = ""
SECRET_KEY = ""
session = Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="us-east-1"
)

firehose = session.client('firehose')


# ok
def get_data_from_file(filename):
    '''
        Get a data in data frame format from file.
        
        Args
        filename (string): location of file
        
        return a data frame
    '''
    return pd.read_csv(filename, encoding="latin9")


# ok
def real_time_generator_emulator(filename, url):
    '''
        generate a emulator to send collected tweets in real time
        
        Args
        filename (string): location of tweets database.
        url (string): location of service will receive the tweets.
        
        return none.
    '''
    database = get_data_from_file(filename)
    database_size = database.shape[0]
    
    count_tweets = 0
    
    while count_tweets < database_size:
        chunk_size = random.randint(1, 10)
        second_sleepy = random.randint(1, 30)
        
        selected_tweets = database.iloc[count_tweets : count_tweets + chunk_size]
        selected_tweets.replace(np.nan, None, inplace=True)
        selected_tweets = selected_tweets.to_dict(orient="records")
        

        count_tweets += chunk_size
        transformed_tweets = []

        for tweet in selected_tweets:
            transformed_tweets.append({"Data": json.dumps(tweet)})
    
        response = firehose.put_record_batch(
            DeliveryStreamName =url,
            Records=transformed_tweets
        )
        if(200 <= response['ResponseMetadata']["HTTPStatusCode"] < 300): print("Sent ok!")
        elif(response['ResponseMetadata']["HTTPStatusCode"] >= 400): print(transformed_tweets, "chunk don't received")
        else: print(transformed_tweets, "weird thing happened")
        print("sleeping for: ", second_sleepy)
        time.sleep(second_sleepy)
    

real_time_generator_emulator("../sample_data/database.csv", "PUT-S3-VL6p2")