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
### Generate "SQL process" table

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
            ) as "counting delivered orders",
            count(*) as  "total_orders"
        FROM "db-poc-case-1"."order_table" as "o"
        JOIN "db-poc-case-1"."trackcode_table" as "t"
            on "t"."id" = "o"."trackcode_id"
        JOIN "db-poc-case-1"."client_table" as "cl"
            on "cl"."id" = "t"."client_id"
        WHERE "t"."creation" BETWEEN '{0}' and '{1}' and "cl"."enterpris_key" = '{2}';
    '''
SQL_TEMPLATE_count_orders_by_range = '''
        SELECT count(*)
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
    '''
    sql_process_table_data.append(Row(
        id=index+1,
        sql_command=SQL_TEMPLATE[endpoints[index]],
        version="v1",
        created_at=datetime_now,
        finished_in=None,
        process=endpoints[index],
        description=ENDPOINT_DESCRIPTION[endpoints[index]]
    ))
    '''
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
    StructField('description', StringType(), True),
])

sql_process_table_df = spark.createDataFrame(sql_process_table_data, sql_process_table_schema)
sql_process_table_df.printSchema()
temp_name_table = "temp_sql_process_table"

sql_process_table_df.createOrReplaceTempView(temp_name_table)

### save in data lake in iceberg table
sql_stmnt = """
    CREATE OR REPLACE TABLE iceberg_catalog.%s.%s
    USING iceberg
    TBLPROPERTIES ('table_type'='ICEBERG', 'format-version'='2', 'format'='parquet')
    LOCATION 's3://s3-storage-layer-poc-5/glue/data/db_poc_case_fourth/csv_to_iceberg_glue'
    AS SELECT * FROM %s
    """ % (glue_schema_db, "sql_process", temp_name_table,)
print(sql_stmnt)
spark.sql(sql_stmnt).show()

spark.catalog.dropTempView(sql_stmnt)

job.commit()