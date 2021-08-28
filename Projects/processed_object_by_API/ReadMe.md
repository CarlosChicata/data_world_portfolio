# Processed Object By API
## Purpose
Create an API to get richest data from image-type raw data stored in S3. The answer can be in json format.

## Context
We are service providers and it leads us to store images with text from our clients in addition to some information about it that is in a database.

We have reached an agreement with a client on the use of this information that we have richer. To comply, we will create an API service that extracts the text from the image and indicates the detailed information of the image and its creation. 

## Tools and developer enviroment
We use AWS cloud to create this service. I will use followed service.
* Rekognition.
* S3: Standard.
* API Gateway: HTTP API.
* DynamoDB.
* Lambda function.

The programming languaje to use to implement is python 3.8. Boto3 1.17.39 is a AWS SDK to connect with AWS Service.

## Diagrams
![diagram of project](https://github.com/CarlosChicata/data_engineering_portfolio/blob/main/processed_object_by_API/proccess-object-by-api.png)

## What services does money represent?

* lambdas x2: 
  * Accumulate computing time per request in month.
  * Number of request to process in month.
* Rekognition: 
  * analyze of each image per month.
* S3: 
  *  Number Get request to object.
  *  Capacity of stored data in bucket.
  *  Capacity of data will return to caller using S3 object lambda .
* API Gateway:
  * Number of call to API HTTP.
* DynamoDB:
  * Capacity per GB in month.
  * Number of write operation.
  * Number of read operation.

## Learned lesson
Those are:

1) The rekognition services to detect text in image is available in specified regions. i need to move Canada region (ca-central-1) to north of virgin region (us-east-1) to use. I need to check what region has available services.
2) Define policy in S3 to get public access to everyone.
3) Get approximate the cost of usage all service by AWS.

## Version
Current versión is 0.1.0

## Ideas to optimize
* Connect API Gateway with HTTP via GET request URL to trigger s3 object lambda function. i need to remove a extra lambda to wrapper s3 object lambda.
