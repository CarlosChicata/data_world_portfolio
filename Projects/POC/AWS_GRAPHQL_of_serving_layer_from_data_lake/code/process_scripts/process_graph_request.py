'''
Proceso para mapear la consulta de GraphQL a SQL para Athena
'''
import time
import io
import os


import pandas as pd
from boto3 import Session
#import boto3

'''
ACCESS_KEY = ""
SECRET_KEY = ""
session = Session()
athena_cli = session.client("athena", region_name="us-east-1")
s3_cli = session.client("s3")
#s3_cli = boto3.client('s3')
#athena_cli = boto3.client('athena')

ATHENA_S3_OUTPUT = os.environ["ATHENA_S3_OUTPUT"]
ATHENA_WORKGROUP = os.environ["ATHENA_WORKGROUP"]
ATHENA_S3_BUCKET_OUTPUT = os.environ["ATHENA_S3_BUCKET_OUTPUT"]
'''

# OK
def get_data_from_sql_engine(query):
    '''
        Execute a SQL sentences in AWS AThena and return data.
        
        Params
        query (string): sql query to extract data
        
        return a location of generated file: key of file and bucket
    '''
    try:
        # setting params to control de Athena
        STATE = "RUNNING"

        ## STEP 1 : go the SQL sentence to athena
        
        query_id = athena_cli.start_query_execution(
            QueryString = query,
            QueryExecutionContext = {
                "Database": "db-poc-case-1"
            },
            ResultConfiguration= {"OutputLocation": ATHENA_S3_OUTPUT}
        )

        ## STEP 2 : waiting the finish operation: asynchronic ops

        while STATE in ["RUNNING", "QUEUED"]:
            #MAX_EXECUTION -= 1
            response = athena_cli.get_query_execution(
                    QueryExecutionId=query_id["QueryExecutionId"]
                )

            if "QueryExecution" in response and \
                "Status" in response["QueryExecution"] and \
                "State" in response["QueryExecution"]["Status"]:

                STATE = response["QueryExecution"]["Status"]["State"]

                if STATE == 'FAILED' or STATE == 'CANCELLED':
                    print(STATE)
                    raise Exception("error: not allow to get data; maybe it was failed or cancelled.")
                if STATE == "SUCCEEDED":
                    print("Get data!")
                    break

        ## STEP 3 : get data of query
        file_query_solved = query_id["QueryExecutionId"] + ".csv"
        
        return file_query_solved, ATHENA_S3_OUTPUT
    except Exception as e:
        print("error")
        print(e)
        raise e

def processing_graphql_request(gql_request_field):
    '''
        Convert GraphQL request to object to manage field and relations.
    '''
    
    
    

def lambda_handler(event, context):
    '''
        Handler endpoint of lambda for user requests.
    '''
    print(event)

    try:
        return {
            "id": 1,
            "name": "Arequipa",
            "countryID":  {
                "currencyISO": "SOL",
                "id": 100,
                "name": "CarlosChicata",
                "prefixPhone": "+051",
                "region": "Perú"
            }
        }

    except Exception as e:
        print("error")
        print(e)
        return {}

gplr = [
      'address', # -> 1
      'cityID', # -> 1*
      'cityID/id', # -> 2 
      'cityID/countryID', # -> 2*
      'cityID/countryID/currencyISO', # -> 3
      'cityID/countryID/id', # -> 3
      'cityID/countryID/name', # ->  3
      'cityID/name', # -> 2
      'commercialName', # -> 1 
      'enterprise_key' # ->  1
    ]
processing_graphql_request(gplr)
