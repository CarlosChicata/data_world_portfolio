CREATE TABLE csv_to_iceberg (
    id bigint,
    name string,
    year int,
    category string
)
PARTITIONED BY (year)
LOCATION 's3://s3-storage-layer/athena/'
TBLPROPERTIES (
    'table_type'='ICEBERG',
    'format'='parquet',
    'write_target_data_file_size_bytes'='536870912'
)