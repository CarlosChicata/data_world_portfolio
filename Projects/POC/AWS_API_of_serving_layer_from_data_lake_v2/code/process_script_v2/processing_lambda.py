import time
import io
import json


import pandas as pd
import boto3



def lambda_handler(event, context):
    # TODO implement
    print(event)
    context_fields = event["requestContext"]["authorizer"]["lambda"]
    return {
        'statusCode': 200,
        'body': json.dumps('Hola Carlitos o Jessica o Zayda o Melita o Ariani o Ethel')
    }
