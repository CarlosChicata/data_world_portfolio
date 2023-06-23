import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.conf import SparkConf
from awsglue.context import GlueContext
from pyspark.sql import SparkSession


# get passed params from aws glue job
args = getResolvedOptions(
    sys.argv, 
    ['bucket_origin', "object_bucket_origin"]
)

# check
bucket_origin = args["bucket_origin"]
object_bucket_origin = args["object_bucket_origin"]

print(bucket_origin, object_bucket_origin, sep="\n")

# setup the spark session in my aws glue job
conf = SparkConf()\
    .set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")\
    .set("spark.sql.catalog.glue_catalog", "org.apache.iceberg.spark.SparkCatalog")\
    .set("spark.sql.catalog.glue_catalog.warehouse", "s3://s3-storage-layer/athena/")\
    .set("spark.sql.catalog.glue_catalog.catalog-impl","org.apache.iceberg.aws.glue.GlueCatalog")\
    .set("spark.sql.catalog.glue_catalog.io-impl","org.apache.iceberg.aws.s3.S3FileIO")
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# read the csv file in dynamicframe obj.
csv_file_s3_url = "s3://" +  bucket_origin + "/" + object_bucket_origin

print(csv_file_s3_url)

dynamicFrame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [csv_file_s3_url]},
    format="csv",
    format_options={
        "withHeader": True,
    }
)

dataFrame = dynamicFrame.toDF()

# write a iceberg table in glue catalog using csv file

dataFrame.createOrReplaceTempView("tmp_csv_to_iceberg_order_glue")

query = f"""
    CREATE TABLE glue_catalog.db-poc-case-4.csv_to_iceberg_order_glue
    USING iceberg
    AS SELECT * FROM tmp_csv_to_iceberg_order_glue;
"""

spark.sql(query)
