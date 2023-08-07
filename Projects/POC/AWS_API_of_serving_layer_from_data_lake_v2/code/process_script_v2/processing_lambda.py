import time
import io
import json


import pandas as pd
import boto3



def lambda_handler(event, context):
    # TODO implement
    print(event)
    context_fields = event["requestContext"]["authorizer"]["lambda"]
    columns = ", ".join(context_fields["columns"])
    command = context_fields["command"]
    enterprise_key = context_fields["enterprise_key"]
    command_sql = command % ('2023-02-10 00:00', '2023-05-10 00:00', enterprise_key, columns)
    return {
        'statusCode': 200,
        'body': json.dumps('Hola Carlitos o Jessica o Zayda o Melita o Ariani o Ethel')
    }
