import sys

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.functions import *


bucket_origin = sys.argv[1]
object_bucket_origin = sys.argv[2]

# setup session in spark
spark = SparkSession\
            .builder.appName("create-table-orders-table-from-emr-serverless")\
            .enableHiveSupport()\
            .getOrCreate()

catalog_name = "glue_iceberg_catalog_demo"
schema_name = "db_poc_case_fourth"
table_name = "csv_to_iceberg_order_emr_serverless"

spark.sql("use " + catalog_name).show()
spark.sql("""show current namespace""").show()


# read the csv file in dynamicframe obj.
csv_file_s3_url = "s3://" +  bucket_origin + "/" + object_bucket_origin

print(csv_file_s3_url)

df = spark.read.format("csv").option("delimiter", ";").option("header", "true").load(csv_file_s3_url)

# create tem tamble with data from csv file inside spark
df.registerTempTable("csv_data_orders")

# write a iceberg table in glue catalog using csv file
sql_stmnt = """
CREATE OR REPLACE TABLE {}.{}.{}
USING iceberg
TBLPROPERTIES ('table_type'='ICEBERG', 'format-version'='2', 'format'='parquet')
LOCATION 's3://s3-storage-layer/emr_serverless/data/db_poc_case_fourth/csv_to_iceberg_emr_serverless'
AS SELECT * FROM csv_data_orders
""".format(catalog_name,schema_name, table_name)
spark.sql(sql_stmnt).show()


