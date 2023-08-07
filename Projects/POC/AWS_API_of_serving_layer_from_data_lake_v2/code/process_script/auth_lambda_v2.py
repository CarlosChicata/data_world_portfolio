'''
    Generate a authorizer lambda to handle the authorize and authenticate 
    of endpoints in the REST API service.

    NOTE:
     you need a pandas, use a layer from: https://api.klayers.cloud//api/v2/p3.9/layers/latest/us-east-1/html
'''
import time
import io


import pandas as pd
#from boto3 import Session
import boto3


ACCESS_KEY = ""
SECRET_KEY = ""
SQL_command = '''
    select ac.id,
        cac.id,
        sp.id,
        cac.access_control_id,
        ac.enterprise_key,
        sp.sql_command,
        cac.columns
    from "access_controls" ac 
    join "column_of_access_control" cac 
    on cac.access_control_id = ac.id
    join "sql_process" sp 
    on sp.id = cac.sql_body_id
    where ac."enterprise_key" = '{0}' 
        and ac."{1}" = true
        and sp."process" = '{2}';
'''

S3_OUTPUT = "s3://pruebas-generales-para/" # ENV PARAMS
S3_BUCKET = "pruebas-generales-para" # ENV PARAMS
s3_cli = boto3.client('s3')
athena_cli = boto3.client('athena')

def generate_policy(principal_id, effect, method_arn, columns, sql_comm, enterprise_key):
    '''
        Generate a policy to authorize request access the endpoint.
    '''
    auth_response = {}
    auth_response['principalId'] = principal_id

    if effect and method_arn:
        policy_document = {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Sid': 'FirstStatement',
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': method_arn
                }
            ]
        }
 
        auth_response['policyDocument'] = policy_document

    return auth_response


def get_data_from_athena(key_enterprise, process_name):
    '''
        How to get data to validate from aws athena table.

        Params:
        key_enterprise (string): key of client to access.
        process_name (string): name of available process in serving layer 

        Return a flag to indicate of access.

        This Flag can be:
        * -1 = no authorized
        * 0 = authorized but denied operation
        * 1 = authorized and accepted operation
    '''
    try:
        tic = time.perf_counter()
        query = SQL_command.format(key_enterprise, process_name,process_name)
        print(query)
        STATE = "RUNNING"
        MAX_EXECUTION = 10

        ## STEP 1 : go the SQL sentence to athena
        query_id = athena_cli.start_query_execution(
            QueryString = query,
            QueryExecutionContext = {
                "Database": "db_poc_case_fifth"
            },
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
                    print(response)
                    print(STATE)
                    raise Exception("error: not allow to get data; maybe it was failed or cancelled.")
                if STATE == "SUCCEEDED":
                    print("Get data!")
                    break

            time.sleep(0.3)

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
            return (-1, None, None)
        else:
            toc = time.perf_counter()
            print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
            if df_solved.iloc[0]["sql_command"] != None and  df_solved.iloc[0]["columns"] != None:
                return (1, df_solved.iloc[0]["sql_command"], df_solved.iloc[0]["columns"] )
            else: 
                return (0, None, None)
    except Exception as e:
        print(e)
        toc = time.perf_counter()
        print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
        return (-1, None, None)


def lambda_handler(event, context):
    '''
        Handler endpoint of lambda for user requests.
    '''
    event['methodArn'] = event["routeArn"]
    try:
        if event["headers"]["token"] is None:
            print("case 0")
            return generate_policy(None, 'Deny', event['routeArn'])
        
        path_service = event["rawPath"].split("/")[-1]
        
        print(event["headers"]["token"])
        print(path_service)
        
        is_validated = get_data_from_athena(
                event["headers"]["token"],
                path_service
            )
            
        print(is_validated[0])
        if is_validated[0] == 1: 
            print("case 1: accepted and authorized")
            return generate_policy('user', 'Allow', event['routeArn'], is_validated[2], is_validated[1], event["headers"]["token"])
        elif is_validated[0] == 0:
            print("case 2: accepted and not authorized")
            return generate_policy('user', 'Deny', event['routeArn'], is_validated[2], is_validated[1], event["headers"]["token"])
        else:
            print("case 3: unauthorized")
            return generate_policy(None, 'Deny', event['routeArn'], is_validated[2], is_validated[1], event["headers"]["token"])

    except Exception as e:
        print("error")
        print(e)
        return generate_policy(None, 'Deny', event['routeArn'])
