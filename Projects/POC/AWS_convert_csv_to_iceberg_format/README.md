# Case 4: How convert csv to iceberg format in file 

## Purpose and warning

When i was learning to build the [POC case # 1](https://github.com/CarlosChicata/data_world_portfolio/tree/master/Projects/POC/AWS_API_of_serving_layer_from_data_lake); i learned that i can use iceberg format to support `DELETE`, `UPDATE` and `INSERT` commands in SQL directly; check [it](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-updating-iceberg-table-data.html) if you wanna know more.
So the question is: __*how can convert data from csv format to iceberg format?*__

In This POC; i will search the ways to generate this data conversion; check limitations in transition and others issue about performance of process and queries, needed services and costs.

My acceptance criterias are:

* _List the ways to convert from csv format to iceberg format_ :white_large_square:
* _Create a matrix to comparing the ways of data conversion_ :white_large_square:
* _Indicate the limitations and benefits for each ways of data conversion_ :white_large_square:
* _Diagram of arquitecture for all each ways of data conversion_ :white_large_square:
* _Indicate the important of iceberg format_ :white_large_square:

## Note about the problem context


## Challenges


## Solution

There are some way to convert data in CSV format to iceberg format.

### Athena

The strategy is create a new table in iceberg format and insert all data in batch mode from csv dataset by AWS Athena. 


### General Idea


### Tools to implement


### Project Structure

### How to prepare this project?


### How to set up this project?

#### By video


#### By step-by-step Documentation 


### How destroy the POC project? (By step-by-step Documentation )

### Topic issues


#### Scalability: :star2::star2::star2::star2::star2:



#### Performance: :star2::star2::star::star::star:

#### Reusability: :star2::star2::star2::star::star:


#### Security :star2::star2::star::star::star:

