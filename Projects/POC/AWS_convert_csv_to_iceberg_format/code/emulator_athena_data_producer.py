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
    while chunk_iter <= top_limit_dataset:
        chunk_iter += size_chunk

        for idx in range(chunk_iter, min(chunk_iter + size_chunk, top_limit_dataset)):

    print(faked_dataset.shape)