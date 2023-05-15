# Case 3: Ingesting disaster tweets in real time

## Purpose and warning
The purpose this POC is to get several tweets about real disaster in real time, classify it and store in data warehouse system to analysis from data team; but you need to be cared because  some tweets are joke.

My acceptance criterias are:

* Classify the tweet: like disaster or joke; and kind of disaster.
* Processing in (near) real time the tweets.
* Store all tweets in data warehouse to consume.
* Create a data model to support the storage.


## Note about the problem context

This is a interesting problem because i need to classify a tweets about the disaster; but i have several points to resolve:

1. I need to assign label to train my classifier. I have a dirty dataset and i need to clean it first.
2. I need to learn how insert a bunk of data to data warehouse system service (AWS redshift) without negatively impact its performance.
3. I need to link the tweets file stored in S3 with record in data warehouse system service for each tweets processed.

This is a diagram of the  data modeling will support the operation in data warehouse system service. as i'm processing texts, i think i need to apply some points from the unstructure data warehouse from [this post i wrote](https://medium.com/data-world-portafolio/empezando-con-el-data-warehouse-datos-no-estructurados-1b4c42236cf3) in the data modelling diagram.

## Challenges

These are the main challenges to face:

1. Link the tweets file stored in S3 with record in data warehouse system service for each tweets processed.
2. How insert a bunk of data to data warehouse system service (AWS redshift) without negatively impact its performance.
3. Classify the tweets in kind of disaster and its whether joke or not.

## Solution

### General Idea

I receive and buffer all JSON data in AWS kinesis firehose, then transform it (mean classify and format all records to be ready consume), then store it in AWS S3 and redshift.

![Diagram of architecture of POC case 3](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/diagram_architecture_poc_case_3.drawio.png)

### Tools to implement

1. Python 3.9
2. AWS Redshift
3. AWS Kinesis Firehose
4. AWS S3
5. AWS Lambda
6. AWS Comprehend

### Project Structure


### How to set up this project?

#### By video
Soon i will upload the videos in spanish and english.

#### By step-by-step Documentation

First; create a lambda function with process of transformation to classify and format all chunk of data to be ready to consume in data warehouse service.

Second; create a AWS kinesis firehose service to buffer and call the transformation process; for this POC, i will choose "the Direct PUT" option in source and "Amazon S3" in destination.

![basic setup firehose ](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/setup_firehose_part1.png)

Third; to continue with the creation of AWS kinesis firehose, click in "enable of data transformation" option in the "data transformation" section; link with created lambda in first step and set up of variables of process to generate the bulk of data will process in the lambda and latency of operation. Read more about it in this [link](https://catalog.us-east-1.prod.workshops.aws/workshops/c342c6d1-2baf-4827-ba42-52ef9eb173f6/en-US/beam-on-kda/create-infrastructure/firehose/configure-settings).

![enable transformation opcion](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/setup_firehose_part2.png)

Fourth; to  end with the creation of AWS kinesis firehose, link with the AWS S3 will store all  prepared data from lambda in the AWS Kinesis firehose; then click in "create" and wait because it will take a few minutes to complete.

![link the destination point](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/setup_firehose_part3.png)

Fifth; then you turn on the enviroment of project, go to "process_scripts" folder and execute `python firehose_real_time_sender.py`. This script will emulate the data producer; Remember setup this script with name of firehose service and other credencials to work.

![Send faked data from sender generator](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/sender_json_data.png)

### Topic issues


#### Scalability: 🌟🌟🌟🌟🌟


#### Performance: 🌟🌟⭐⭐⭐


#### Reusability:  🌟🌟🌟⭐⭐

#### Security: 🌟🌟🌟🌟⭐



