# Case 4: How convert csv to iceberg format in file 

## Purpose and warning

When i was learning to build the [POC case # 1](https://github.com/CarlosChicata/data_world_portfolio/tree/master/Projects/POC/AWS_API_of_serving_layer_from_data_lake); i learned that i can use iceberg format to support `DELETE`, `UPDATE` and `INSERT` commands in SQL directly; check [it](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-updating-iceberg-table-data.html) if you wanna know more.
So the question is: __*how can convert data from csv format to iceberg format?*__

In This POC; i will search the ways to generate this data conversion; check limitations in transition and others issue about performance of process and queries, needed services and costs.

My acceptance criterias are:

* _List the ways to convert from csv format to iceberg format_ :white_check_mark:
* _Create a matrix to comparing the ways of data conversion_ :white_check_mark:
* _Indicate the limitations and benefits for each ways of data conversion_ :white_large_square:
* _Diagram of arquitecture for all each ways of data conversion_ :white_check_mark:
* _Indicate the important of iceberg format_ :white_large_square:

## Note about the problem context

We need to convert sent data from app is in csv format into iceberg format to use in data lake. Even though the csv format is a file format and the iceberg format is a table format; check this [post](https://shahrajesh2006.medium.com/data-lakes-understanding-file-format-and-table-formats-38d7999c0ec2 ) to understand the difference both; i need to use a file format inside table format to manage the data; so i choose parquet as a main file format; based in this format is best in analytics operations;  and avro as a secondary file format; based in this is best in write operation.

I will use AWS Athena to use the data lake by the data consumer services.

## Challenges

## Solution

There are some way to convert data in CSV format to iceberg format.

### Athena

The strategy is create a new table in iceberg format natively by AWS Athena and insert all data in batch mode from csv dataset by AWS Athena. The data producer got all data will be stored in data lake.

![Athena Architecture infra](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/athena_infra_poc_4.drawio.png)

### Glue

The strategy is create a glue job in spark batch mode by AWS Glue Job to create a table in Athena from AWS Glue data catalog and move all data from CSV format file into iceberg format. The data file is stored in S3 bucket, and we can change the code to glue job in streaming mode with a few minimum changes. I used SPark and AWS Glue python package in scrip.

![Glue Architecture infra](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/glue_infra_poc_4.drawio.png)

The AWS Glue can work in streaming mode and use the workflow to create more complexity data pipeline if you need; that's great!

### EMR

⚠️ __Note__: in AWS EMR you have two options: serverless or serverfull. For this POC, i chosen the serverless options because i don't worry about configuring, managing, and scaling clusters or servers.

The strategy is create a glue job in spark batch mode by AWS Glue Job to create a table in Athena from AWS Glue data catalog and move all data from CSV format file into iceberg format in S3 Bucket. I just can use Spark library in script. The infrastructure is same with Glue way because botn use spark to implement the solutions.

![EMR serverless infra diagram](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/emr-serverless_infra.png)

## How to prepare this project?

⚠️ I did this part; but if you wanna know how i generate this tables and you wanna generate these in new format, Read this part.

I have in data folder, one file with faked data i generated based in my experience. Although I used some fields, there are fields that I don't use; if you wanna experiment with this, do it! 😄

### How to set up this project?

#### By video
Soon i will upload the videos in spanish and english.

#### By step-by-step Documentation

##### Common part

First, You need to create you will use in this POC. Go to cloudformation, create a Stack using the template and pass `infraestructure_cloudformation.yaml` file to create all resource.

![Create resource](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/create_resource_poc_4.png)

Second;  create 5 folder to store all script and organize your data in S3: script (store all scripts to execute), emr-serverless(for emr way), glue (use for glue way ), athena (use for athena way) and raw-csv-file (store faked csv data)

![Create folder S3](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/create_folder_in_s3.png)

##### Glue way

Third; In this case, i will execute the `CSVToIcebergTransformer` glue job to create a table and insert data from CSV file.

![Execute glue job](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/glue_insert_data.png)

Fourth; Go the AWS Athena and exeute `SELECT * from csv_to_iceberg_glue;` query in `db_poc_case_fourth` database in glue data catalog to verify if all data is store.

![Check data in glue](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/check_data_glue.png)

##### Athena way

Third; you need to turn on the script to emulate.

![Insert data in athena](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/sendin_data_athena_poc.png)

Fourth; Go the AWS Athena and exeute `SELECT * from csv_to_iceberg_order_athena;` query in `db_poc_case_fourth` database in glue data catalog to verify if all data is store.

![Check data in Athena](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/insert_data_athena_poc.png)

##### EMR serverless way

Third; in this case, check the IAM role will use the EMR have glue data catalog and S3 permission to use these objects. Check [this doc](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html#gs-prerequisites) to know the needed permissions.

Fourth; go to EMR, click in "serverless" button and click in " Create and launch Studio" button.

![star EMR studio](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/EMR_serverless_start.png)

Fifth; setup the hardware you will use in your EMR. select the spark option, the 6.11 version and give the name of application. Let's leave the other configurations by default and click the create button.

![setup hardware](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/emr_serverless-setup_part1.png)

Sixth; after the application is "created" status, select the created application and click "start application" to use the application.

Seventh; after the application is "starting" status, click in "submit job" button and setup the job name, role to access AWS resources, location of spark script in S3 and params will be used in spark script.

![dada](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/emr_serverless_setup_job_part1.png)

Eighth; in setting job, set up all spark configuration to use Glue in spark script. Use [This doc](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-iceberg.html) to know what params you will need.

![setup service](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/emr_serverless_setup_job_part2.png)

Tenth; click in "submit" button to create and execute the job. After few a minutes, i will get a sucess status from your job.

![sucess job in ERM serverless](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/emr_serverless_setup_job_part3.png)

Eleventh; Go to the AWS Athena and check if the csv_to_iceberg_order_emr_serverless table exist.

![](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_convert_csv_to_iceberg_format/images/emr_serverless_success_job.png)

## Topic issues

| Category | Glue | Athena | EMR Serverless |
|----------|------|--------|-----|
| Processing mode | Apply: you can use programatic enviroment to develop ETL pipeline. only for spark and aws glue library | Not apply: you just can use SQL commands. | Apply: you can use programatic enviroment to develop ETL pipeline. only for spark library. |
| Kind of hardware to use | Based in predetermined options | Depend of service (EC2, function o fargate) to use. AWS Athena is serverless. | Have default option and custom option. You need to create a image of compute to use the custom option. |
| Versión of iceberg can use | release 1.0.0 in version 4 of glue; depend of  version of glue. | Use only version 2 of iceberge table. Don't say nothing about release version of apache iceberg. | Version of iceberg 1.2.0-amzn-0 |
| what kind of managed service is? | Serverless | Serverless | Serverless |
| file format support | parquet, AVRO, or ORC | Parquet, ORC (only v3) and AVRO (only v3) | Parquet, ORC, Avro |
| analytics engine | Spark | Spark | Spark, Trino, PrestoDB, Flink, Hive |
