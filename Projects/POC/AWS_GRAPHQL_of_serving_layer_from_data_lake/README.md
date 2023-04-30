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

### Tools to implement

1. AWS Athena
2. Python 3.9
3. AWS S3 standard
4. AWS AppSync
5. AWS Lambda function and layers.
6. AWS Glue: Database

