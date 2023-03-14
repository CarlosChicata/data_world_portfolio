'''
    Generate a authorizer lambda to handle the authorize and authenticate 
    of endpoints in the REST API service.
'''
import time


from boto3 import Session



session = Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)


athena_cli = session.client("athena", region_name="us-east-1")
tic = time.perf_counter()


def get_data_from_athena(key_enterprise):
    '''
        How to get data to validate from aws athena table.

        Params:
        key_enterprise (string): key of client to access.

        Return a flag to indicate of access.
    '''
    query = '''
        SELECT * FROM "control-access-test"."access_control_table"
        where "enterprisekey" = '{0}';
    '''.format(key_enterprise)
    STATE = "RUNNING"
    MAX_EXECUTION = 10

    ## STEP 1 : go the SQL sentence to athena
    query_id = athena_cli.start_query_execution(
        QueryString = query,
        ResultConfiguration= {"OutputLocation": "s3://pruebas-generales-para/"},
        WorkGroup = "primary"
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
            if STATE == "SUCCEEDED":
                print("entramos")
                break

        time.sleep(8)

    ## STEP 3 : get data of query
    response = athena_cli.get_query_results(
        QueryExecutionId=query_id["QueryExecutionId"]
    )

    results = response["ResultSet"]["Rows"]
    print(results)
    print(len(results))
    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")




get_data_from_athena("f1bf44f9-ca62-4df3-93ac-90e0c3fc4dc9")

