# Case 6: Data modeling in operational area: Inmon analytical physical design

## Purpose and warning

In case 5; I created a logical data model with analytical focus to support analytical queries to BI/data analytisc. Now i need to add performance features to improve the performance this data model. In this case the artifact will be a physical data modeling.

## Why will i do?

There are any difference in operational and analytical data model. The operational data model support update and insert operations in high amount, need to be process so fast so possible then the operations need to be minimum amount, not too complexity processing aggregation queries, not too integrated and few data use. Analytical data model support read in high amount and insert in middle amount but last one dependent in type of consume from user; process complex aggregation queries; too integrated and/or return high amount of data.

So then, i need to implement a analytical data model focus physical view; **why physical view?** because the logical data model translate the conceptual model and business requirements into structure of specified tables and columns that any DBMS can implement it (The main feature that separate it the physical model); that comply the operational focus. In physical data model; dependently the chosen DB i can implement more details to achieve a performance in operations.

## Decisions

These are decision to applied.

1. All primary groups and/or some secondary groups will get some special fields to management the validity of register face the change of value:
  * Start lifecycle time: this datetime in the register with its fields start to use in the operational data model.
  * End lifecycle time:  this datetime in the register with its fields start to use in the operational data model.
  * Is delete: this register is soft delete from analytical system. The reason is that register is not apply.
  * ID internal: ID register in analytical data system.
  * ID register: ID register in operational data system.
2. I added "location" table to manage the change of location in shipments, to respect the spirit of the 3NF.
3. I don't add field from original table to related table to improve the performance, to respect the 2NF rule.
4. I remove "ZIP postal codes" field in "City", and replace it with "City Postal" table, to respect the 1NF rule. 
5. I remove "Applied cities" field in "Service", and replace it with "City in service" table, to respect the 1NF rule. 
6. I remove "Branch Schedule list" field in "Branch" and replace it with "Branch schedule" table, to respect the 1NF rule.
7. Some table will get a B-tree index with clustered method to improve the performance of reading operation.

## Diagram

![Diagram](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/inmon_physical_data_design_in_operational_area/Analytical%20physical%20data%20model%20-mandalo.png)

### Note

_*_ : this field is based in table in this diagram.
