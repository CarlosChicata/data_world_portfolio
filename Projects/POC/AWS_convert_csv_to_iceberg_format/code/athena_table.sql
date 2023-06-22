CREATE TABLE csv_to_iceberg_order_athena (
    id bigint,
    code string,
    enterprise_id int,
    size string,
    creation timestamp,
    pick_address string
)
PARTITIONED BY (enterprise_id)
LOCATION 's3://s3-storage-layer/athena/'
TBLPROPERTIES (
    'table_type'='ICEBERG',
    'format'='parquet',
    'write_target_data_file_size_bytes'='536870912'
)