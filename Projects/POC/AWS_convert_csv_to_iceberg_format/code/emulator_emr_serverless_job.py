import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkConf, SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col


# get passed params from aws glue job
args = getResolvedOptions(
    sys.argv, 
    ['JOB_NAME','bucket_origin', "object_bucket_origin"]
)

# check
bucket_origin = args["bucket_origin"]
object_bucket_origin = args["object_bucket_origin"]

print(bucket_origin, object_bucket_origin, sep="\n")

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
    ("spark.sql.catalog.iceberg_catalog.warehouse", "s3://s3-storage-layer/iceberg_catalog/"),
    ("spark.sql.catalog.iceberg_catalog.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog")
]
 
spark_conf = SparkConf().setAll(conf_list)
spark = SparkSession.builder.config(conf=spark_conf).enableHiveSupport().getOrCreate()
glue_context = GlueContext(spark.sparkContext)
job = Job(glue_context)
job.init(args['JOB_NAME'], args)

# read the csv file in dynamicframe obj.
csv_file_s3_url = "s3://" +  bucket_origin + "/" + object_bucket_origin

print(csv_file_s3_url)

df = spark.read.format("csv").option("delimiter", ";").option("header", "true").load(csv_file_s3_url)

# create tem tamble with data from csv file inside spark
df.registerTempTable("csv_data_orders")

# write a iceberg table in glue catalog using csv file
sql_stmnt = f"""
CREATE OR REPLACE TABLE iceberg_catalog.db_poc_case_fourth.csv_to_iceberg_emr_serverless
USING iceberg
TBLPROPERTIES ('table_type'='ICEBERG', 'format-version'='2', 'format'='parquet')
LOCATION 's3://s3-storage-layer/emr_serverless/data/db_poc_case_fourth/csv_to_iceberg_emr_serverless'
AS SELECT * FROM csv_data_orders
"""
spark.sql(sql_stmnt).show()

job.commit()

