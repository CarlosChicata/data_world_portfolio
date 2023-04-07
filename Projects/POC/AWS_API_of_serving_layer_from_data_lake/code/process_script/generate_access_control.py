'''
    Generate a random access control endpoint table.
'''
import random

import pandas as pd


df = pd.read_csv(
    "./fake_data/fake_client_table.csv",
    encoding =  "utf-16",
    sep=";"
)
endpoints = [
    "all_orders_by_range",
    "get_money_from_routes_by_range", 
    "most_visited_location_from_trackcode_by_range", 
    "count_trackcode_by_range", 
    "count_orders_by_range", 
    "count_trackcode_lost_by_range", 
    "most_required_service_by_range", 
    "count_delivered_trackcode_before_promise_time_by_range"
]
for endpoint in endpoints:
    df[endpoint] = [
        random.random() > 0.2 for _ in range(df.shape[0])
    ]

endpoints.append("id")
endpoints.append("enterpriseKey")

df = df[endpoints]
print(df.columns)

df.to_parquet("./fake_parquet/access_control_table.parquet")