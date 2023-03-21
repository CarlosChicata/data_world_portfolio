'''

function to manage the query #3


'''
import io
import json
import time

import boto3
import pandas as pd


# setups of lambda

s3_cli = boto3.client('s3')
athena_cli = boto3.client('athena')


S3_OUTPUT = "s3://pruebas-generales-para/" # ENV PARAMS
S3_BUCKET = "pruebas-generales-para" # ENV PARAMS


def get_data_from_athena(event):
    '''
        Get data from AWS ATHENA.

        Params:
        start_time ( "YYYY-MM-DD" str) : start datetime of range.
        end_time ( "YYYY-MM-DD" str) : end datetime of range.

        return a JSON dict
    '''

    ## STEP 0 : preparring query to get data
    query = '''
        SELECT distinct DATE(CAST("t"."creation" as TIMESTAMP)) as "date_creation", "c"."name", count(*)  as "amount"
        FROM "db-poc-case-1"."trackcode_table" as "t"
        RIGHT JOIN "db-poc-case-1"."client_table"  as "cl"
            ON "t"."client_id" = "cl"."id"
        RIGHT JOIN "db-poc-case-1"."city_table"  as "c"
            ON "cl"."city_id" = "c"."id"
        WHERE "t"."creation" BETWEEN '{0}' and '{1}' and "cl"."enterpris_key" = '{2}'
        GROUP BY DATE(CAST("t"."creation" as TIMESTAMP)), "c"."name";
    '''.format(event["start_datetime"], event["end_datetime"], event["headers"]["token"])
    print(query)
    STATE = "RUNNING"
    MAX_EXECUTION = 10

    ## STEP 1 : go the SQL sentence to athena
    query_id = athena_cli.start_query_execution(
        QueryString = query,
        ResultConfiguration= {"OutputLocation": S3_OUTPUT}
    )
    print("request of query: ", query_id)

    ## STEP 2 : waiting the finish operation: asynchronic ops
    while MAX_EXECUTION > 0 and STATE in ["RUNNING", "QUEUED"]:
        MAX_EXECUTION -= 1
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
        Bucket=S3_BUCKET,
        Key=file_query_solved
    )
    df_solved = pd.read_csv(io.BytesIO(response['Body'].read()), encoding='utf8')

    ## STEP 4: return a data in JSON format
    return df_solved.to_json(orient="records")


def validated_obligaroty_fields(body, fields):
    '''
        Check if the request must have all needed fields in query.

        Params:
        body (dic): body of request.
        fields (list of string) : all fields need to work

        Return None or raise
    '''
    body_fields = set(body.keys())
    fields_set = set(fields)

    if len( fields_set & body_fields ) == len(fields_set):
        return None
    else:
        raise Exception("We need all needed fields: " + ", ".join(fields))


def lambda_handler(event, context):
    '''
        Handler endpoint of lambda for user requests.
    '''
    try:
        body = json.loads(event['body'])
        need_fields = [ "start_datetime", "end_datetime" ]
        body["headers"] = event["headers"]
        validated_obligaroty_fields(body, need_fields)
        data_req = get_data_from_athena(body)
        return {
            "headers": {
                "Content-Type": "application/json"
            },
            "statusCode": 200,
            "body": data_req
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }

