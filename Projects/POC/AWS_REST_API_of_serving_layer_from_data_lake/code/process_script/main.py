'''

This file generate a new fake data based in previous fake data table.


'''
import pandas as pd


def generate_country_table():
    '''
        Generate a official table of country.
    '''
    
    df = pd.read_csv(
        "./fake_data/fake_country_table.csv",
        encoding =  "utf-16",
        sep=";"
    )
    df.to_parquet("./fake_parquet/country_table.parquet")
    

def generate_city_table():
    '''
        Generate a official table of city.
    '''
    df = pd.read_csv(
        "./fake_data/fake_city_table.csv",
        encoding =  "utf-16",
        sep=";"
    )
    df["name"] = df['name'].apply(str.lower)
    df.rename(columns={
        "countryID": "country_id",
        "timeZone": "timezone"
    }, inplace=True)
    df = df.drop(columns=["cityPoint"])
    df.to_parquet("./fake_parquet/city_table-gzip.parquet", compression="gzip")


def generate_client_table():
    '''
        Generate a official table of client.
    '''
    df = pd.read_csv(
        "./fake_data/fake_client_table.csv",
        encoding =  "utf-16",
        sep=";"
    )
    df["businessName"] = df["businessName"].astype("str")
    df["comercialName"] = df["comercialName"].astype("str")
    df["businessName"] = df['businessName'].apply(str.lower)
    df["comercialName"] = df['comercialName'].apply(str.lower)
    df.rename(columns={
        "comercialName": "comercial_name",
        "businessName": "business_name",
        "enterpriseKey": "enterpris_key",
        "cityID": "city_id"
    }, inplace=True)
    #df_final.to_parquet("./fake_parquet/client_table.parquet")
    ### test
    df_final = []
    df_test = df.head(5)
    for index, row in df_test.iterrows():
        service_ids = row["serviceIDs"].replace(" ", "")
        service_ids = service_ids.replace("{", "")
        service_ids = service_ids.replace("}", "")
        service_ids = service_ids.split(",")
        service_ids = [ int(x) for x in service_ids]
        for service_id in service_ids:
            row["serviceIDs"] = service_id
            df_final.append(row.to_dict())
    df_final = pd.DataFrame(df_final)
    df_final.to_parquet("./fake_parquet/client_table.parquet")


def generate_product_size_table():
    '''
        Generate a official table of product size.
    '''
    df = pd.read_csv(
        "./fake_data/fake_product_size_table.csv",
        encoding =  "utf-16",
        sep=";"
    )
    df["name"] = df["name"].astype("str")
    df["name"] = df['name'].apply(str.lower)
    df.rename(columns={
        "dimX": "dim_x",
        "dimY": "dim_y",
        "dimZ": "dim_z"
    }, inplace=True)
    df.to_parquet("./fake_parquet/product_size_table.parquet")


def generate_service_table():
    '''
        Generate a official table of service.
    '''
    df = pd.read_csv(
        "./fake_data/fake_service_table.csv",
        encoding =  "utf-16",
        sep=";"
    )
    df["name"] = df['name'].apply(str.lower)
    df.to_parquet("./fake_parquet/service_table.parquet")


def generate_trackcode_table():
    '''
        Generate a official table of trackcode.
    '''
    df = pd.read_csv(
        "./fake_data/fake_trackcode_table.csv",
        encoding =  "utf-16",
        sep=";"
    )
    df.rename(columns={
        "createdAt": "creation",
        "enterpriseID": "client_id",
        "pickUpAddress": "pickup_address",
        "dropAddress": "drop_address",
        "serviceID": "service_id",
        "productDescription": "product_description",
        "productPrice": "product_price",
        "packageSizeID": "product_size_id",
        "packageWeight": "product_weight",
        "dropPoint": "drop_point",
        "pickUpPoint": "pickup_point"
    }, inplace=True)
    df.to_parquet("./fake_parquet/trackcode_table.parquet")


def generate_route_table():
    '''
        Generate a official table of route.
    '''
    df = pd.read_csv(
        "./fake_data/fake_route_table.csv",
        encoding =  "utf-16",
        sep=";"
    )
    df.rename(columns={
        "cityID": "city_id",
        "routeCode": "code",
        "priceOriginal": "price_original",
        "priceIncentive": "price_with_incentive",
        "estimatedTotalDistance": "distance",
        "price": "price_official"
    }, inplace=True)
    df = df.drop(columns=["incentive"])
    df.to_parquet("./fake_parquet/route_table.parquet")


def generate_order_table():
    '''
        Generate a official table of order.
    '''
    df = pd.read_csv(
        "./fake_data/fake_order_table.csv",
        encoding =  "utf-16",
        sep=";"
    )
    df.rename(columns={
        "orderID": "trackcode_id",
        "routeID": "route_id",
        "promiseTime": "promise_time",
        "startTime": "start_time", 
        "endTime": "end_time"
    }, inplace=True)
    df.to_parquet("./fake_parquet/order_table.parquet")


############ MAIN ############

generate_country_table()
generate_city_table()
generate_client_table()
generate_product_size_table()
generate_service_table()
generate_trackcode_table()
generate_route_table()
generate_order_table()

