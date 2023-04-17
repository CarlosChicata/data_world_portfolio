'''
Proceso para mapear la consulta de GraphQL a SQL para Athena
'''
import time
import io
import os


import pandas as pd
from boto3 import Session
#import boto3


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


def get_data_from_sql_engine(query):
    '''
        Execute a SQL sentences and return data.
    '''
    try:
        # setting params to control de Athena
        STATE = "RUNNING"
        #MAX_EXECUTION = 10
        
        ## STEP 1 : go the SQL sentence to athena
        
        query_id = athena_cli.start_query_execution(
            QueryString = query,
            ResultConfiguration= {"OutputLocation": ATHENA_S3_OUTPUT},
            WorkGroup = ATHENA_WORKGROUP
        )

        ## STEP 2 : waiting the finish operation: asynchronic ops

        #while MAX_EXECUTION > 0 and STATE in ["RUNNING", "QUEUED"]:
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
                    raise Exception("error: not allow to get data; maybe it was failed or cancelled.")
                if STATE == "SUCCEEDED":
                    print("Get data!")
                    break

            time.sleep(8)

        ## STEP 3 : get data of query
        file_query_solved = query_id["QueryExecutionId"] + ".csv"
        
        response = s3_cli.get_object(
            Bucket=  ATHENA_S3_BUCKET_OUTPUT,
            Key=file_query_solved
        )
        
        df_solved = pd.read_csv(io.BytesIO(response['Body'].read()), encoding='utf8')
        
        return None
    except Exception as e:
        print("error")
        print(e)
        raise e


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
