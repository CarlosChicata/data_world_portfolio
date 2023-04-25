# Case 2: GraphQL API of serving layer stored from data lake in AWS

## Purpose and warning

I have a data model ready to be consumed for several software components in our internal service system. This model is stored in data lake by data architect decision. So that you have to expose a data schema that users of other services in the system, need to consume it based on their own requirements to work; so then i wanna implement a API to give access this users.

My acceptance criterias are:

* Management of access of data in data schema based in authorization permimssions.
* Get a GraphQL API with data source based in data lake.
* Management a validation credentials to autenticate the usage of data schema.
* Create a process to optimize number of query need to structure the wanted data.
* Available reading on demand and real time notification methods as a services to other components on your service system.

## Note about the problem context

There are some point you need to know to understand better the problem:

First, this is the data model to extract data. This is a data modeling based in normalization view of tables. The theme of the serving data layer is about logistic delivery of product. **Note**: don't focus in design of data model, i don't focus to be correct design to check if the model effects someway the POC case.

![Data model](https://github.com/CarlosChicata/data_world_portfolio/blob/master/Projects/POC/AWS_API_of_serving_layer_from_data_lake/code/image/POC%20serving%20layer%20-%20data%20model.png)

Second, you can modify or add new content in the tables of your data lake, so you give subscription service to support real time process in your component. Also you need to support retrievel operation on demand too. __The main object is to get give data as fast as possible to other component based in their data and performance requierements.__

## Challenges

These are the main challenges to face:

* We need to support query and subscription operations in your graphQL api.
* We need to connect data lake in S3 with Athena as a data source.
* We need to reduce the number of independent query to table get structure the wanted data.
* We need to to support management of select authorized fields in data schema based in role.
* We need to authenticate used will use the data schema

