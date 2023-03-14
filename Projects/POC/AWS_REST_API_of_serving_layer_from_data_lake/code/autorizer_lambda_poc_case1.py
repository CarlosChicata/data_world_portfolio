'''
    Generate a authorizer lambda to handle the authorize and authenticate 
    of endpoints in the REST API service.
'''
import time
import io


import pandas as pd
from boto3 import Session



ACCESS_KEY = ""
SECRET_KEY = ""
S3_OUTPUT = "s3://pruebas-generales-para/" # ENV PARAMS
S3_BUCKET = "pruebas-generales-para" # ENV PARAMS

session = Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)


athena_cli = session.client("athena", region_name="us-east-1")
s3_cli = session.client("s3")


def get_data_from_athena(key_enterprise, field):
    '''
        How to get data to validate from aws athena table.

        Params:
        key_enterprise (string): key of client to access.

        Return a flag to indicate of access.

        This Flag can be:
        * -1 = no authorized
        * 0 = authorized but denied operation
        * 1 = authorized and accepted operation
    '''
    try:
        tic = time.perf_counter()
        query = '''
            SELECT * FROM "control-access-test"."access_control_table"
            where "enterprisekey" = '{0}';
        '''.format(key_enterprise)
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
        
        ## STEP 4: generate a solution
        if df_solved.shape[0] == 0 or df_solved.shape[0] > 1:
            toc = time.perf_counter()
            print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
            return -1
        else:
            toc = time.perf_counter()
            print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
            return 1 if df_solved.iloc[0][field] == True else 0
    except Exception as e:
        print(e)
        toc = time.perf_counter()
        print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
        return -1




print(get_data_from_athena("f1bf44f9-ca62-4df3-93ac-90e0c3fc4dc9", "all_orders_by_range"))

