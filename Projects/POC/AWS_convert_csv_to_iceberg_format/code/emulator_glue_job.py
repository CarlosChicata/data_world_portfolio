import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession


# get passed params from aws glue job
args = getResolvedOptions(
    sys.argv, 
    ['bucket_origin', "bucket_destiny", "object_bucket_origin", "object_bucket_destiny"]
)

# check
bucket_origin = args["bucket_origin"]
bucket_destiny = args["bucket_destiny"]
object_bucket_origin = args["object_bucket_origin"]
object_bucket_destiny = args["object_bucket_destiny"]

print(bucket_origin, bucket_destiny, object_bucket_origin, object_bucket_destiny, sep="\n")

# setup the spark session in my aws glue job
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

# write the parquet file from dynamicframe obj.
parquet_file_s3_url = "s3://" +  bucket_destiny + "/" + object_bucket_destiny

glueContext.write_dynamic_frame.from_options(
    frame=dynamicFrame,
    connection_type="s3",
    format="parquet",
    connection_options={
        "path": parquet_file_s3_url,
    }
)


