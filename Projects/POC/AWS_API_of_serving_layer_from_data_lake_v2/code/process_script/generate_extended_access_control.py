import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkConf, SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(
    sys.argv,
    ['JOB_NAME']
)


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

