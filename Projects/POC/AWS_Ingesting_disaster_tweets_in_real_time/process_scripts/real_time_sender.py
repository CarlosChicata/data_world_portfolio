'''
    Process to emulate the send of tweets in real time enviroment
'''
import time
import json
import random


import requests
import pandas as pd


# ok
def get_data_from_file(filename):
    '''
        Get a data in data frame format from file.
        
        Args
        filename (string): location of file
        
        return a data frame
    '''
    return pd.read_csv(filename, encoding="latin9")


# need to test
def http_request_send(url, data):
    '''
        Send a tweet to infra from http request
        
        Args
        url (string): url will receive the tweets.
        data (object) List of tweets will process.
        
        return none
    '''
    headers_req = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(url, data=json.dumps(data), headers=headers_req)


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
        selected_tweets = selected_tweets.to_dict(orient="records")
        print(selected_tweets)
        print(type(selected_tweets))
        print(second_sleepy)
        print(chunk_size)
        
        count_tweets += chunk_size
        http_request_send(url, selected_tweets)
        time.sleep(second_sleepy)
    

real_time_generator_emulator("./sample_data/database.csv", "FAKE URL SERVICE")