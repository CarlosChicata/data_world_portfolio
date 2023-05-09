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


### Topic issues


#### Scalability: 🌟🌟🌟🌟🌟


#### Performance: 🌟🌟⭐⭐⭐


#### Reusability:  🌟🌟🌟⭐⭐

#### Security: 🌟🌟🌟🌟⭐



