import time

from boto3 import Session
import pandas as pd


ACCESS_KEY = ""
SECRET_KEY = ""

session = Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

athena_cli = session.client("athena", region_name="us-east-1")
S3_OUTPUT = ""


def send_data_to_athena_table(sql_query):
    '''
        execute the SQL query in athena

        Params
        sql_query (string): SQL query to run.
        return None
    '''
    STATE = "RUNNING"

    ## STEP 1 : go the SQL sentence to athena
    query_id = athena_cli.start_query_execution(
        QueryString = sql_query,
        ResultConfiguration= {"OutputLocation": S3_OUTPUT}
    )
    print("request of query: ", query_id)

    ## STEP 2 : waiting the finish operation: asynchronic ops

    while  STATE in ["RUNNING", "QUEUED"]:
        response = athena_cli.get_query_execution(
                QueryExecutionId=query_id["QueryExecutionId"]
            )

        if "QueryExecution" in response and \
            "Status" in response["QueryExecution"] and \
            "State" in response["QueryExecution"]["Status"]:

            STATE = response["QueryExecution"]["Status"]["State"]
            if STATE == 'FAILED' or STATE == 'CANCELLED':
                print("error in execution of query")
                raise Exception("error: not allow to get data; maybe it was failed or cancelled.")
            if STATE == "SUCCEEDED":
                print("Get data!")
                break
        
        time.sleep(10)

    return None


def sending_batch_data(size_chunk):
    '''
        Send data in batch mode from csv format file to iceberg file by AWS Athena.

        Params:
        size_chunk (int): number of element in chunk.

        return none
    '''
    if size_chunk >= 100:
        raise Exception("The size_chunk can't be more 100 because avoid limit in partitions athena.")

    faked_dataset = pd.read_csv(
        "../data/faked_orders.csv",
        encoding='utf8',
        sep=";"
    )
    chunk_iter = 0
    top_limit_dataset = faked_dataset.shape[0]
    top_limit_dataset = 5

    while chunk_iter <= top_limit_dataset:
        sql_data = [] 

        for idx in range(chunk_iter, min(chunk_iter + size_chunk, top_limit_dataset)):
            data = faked_dataset.iloc[[idx]].values.tolist()[0]
            data[4] = data[4][0:-6]
            sql_data.append(
                "(%s, '%s', %s, '%s', TIMESTAMP '%s', '%s')" % tuple(data)
            )

        sql_data = ",".join(sql_data)
        sql_insert = 'INSERT INTO csv_to_iceberg_order ("id","code", "enterprise_id", "size", "creation", "pick_address") values ' + sql_data
        print(sql_insert)
        chunk_iter += size_chunk

    print(faked_dataset.shape)


####  MAIN PROCESS
sending_batch_data(2)
