# Case 5: Data modeling in operational area: inmon analytical logical design

## Purpose and warning

In case 1 to 4; I understood how mandalo will work in process in all level data model. But the startups has some BI and data analytics that they need to work to improve processes and operations; si i need to create a data model to operate this type of workflow and don't affect the operational model.

In this case the artifact will be a logical data modeling; but a thinking i will implement in analytical focus.

## Why will i do?

There are any difference in operational and analytical data model. The operational data model support update and insert operations in high amount, need to be process so fast so possible then the operations need to be minimum amount, not too complexity processing aggregation queries, not too integrated and few data use. Analytical data model support read in high amount and insert in middle amount but last one dependent in type of consume from user; process complex aggregation queries; too integrated and/or return high amount of data.

So then, i need to implement a analytical data model focus logical view; **why logical view?** because the logical data model translate the conceptual model and business requirements into structure of specified tables and columns that any DBMS can implement it (The main feature that separate it the physical model); that comply the operational focus. In physical data model; dependently the chosen DB i can implement more details to achieve a performance in operations; but the logical model will give me the amount of operations, complexity of query to support insert and read data operations and indicate how the evolution of corporate data architecture model will be.

In the case of analytical focus; i need to select entities and field that will give value to the users and organizational goals.

## Decision

### Goals and selected entities

The goals of the analytical team are:

* Understand the operations of clients in shipments.
* Understand ours service into clients and drivers.
* Find new opportunities in operations and resource usage to face of client and ours.

For these goals we select only elements based in operations of our clients and ours.

### Data modeling in Inmon

This form of data model is look like a operational data model with some exceptions:

* Remove all operational data and other elements based in this focus.
* Remove all tables that not matter to analytical operations.
* Based in 1-3 normal format techniques to model it.

For this reason, i used this [post](https://medium.com/data-world-portafolio/empezando-con-el-data-warehouse-modelamiento-8d13d3c9bd60) explain shortly how to model this type of structure in database; you need to read more the "building a data warehouse" of inmon to know about it. So then i use this focus and decided following issues:

1. All "primary group" entities are: `warehouse`, `vehicle`, `service`, `shipment`, `route`, `driver`, `city`, `country`, `enterprise`, `request`, `incident`, `Historial event`.
2. All "secondary group" entities are:  `compensation incomplete term`, `Location`, `branch schedule`, `order`, `branch`, `Status event order`, `status event route`.
3. All "Connection" entities: `term of request`, `term of service`, `service of city`, `resource vehicle`, `resource shipment`. In general use foreign key to connect between tables.
4. All "Type of" entities : 
  * "Historial event" are: `historial of driver`, `historial of vehicle`. 
  * "Service" are: `Order based service`, `driver based service`, `resource based service`
  * "Historial of warehouse in moving resource" are: `resource vehicle`, `resource shipment`   
6. i'm trying to apply the 1-3 NF to normalize the structure of data. If it's error: don't kill me, i'm learning because it hard to get a references to implement based in this form.

## Diagram

![Diagram of logical data model in analytical focus](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/inmon_logical_data_design_in_operational_area/Analytical%20logical%20data%20model%20-mandalo.png)

### Note

_*_: This field is used like other table like type.
