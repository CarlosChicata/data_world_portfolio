import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkConf, SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, when, regexp_replace


# get passed params from aws glue job
args = getResolvedOptions(
    sys.argv, 
    ['JOB_NAME','bucket_origin', 'glue_schema_db']
)

# check
bucket_origin = args["bucket_origin"]
glue_schema_db = args["glue_schema_db"]

print(bucket_origin, sep="\n")

# setup the spark session in my aws glue job
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

### define utiity functions

def processing_data(object_bucket_origin, name_table, rename_cols, filter_column, clean_column):
    
    # read the csv file in dynamicframe obj.
    csv_file_s3_url = "s3://" +  bucket_origin + "/" + object_bucket_origin

    print(csv_file_s3_url)

    df = spark.read.format("csv").option("delimiter", ";").option("encoding", "utf-16").option("header", True).load(csv_file_s3_url)

    print(df.show(2))

    df = df.filter(
            ~(col(filter_column).contains("�"))
        )
    
    print(df.show(2))
    
    # remove useless unknown character
    df = df.withColumn(clean_column, 
        when(df[clean_column].contains("�"), (regexp_replace(df[clean_column],"�", "")))
    )

    # rename based in new columns
    for old_name, new_name in rename_cols:
        df = df.withColumnRenamed(old_name, new_name)

    print(df.show(2))
    print(df.count())

    # create tem tamble with data from csv file inside spark
    temp_name_table = "temp" + name_table
    df.registerTempTable(temp_name_table)

    # write a iceberg table in glue catalog using csv file
    sql_stmnt = """
    CREATE OR REPLACE TABLE iceberg_catalog.%s.%s
    USING iceberg
    TBLPROPERTIES ('table_type'='ICEBERG', 'format-version'='2', 'format'='parquet')
    LOCATION 's3://s3-storage-layer-poc-5/glue/data/db_poc_case_fourth/csv_to_iceberg_glue'
    AS SELECT * FROM %s
    """ % (glue_schema_db, name_table, temp_name_table,)
    print(sql_stmnt)
    spark.sql(sql_stmnt).show()

### main processes
'''
processing_data(
    "fake_city_table.csv", 
    "city_table", 
    [('"cityPoint"�', "city_point"),("countryID","country_id"), ("timeZone","timezone")],
    "name",
    '"cityPoint"�',
)

processing_data(
    "fake_client_table.csv",
    "client_table",
    [("businessName", "business_name"), ("comercialName", "comercial_name"),("cityID","city_id"),("serviceIDs","service_ids"),('"enterpriseKey"�',"enterprise_key")],
    "id",
    '"enterpriseKey"�'
)

processing_data(
    "fake_country_table.csv",
    "country_table",
    [("prefixPhone", "prefix_phone"), ('"currencyISO"�', "currency_iso")],
    "id",
    '"currencyISO"�'
)

processing_data(
    "fake_order_table.csv",
    "order_table",
    [("orderID", "order_id"),("routeID", "route_id"),("promiseTime","promise_time"), ("startTime","start_time"), ('"endTime"�', "end_time")],
    "orderID",
    '"endTime"�'
)
'''

processing_data(
    "fake_product_size_table.csv",
    "product_size_table",
    [("dimX", "dim_x"), ("dimY", "dim_y"), ('"dimZ"�', "dim_z")],
    "id",
    '"dimZ"�'
)

job.commit()

