import chunk
from boto3 import Session
import pandas as pd

'''
ACCESS_KEY = ""
SECRET_KEY = ""

session = Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

athena_cli = session.client("athena", region_name="us-east-1")
'''


def sending_batch_data(size_chunk):
    '''
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
