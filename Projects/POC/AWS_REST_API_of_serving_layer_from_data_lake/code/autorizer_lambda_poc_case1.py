'''
    Generate a authorizer lambda to handle the authorize and authenticate 
    of endpoints in the REST API service.
'''
import time


from boto3 import Session


ACCESS_KEY = ""
SECRET_KEY = ""
STATE = "RUNNING"
MAX_EXECUTION = 5

session = Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

tic = time.perf_counter()
athena_cli = session.client("athena", region_name="us-east-1")

### process
## go the SQL sentence to athena
query_id = athena_cli.start_query_execution(
    QueryString = 'SELECT * FROM "control-access-test"."access_control_table" limit 10;',
    ResultConfiguration= {"OutputLocation": "s3://pruebas-generales-para/"},
    WorkGroup = "primary"
)
print(query_id)

## waiting the finish operation: asynchronic ops

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

    time.sleep(30)



## get data of query
response = athena_cli.get_query_results(
    QueryExecutionId=query_id["QueryExecutionId"]
)

results = response["ResultSet"]["Rows"]
print(results)
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")