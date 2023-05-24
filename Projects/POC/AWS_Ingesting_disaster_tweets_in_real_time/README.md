# Case 3: Ingesting disaster tweets in real time

## Purpose and warning
The purpose this POC is to get several tweets about real disaster in real time, classify it and store in data warehouse system to analysis from data team.

My acceptance criterias are:

* Classify the tweet: kind of disaster.
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
3. Classify the tweets in kind of disaster.

## Solution

### General Idea

I receive and buffer all JSON data in AWS kinesis firehose, then transform it (mean classify and format all records to be ready consume), then store it in AWS S3 and redshift.

![Diagram of architecture of POC case 3](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/diagram_architecture_poc_case_3.drawio.png)

### How will you prepare my classifier?

Well, i applied a cleaning processing to understand how the dataset work, clean it and generate a approx. label based on own ideas. I did't focus on a depth-in cleaning processing on dataset ( this is a POC ); but i effort to get more cleaning data i can.

If you want to know how i clean it; check `Assign better label to dataset.ipynb` file in process_script folder: this a notebook in jupyter you can execute 😄.

In This script will you know:

1.  How i select fields in faked dataset to preparing label.
2.  How generate the label of kind of disaster.
3.  How i split the original dataset into training and testing dataset for classifier process.


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

First; create a lambda function with process of transformation to classify and format all chunk of data to be ready to consume in data warehouse service. The code will be stay in `transform_firehose_lambda.py` in **process_script** folder. Remember setup the `ENDPOINT_CLASSIFIER` variable to use the custom classifier from endpoint in AWS comprehend.

![Create a transform lambda](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/create_transform_lambda.png)

Second, Run `Assign better label to dataset.ipynb` script to generate all train and test data set models to train the classifier and use to send in the emulator of twitter ingester.

![Creat dataset models](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/create_dataset_classifier.png)

Third; Create a custom classifier with AWS Comprehend; go to the service, click in "custom classifier", click in "create new model", and assign the name of classifier and select the language of dataset.

![Classifier name](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/create_clasifier_part1.png)

Fourth; to continue in creating of classifier, select the mode of classifier; you need the single-label mode; and select the dataset model that you will use to train your classifier. Rememeber the dataset model need to be located in S3.

![Preparing data](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/create_clasifier_part2.png)

Fifth;  to finish in creating of classifier, select the S3 bucket to store the confusion matrix to understand the classifier and specify new IAM role for classfier to access S3 resource; then click in "create".

![FInish classifier](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/create_clasifier_part3.png)

Sixth; create a AWS kinesis firehose service to buffer and call the transformation process; for this POC, i will choose "the Direct PUT" option in source and "Amazon Redshift" in destination.

![part 1 in setup kinesis firehose](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/setup_redshift_part3.png)

Seventh; to continue with the creation of AWS kinesis firehose, click in "enable of data transformation" option in the "data transformation" section; link with created lambda in first step and set up of variables of process to generate the bulk of data will process in the lambda and latency of operation. Read more about it in this [link](https://catalog.us-east-1.prod.workshops.aws/workshops/c342c6d1-2baf-4827-ba42-52ef9eb173f6/en-US/beam-on-kda/create-infrastructure/firehose/configure-settings).

![enable transformation opcion](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/setup_firehose_part2.png)

Eighth; to continue with the creation of AWS kinesis firehose; set up the access of redshift: user credentials, cluster, database and table will store classifier tweets.

![setup redshift](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/setup_kinesis_redshift_part_1.png)

Ninth; to end with creation of AWS kinesis firehose, you need to setup the intermedie S3 destination: select the S3 bucket will store and way to handle the records in redshift. If you wanna learn about how way read records in redshift, use [this](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-copy-from-json.html).

![redshift setup kinesis](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/create_setup_redshift_part2.png)

; then you turn on the enviroment of project, go to "process_scripts" folder and execute `python firehose_real_time_sender.py`. This script will emulate the data producer; Remember setup this script with name of firehose service and other credencials to work.

![Send faked data from sender generator](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_Ingesting_disaster_tweets_in_real_time/images/sender_json_data.png)

### Topic issues


#### Scalability: 🌟🌟🌟🌟🌟


#### Performance: 🌟🌟⭐⭐⭐


#### Reusability:  🌟🌟🌟⭐⭐

#### Security: 🌟🌟🌟🌟⭐

#### Security: 🌟⭐⭐⭐⭐

