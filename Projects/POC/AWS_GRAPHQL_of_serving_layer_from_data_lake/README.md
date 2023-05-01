# Case 2: GraphQL API of serving layer stored from data lake in AWS

## Purpose and warning

I have a data model ready to be consumed for several software components in our internal service system. This model is stored in data lake by data architect decision. So that you have to expose a data schema that users of other services in the system, need to consume it based on their own requirements to work; so then i wanna implement a API to give access this users.

My acceptance criterias are:

* _Management of access of data in data schema based in authorization permissions._ :boom: __Note__ : Because the complexity to solve in this POC, i will it in version 2.
* _Get a GraphQL API with data source based in data lake._ :heavy_check_mark:
* _Management a validation credentials to autenticate the usage of data schema._ :heavy_check_mark:
* _Create a process to optimize number of query need to structure the wanted data._ :heavy_check_mark:
* _Available reading on demand and real time notification methods as a services to other components on your service system._ 🤔: __Note__ : Because the complexity to solve the real time service in this POC, i will it in version 2.

__If you want to expose the generated data from your service in serverless architecture, that it will be consumed for internal services neighborhood based in their own data requirements and requirements are different each others. I think this POC is for your.__.

## Note about the problem context

There are some point you need to know to understand better the problem:

First, this is the data model to extract data. This is a data modeling based in normalization view of tables. The theme of the serving data layer is about logistic delivery of product. **Note**: don't focus in design of data model, i don't focus to be correct design to check if the model effects someway the POC case.

![Data model](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_API_of_serving_layer_from_data_lake/code/image/POC%20serving%20layer%20-%20data%20model.png)

Second, you can modify or add new content in the tables of your data lake, so you give subscription service to support real time process in your component. Also you need to support retrievel operation on demand too. __The main object is to get give data as fast as possible to other component based in their data and performance requierements.__

## Challenges

These are the main challenges to face:

* _We need to support query and subscription operations in your graphQL api_. 🤔 __Note:__ i implemented a query service based in range but the real time service wasn't implemented by complexity to solve it; so in the version 2 of this POC i will solve it.
* _We need to connect data lake in S3 with Athena as a data source._ :heavy_check_mark:
* _We need to reduce the number of independent query to table get structure the wanted data._ :heavy_check_mark:
* _We need to  support management of select authorized fields in data schema based in role._ :boom: __Note:__ For this POC i've chosen don't implement this part by complexity to solve. In version 2 this POC i will it.
* _We need to use a authenticate method will use the data schema._ 🤔 __Note:__ AWS Appsync create authentication methods ( API Key) by default; but i think i can create a custom authentication method to get a fine-granular control and implement more interesting things. So in the version 2 of this POC i will solve it.

## Solution

### General Idea

I receive all graphql request with needing fields, turn it to SQL query to execute on athena; the response will structure based in graphql request in JSON format and return it to API.

![Architecture solution of POC](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_GRAPHQL_of_serving_layer_from_data_lake/code/images/appsync%2Bdatalake.drawio.png)

### Conversion GraphQL request - SQL query - Graphql response

I think i front two main challenges:

1. I need to select several tables in one data source to get the data.
2. I need to select specific fields to be available in the response.

So these challenges will solve when i can manage the query in its making. I thought the solution: to format the graphql request fields to build a object of field management; then it translated to SQL query; with the help of a mapping of table relationships for data source; and execute in AWS Athena, i got the file with data, and it pass to response generator to structure the data with graphql response; with the help of structure mapper; to send the list of requested data.

![Main idea to manage the graphQL request with several tables](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_GRAPHQL_of_serving_layer_from_data_lake/code/images/gql-sql-gql%20(1).png)

I can use it as a data source in appsync or convert it a lambda layer to resusable code. 😄

### Tools to implement

1. AWS Athena
2. Python 3.9
3. AWS S3 standard
4. AWS AppSync
5. AWS Lambda function and layers.
6. AWS Glue: Database

### Project Structure

In the __Code__ folder contains all files associated this POC. This folder is structured following topics:

* __fake data__ folder contains faked data to test your process of generated data file from AWS Athena.
* __process_scripts__ folder contains all scripts need to use in the lambda as data sources.
* __variables__ contains the mapper of tables relationships of the database hosted in AWS Athena. :boom: __NOTE:__ This file isn't used in this POC. It's include in code.
* __schema.graphql__ file contain all types and queries will i do in the Graphql API. :boom: __NOTE:__ This file isn't used in all, some parts are used in this POC. 
* __reference.txt__ file contain all reference studied to implement this POC.
* __infraestructure_cloudformation.yaml__ file contain all IaC resource i will need to implement the POC. :boom: __NOTE:__ This file isn't used in this POC.

### How to set up this project?

#### By video
Soon i will upload the videos in spanish and english.

#### By step-by-step Documentation

Zero, i used all tables i generated in the POC case 1; so i won't repeat the process twice or more times. The steps are second, fourth and fifth in the list of setup environment of POC case 1 that you can check it.

First; go the Appsync and click in "from the scratch", then introduce the name of the graphql API and click in "create".

Second, create a lambda function with code of the __main.py__ script. This lambda is built python 3.9, add it pandas layers to work, set up ATHENA_S3_OUTPUT ( S3 URL of the bucket) and ATHENA_S3_BUCKET_OUTPUT (Name of bucket) variables to store the file. For this POC it named _data-source-athena_.

The NAME_CLIENT is the name of main table ( first table in data schema) of the query; and MAPPER_RELATIONSHIPS is the mapper of table relationships in the AWS Athena. Remember get access the fields of graphql request; maybe it change the way how it pass in lambda.

Third; return into api in appsync, go the "schema" section and add the following data schema __Remember__: This is a part of completed data schema in schema.graphql. Then to click in "Save".

```
type City {
	timezone: String!
	name: String!
	country_id: Country!
	id: Int!
}

type Client {
	comercial_name: String
	business_name: String
	city_id: City!
	id: Int!
	address: String
	serviceids: Int
	enterpris_key: String!
}

type Country {
	id: Int!
	name: String!
	region: String!
	prefixphone: Int!
	currencyiso: String!
}

type Query {
	getClient: [Client]
}

schema {
	query: Query
}
```

Fourth; go the "data source" section, clicj in "create a data source", add a name ; i named athena_data_source like a lambda; and select type of data source, click in "lambda", select the region and lambda will use, and click "save".

Fifth; go the "queries" section, structure the query you want and execute it; soon you will get all data based in the graphql request. Congrats 🎉✨


### Topic issues

I needed to learn in my few free time some topics about AWS resource  Appsync; so i built based on simplicity and functional vision such that i got a POC in version 1 with minimum functionality to the main goal: generate the more efficient and flexible query to run in AWS Athena.

#### Scalability: 🌟🌟🌟🌟🌟

👍 Because the architecture is serverless focus in general; the resources can created based in demand required in all kind of enviroment to solve all user requests. Any change in data or code can be apply in scale in this infrastructure model.

#### Performance: 🌟🌟⭐⭐⭐

👍 The query is generated with only needed fields and tables required to work; so then you only need to use one query to get all data required in one database.

👀 The performance of tables in AWS Athena depend how you structure the tables, so then i can improve these. I will read this [post](https://aws.amazon.com/es/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/) to i know how to do.

This focus only apply for query to get all data, but it need to get params and paginations process to improve the query services; and i need to add real time process in this API to delivery data in this option.

#### Reusability:  🌟🌟🌟⭐⭐

👍 I can use a only code; it just a bit long code; to generate the differents kind of queries for one database based in graphql request. This code can be either data source or layer lambda; so you can use with many SQL database engine with one code!.

👀 i need to parameter some variables to completely abstract the code to one file; so then i process it like a function and get use the AWS lambda as container for customer parameters that process needs.

#### Security: 🌟🌟🌟🌟⭐

👍 The default authentication and authorization method; API Key; can work for this demo.

👀 If i can send data of request based in required __AND__ authorized fields, i think it will be a great functionality in the POC to control the access of data schema. I think to achieve this functionality i need to implement a custom authorization and authentication process for appsync.


