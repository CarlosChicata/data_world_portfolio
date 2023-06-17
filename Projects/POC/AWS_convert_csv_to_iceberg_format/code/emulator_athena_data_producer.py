from boto3 import Session
import pandas as pd

'''
ACCESS_KEY = "AKIA3KOPCZINQWXMWHNP"
SECRET_KEY = "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"

session = Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

athena_cli = session.client("athena", region_name="us-east-1")
'''


faked_dataset = pd.read_csv(
    "../data/faked_orders.csv",
    encoding='utf8',
    sep=";"
)
print(faked_dataset.shape)