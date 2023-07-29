import sys
import random
import uuid
from datetime import datetime

from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkConf, SparkContext
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
from awsglue.context import GlueContext
from awsglue.job import Job


# setting spark enviroment

args = getResolvedOptions(
    sys.argv,
    ['JOB_NAME', 'glue_schema_db']
)

glue_schema_db = args["glue_schema_db"]

conf_list = [
    #General Spark configs
    ("hive.metastore.client.factory.class", "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"),
    ("spark.sql.parquet.writeLegacyFormat", "true"),
    ("spark.sql.parquet.writeLegacyFormat", "true"),
    ("hive.exec.dynamic.partition.mode", "nonstrict"),
    ("spark.sql.hive.caseSensitiveInferenceMode", "INFER_ONLY"),
    ("spark.sql.source.partitinoOverviewMode", "dynamic"),
    #Configs needed for Iceberg
    ("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"),
    ("spark.sql.catalog.iceberg_catalog", "org.apache.iceberg.spark.SparkCatalog"),
    ("spark.sql.catalog.iceberg_catalog.warehouse", "s3:///s3-storage-layer-poc-5/iceberg_catalog/"),
    ("spark.sql.catalog.iceberg_catalog.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog")
]

spark_conf = SparkConf().setAll(conf_list)
spark = SparkSession.builder.config(conf=spark_conf).enableHiveSupport().getOrCreate()
glue_context = GlueContext(spark.sparkContext)
job = Job(glue_context)
job.init(args['JOB_NAME'], args)

##### PROCESS
###############
### Generate "SQL process" table
###############

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
columns_in_endpoints = {
    "all_orders_by_range": [
        '"t"."id" as "trackcode_id"', 
        '"cl"."enterpris_key"', 
        '"t"."creation"', 
        '"t"."crossdocking"',
        '"t"."pickup_address"', 
        '"t"."drop_address"', 
        '"t"."product_description"', 
        '"cl"."business_name"', 
        '"t"."product_weight"',
        '"t"."product_price"', 
        '"cl"."comercial_name"', 
        '"s"."name" as "service_name"', 
        '"c"."name" as "city_name"'],
    "get_money_from_routes_by_range": [
        '"r"."id" as "route_id"', 
        '"r"."code" as "route_code"', 
        '"t"."id" as "trackcode_id"', 
        'coalesce("r"."price_official", 10.0) as "price"',
        '"r"."distance"', 
        '"t"."pickup_address"', 
        '"t"."drop_address"', 
        '"s"."name" as "service_name"', 
        '"t"."creation"', 
        '"cl"."enterpris_key"'], 
    "most_visited_location_from_trackcode_by_range": [
        'DATE(CAST("t"."creation" as TIMESTAMP)) as "date_creation"', 
        '"c"."name"', 
        'count(*)  as "amount"'], 
    "count_trackcode_by_range": [
        'DATE(CAST("t"."creation" as TIMESTAMP)) as "date_creation"', 
        'count(*) as "counting"' 
    ], 
    "count_orders_by_range": ['count(*) as "count"'], 
    "count_trackcode_lost_by_range": ['"t"."id" as "trackcode_id"'], 
    "most_required_service_by_range": [
        '"s"."name"',
        'count(*) as "counting"'], 
    "count_delivered_trackcode_before_promise_time_by_range": [
        'count(*) as "total_orders"', 
        'case when "o"."end_time" is not null and "o"."end_time" >= "o"."promise_time" then 1 else null  end ) as "counting delivered orders"'
    ]
}
selected_field_in_endpoints = [
    "get_money_from_routes_by_range",
    "all_orders_by_range"
]

SQL_TEMPLATE_all_orders_by_range = '''
        SELECT distinct "t"."id" as "trackcode_id", "cl"."enterpris_key", "t"."creation",  
            "t"."crossdocking", "t"."pickup_address", "t"."drop_address", "t"."product_description", 
            "t"."product_price", "t"."product_weight", "cl"."business_name", 
            "cl"."comercial_name", "s"."name" as "service_name", "c"."name" as "city_name"
        FROM "db-poc-case-1"."trackcode_table" as "t"
        RIGHT JOIN "db-poc-case-1"."client_table"  as "cl"
            on "t"."client_id" = "cl"."id"
        RIGHT JOIN "db-poc-case-1"."service_table"  as "s"
            on "t"."service_id" = "s"."id"
        RIGHT JOIN "db-poc-case-1"."city_table"  as "c"
            on "cl"."city_id" = "c"."id"
        WHERE "t"."creation" BETWEEN '{0}' and '{1}' and "cl"."enterpris_key" = '{2}';
    '''
SQL_TEMPLATE_count_delivered_trackcode_before_promise_time_by_range = '''
        SELECT count( 
                case when "o"."end_time" is not null and "o"."end_time" >= "o"."promise_time"
                    then 1 
                    else null 
                end
            ) as "counting_delivered_orders",
            count(*) as  "total_orders"
        FROM "db-poc-case-1"."order_table" as "o"
        JOIN "db-poc-case-1"."trackcode_table" as "t"
            on "t"."id" = "o"."trackcode_id"
        JOIN "db-poc-case-1"."client_table" as "cl"
            on "cl"."id" = "t"."client_id"
        WHERE "t"."creation" BETWEEN '{0}' and '{1}' and "cl"."enterpris_key" = '{2}';
    '''
SQL_TEMPLATE_count_orders_by_range = '''
        SELECT count(*) as "count"
        FROM "db-poc-case-1"."order_table" as "o"
        JOIN "db-poc-case-1"."trackcode_table" as "t"
            on "t"."id" = "o"."trackcode_id"
        JOIN "db-poc-case-1"."client_table" as "cl"
            on "cl"."id" = "t"."client_id"
        WHERE "t"."creation" BETWEEN '{0}' and '{1}' and "cl"."enterpris_key" = '{2}';
    '''
SQL_TEMPLATE_count_trackcode_by_range = '''
        SELECT distinct DATE(CAST("t"."creation" as TIMESTAMP)) as "date_creation", count(*) as "counting"
        FROM "db-poc-case-1"."trackcode_table" as "t"
        JOIN "db-poc-case-1"."client_table"  as "cl"
            on "t"."client_id" = "cl"."id"
        WHERE "t"."creation" BETWEEN '{0}' and '{1}' and "cl"."enterpris_key" = '{2}'
        GROUP BY DATE(CAST("t"."creation" as TIMESTAMP));
    '''
SQL_TEMPLATE_count_trackcode_lost_by_range = '''
        SELECT distinct "t"."id" as "trackcode_id"
        FROM "db-poc-case-1"."route_table" as "r"
        JOIN "db-poc-case-1"."order_table" as "o"
            on "o"."route_id" = "r"."id"
        JOIN "db-poc-case-1"."trackcode_table" as "t"
            on "t"."id" = "o"."trackcode_id"
        JOIN "db-poc-case-1"."client_table" as "cl"
            on "cl"."id" = "t"."client_id"
        WHERE "t"."creation" BETWEEN '{0}' and '{1}' and "cl"."enterpris_key" = '{2}' and "o"."start_time" is null
        GROUP BY "t"."id";
    '''
SQL_TEMPLATE_get_money_from_routes_by_range = '''
        SELECT DISTINCT "r"."id" as "route_id", "r"."code" as "route_code", "t"."id" as "trackcode_id",
            coalesce("r"."price_official", 10.0) as "price", 
            "r"."distance", 
            "t"."pickup_address", "t"."drop_address",
            "s"."name" as "service_name", "t"."creation", "cl"."enterpris_key"
        FROM "db-poc-case-1"."route_table" as "r"
        JOIN "db-poc-case-1"."order_table" as "o"
            on "o"."route_id" = "r"."id"
        JOIN "db-poc-case-1"."trackcode_table" as "t"
            on "t"."id" = "o"."trackcode_id"
        JOIN "db-poc-case-1"."city_table" as "c"
            on "c"."id" = "r"."city_id"
        JOIN "db-poc-case-1"."client_table" as "cl"
            on "cl"."id" = "t"."client_id"
        JOIN "db-poc-case-1"."service_table" as "s"
            on "s"."id" = "t"."service_id"
        WHERE "t"."creation" BETWEEN '{0}' and '{1}' and "cl"."enterpris_key" = '{2}';
    '''
SQL_TEMPLATE_most_required_service_by_range = '''
        SELECT distinct "s"."name", count(*) as "counting"
        FROM "db-poc-case-1"."trackcode_table" as "t"
        JOIN "db-poc-case-1"."client_table" as "cl"
            on "cl"."id" = "t"."client_id"
        JOIN "db-poc-case-1"."city_table" as "c"
            on "c"."id" = "cl"."city_id"
        JOIN "db-poc-case-1"."service_table" as "s"
            on "s"."id" = "t"."service_id"
        WHERE "t"."creation" BETWEEN '{0}' and '{1}' and "cl"."enterpris_key" = '{2}'
        GROUP BY "s"."name;
    '''
SQL_TEMPLATE_most_visited_location_from_trackcode_by_range = '''
        SELECT distinct DATE(CAST("t"."creation" as TIMESTAMP)) as "date_creation", "c"."name", count(*)  as "amount"
        FROM "db-poc-case-1"."trackcode_table" as "t"
        RIGHT JOIN "db-poc-case-1"."client_table"  as "cl"
            ON "t"."client_id" = "cl"."id"
        RIGHT JOIN "db-poc-case-1"."city_table"  as "c"
            ON "cl"."city_id" = "c"."id"
        WHERE "t"."creation" BETWEEN '{0}' and '{1}' and "cl"."enterpris_key" = '{2}'
        GROUP BY DATE(CAST("t"."creation" as TIMESTAMP)), "c"."name";
    '''

SQL_TEMPLATE = {
    "all_orders_by_range" : SQL_TEMPLATE_all_orders_by_range,
    "get_money_from_routes_by_range": SQL_TEMPLATE_get_money_from_routes_by_range,
    "most_visited_location_from_trackcode_by_range": SQL_TEMPLATE_most_visited_location_from_trackcode_by_range,
    "count_trackcode_by_range": SQL_TEMPLATE_count_trackcode_by_range,
    "count_orders_by_range": SQL_TEMPLATE_count_orders_by_range,
    "count_trackcode_lost_by_range": SQL_TEMPLATE_count_trackcode_lost_by_range,
    "most_required_service_by_range": SQL_TEMPLATE_most_required_service_by_range,
    "count_delivered_trackcode_before_promise_time_by_range": SQL_TEMPLATE_count_delivered_trackcode_before_promise_time_by_range,
}

ENDPOINT_DESCRIPTION = {
    "all_orders_by_range" : "Get all detailed trackcode based in datetime range",
    "get_money_from_routes_by_range": "Get all money generated by the routes and detailed in range of datetime",
    "most_visited_location_from_trackcode_by_range": "Get the most visited location from the trackcodes in range of datetime",
    "count_trackcode_by_range": "The number of trackcode generated based date in range of datetime",
    "count_orders_by_range": "The number of orders by code generated during a date range",
    "count_trackcode_lost_by_range": "The number of trackcodes lost",
    "most_required_service_by_range": "The most required service using during a date range",
    "count_delivered_trackcode_before_promise_time_by_range": "Check how many orders are success delivery before the promise time in date range",
}


sql_process_table_data = []
datetime_now = datetime.now()

for index in range(len(endpoints)):
    sql_process_table_data.append(Row(
        id=index+1,
        sql_command=SQL_TEMPLATE[endpoints[index]],
        version="v1",
        created_at=datetime_now,
        finished_in=None,
        process=endpoints[index],
        description=ENDPOINT_DESCRIPTION[endpoints[index]]
    ))

print(sql_process_table_data)
sql_process_table_schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('sql_command', StringType(), False),
    StructField('version', StringType(), False),
    StructField('created_at', TimestampType(), False),
    StructField('finished_in', TimestampType(), True),
    StructField('process', StringType(), False),
    StructField('description', StringType(), True)
])

sql_process_table_df = spark.createDataFrame(sql_process_table_data, sql_process_table_schema)
sql_process_table_df.printSchema()
temp_name_table = "temp_sql_process_table"

sql_process_table_df.createOrReplaceTempView(temp_name_table)

#### save in data lake in iceberg table
sql_stmnt = """
    CREATE OR REPLACE TABLE iceberg_catalog.%s.%s
    USING iceberg
    TBLPROPERTIES ('table_type'='ICEBERG', 'format-version'='2', 'format'='parquet')
    LOCATION 's3://s3-storage-layer-poc-5/glue/data/db_poc_case_fourth/csv_to_iceberg_glue'
    AS SELECT * FROM %s
    """ % (glue_schema_db, "sql_process", temp_name_table,)
print(sql_stmnt)
spark.sql(sql_stmnt).show()

spark.catalog.dropTempView(temp_name_table)
sql_process_table_data = []

###############
### Generate "access control" table
###############

fake_users_account = random.randint(50, 100)
sql_access_control_data = []

client_df = glue_context.create_data_frame.from_catalog(
    database=glue_schema_db,
    table_name="client_table"
)

for fake_user_id in range(fake_users_account):
    flag_endpoint = [ random.uniform(0, 1) < 0.5 for _ in range(len(endpoints)) ]
    random_client_id = random.randint(0, client_df.count())
    uuid_value = str(uuid.uuid4())
    client_id = client_df.collect()[random_client_id]["id"]
    print(client_df.collect()[random_client_id])
    print(uuid_value,client_id, random_client_id)
    
    row_data = { key: value for key,value in zip(endpoints, flag_endpoint) }
    temp_fake_user_id = fake_user_id + 1
    sql_access_control_data.append(Row(
            id=temp_fake_user_id,
            enterprise_key=uuid_value,
            client_id=client_id,
            all_orders_by_range=row_data["all_orders_by_range"],
            get_money_from_routes_by_range=row_data["get_money_from_routes_by_range"], 
            most_visited_location_from_trackcode_by_range=row_data["most_visited_location_from_trackcode_by_range"], 
            count_trackcode_by_range=row_data["count_trackcode_by_range"], 
            count_orders_by_range=row_data["count_orders_by_range"], 
            count_trackcode_lost_by_range=row_data["count_trackcode_lost_by_range"], 
            most_required_service_by_range=row_data["most_required_service_by_range"], 
            count_delivered_trackcode_before_promise_time_by_range=row_data["count_delivered_trackcode_before_promise_time_by_range"]
        ))

print(sql_access_control_data)
print(len(sql_access_control_data))
access_control_table_df = spark.createDataFrame(sql_access_control_data)

access_control_table_df.printSchema()
temp_name_table = "temp_access_controls_table"

access_control_table_df.createOrReplaceTempView(temp_name_table)

#### save in data lake in iceberg table
sql_stmnt = """
    CREATE OR REPLACE TABLE iceberg_catalog.%s.%s
    USING iceberg
    TBLPROPERTIES ('table_type'='ICEBERG', 'format-version'='2', 'format'='parquet')
    LOCATION 's3://s3-storage-layer-poc-5/glue/data/db_poc_case_fourth/csv_to_iceberg_glue'
    AS SELECT * FROM %s
    """ % (glue_schema_db, "access_controls", temp_name_table,)
print(sql_stmnt)
spark.sql(sql_stmnt).show()

spark.catalog.dropTempView(temp_name_table)
sql_access_control_data = []

###############
### Generate "column of access control" table
###############

sql_column_of_access_control_data = []
iter_column_of_access_control = 1

for row in access_control_table_df.collect():
    for endpoint in endpoints:
        if row[endpoint] == True:
            index_endpoint = endpoints.index(endpoint) + 1
            fields_in_query = columns_in_endpoints[endpoint]
            
            # case its too much columns
            if endpoint in selected_field_in_endpoints:
                get_columns = columns_in_endpoints[endpoint]
                column_acount = random.randint(1,len(get_columns))
                fields_in_query = random.sample(get_columns, column_acount)
                
            
            sql_column_of_access_control_data.append(Row(
                id=iter_column_of_access_control,
                access_control_id=row["id"],
                process_key='',
                sql_body_id=index_endpoint,
                columns=fields_in_query
            ))
            iter_column_of_access_control += 1

print(len(sql_column_of_access_control_data))
column_of_access_control_df = spark.createDataFrame(sql_column_of_access_control_data)

column_of_access_control_df.printSchema()
temp_name_table = "temp_column_of_access_control"

column_of_access_control_df.createOrReplaceTempView(temp_name_table)
sql_stmnt = """
    CREATE OR REPLACE TABLE iceberg_catalog.%s.%s
    USING iceberg
    TBLPROPERTIES ('table_type'='ICEBERG', 'format-version'='2', 'format'='parquet')
    LOCATION 's3://s3-storage-layer-poc-5/glue/data/db_poc_case_fourth/csv_to_iceberg_glue'
    AS SELECT * FROM %s
    """ % (glue_schema_db, "column_of_access_control", temp_name_table,)
print(sql_stmnt)
spark.sql(sql_stmnt).show()

spark.catalog.dropTempView(temp_name_table)
sql_column_of_access_control_data = []


job.commit()
