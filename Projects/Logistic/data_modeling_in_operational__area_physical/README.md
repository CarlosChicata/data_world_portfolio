# Case 3: Data modeling in operational area: physical focus to operational activities

## Purpose and warning

In case 1, I understood how mandalo will work in process, generate data and how entities need; and case 2, i added attributes into entities and analyzied the common queries to add new entities to support the operations. So then, in this part i need to extend the data modeling into physical level to be use by database modeler or database administrator.

In this case the artifact will be a Physical data modeling; but a thinking i will implement in operational system and not analytical focus.

## Why will i do?

There are any difference in operational and analytical data model. The operational data model support update and insert operations in high amount, need to be process so fast so possible then the operations need to be minimum amount, not too complexity processing aggregation queries, not too integrated and few data use. Analytical data model support read in high amount and insert in middle amount but last one dependent in type of consume from user; process complex aggregation queries; too integrated and/or return high amount of data.

So then, i need to implement a operational data model focus physical view; __why physical view__? Because the logical data model view is focus in create a structure already to implement in any DBMS: technically this is a template!; but if i need to get performance based in restructure table to new table to get better operations or/and strategy based in location of data inside of physical storage; i need to document a physical data model. The special case is the logical and physical data model they are same, because i don't need to change anything in those models.

## Technical decision to create it 

Based in case 2 of this project that contain all analyzing report of queries, i will take some technical decisions to improve the performance of queries and support some feature: 

1. Flexibility to support new operations from several department by add new tables.
2. Maintain the capacity to migrate all table into another DB to support better the operation when the architect change.
3. Get minimum joins operations between tables. 

This is implemented thinking Postgresql 15.

### Decisions

The decisions i chosen are:

1. All row in any table will apply a soft delete, because if i need to track a old events or legal research about drivers and staff.
2. All row in any table will get a ID to support index and improve performance queries.
3. Some tables are merged into new table; the new table get the name of main table of the group. It's because the minor table in merged table will be queries in lowest level but i need to validate the structure of minor to preserve value and it will use in some queries not frequently. The relationships the merged table maintain is from  the main table. These tables are:
   * Handle shipment register: handle shipment register (main), change shipment (minor).
   * Branch: Branch (main), Branch schedule (minor)
4. There are tables contain common fields and they are same from the  ontology view; so i will separate the common fields into common table and reference it in the specified table to use. These tables are:
   * User: Operational user, driver.
5. The vehicle, driver and warehouse tables is classified like resource entities, and they need to be assigned to general table or two field (type of resource and ID of resource).
6. Add middle tables to support many-to-many relationshion and reusability of table.
   * "Term of service" and "Terms of request" are tables to resuse the "Compensation incomplete term" table.
   * "Resource of request", "Service in city" and "Role in Opt User" tables are middle table in case of many-to-many relationship.
7. Extend some table to improve the reading queries:
   * Add some fields of "shipment" table into "order" table.
   * Add one field of "Driver" table and "Service" table into "Historial of driver" table.
   * Add one field of "branch" table into "Request" table.
   * Add some fields of "Incident" table into "Status event order" table.
   * The "shipment" table was extend using one field from "warehouse", "Branch", "Service" tables.
8. There are some field like enum data type; this is because i need to implement a list of items by the conceptual view they have several values, The list of items are:
   * "Service"."type of service" are `Resource based`, `Order based`.
   * "Service"."applied vehicle to use" and "vehicle"."vehicle type" are `Moto`, `Van`, `Convoy` and `Car`.
   * "Service"."resource" are `Vehicle`, `Driver` and `Warehouse`.
   * "Historial of vehicle"."response", "Historial of driver"."response", "Historial of warehouse in moving shipment"."response", "Historial of warehouse in moving vehicle"."response", "Request"."response" are `Accepted` and `Rejected`.
   * "Historial of warehouse in moving shipment"."type operation" and "Historial of warehouse in moving vehicle"."type operation" are `Get in`,`Get out`
   * "Change shipment"."operation" are `delete`, `update`, `create`.
   * "Handled shipment register"."Status of previous shipment" and "Branch"."Status of changed shipment" are  `Cancelled`, `Validated`, `Start`, `Picked up`, `Picking up`, `Delivering`, `Delivered`, `Failed pick up`, `Failed delivery`, `Returning`, `Returned`, `Crossdocking`, `Finished` and `Crossdocked`.
   * "Vehicle"."who is owner" are `Driver` and `Ours`.
   * "Historial of vehicle"."Status of finish operation", "Vehicle"."Status" are `Repairing`,`Repaired`, `Available`, `Unavailable` and `Using by driver`.
   * "Order"."status", "shipment"."status" are  `Cancelled`, `Validated`, `Start`, `Picked up`, `Picking up`, `Delivering`, `Delivered`, `Failed pick up`, `Failed delivery`, `Returning`, `Returned`, `Crossdocking`, `Finished` and `Crossdocked`.
   * "Route"."Status" are `Created`, `Dispatched`, `Completed`, `Working`, `Cancelled`, `Transfered`, `Accepted` and `Offered`.
   * "Route"."operational incentive" and "Incident"."Discount operator of driver"  are `add`, `multiply`,
   * "Route"."type of work" are `Offered`, `Assigned`.
   * "Status event order"."" are `Cancelled`, `Validated`, `Start`, `Picked up`, `Picking up`, `Delivering`, `Delivered`, `Failed pick up`, `Failed delivery`, `Returning`, `Returned`, `Crossdocking`, `Finished` and `Crossdocked`.
   * "Status event route"."" are `Created`, `Dispatched`, `Completed`, `Working`, `Cancelled`, `Transfered`, `Accepted` and `Offered`.
   * "Incident"."responsibility" are `mandalo`, `end client`, `external event`, `other`, `client`.
   * "Request"."resource type" are `Driver`, `Warehouse` and `Vehicle`.
   * "Resource of request"."type" are  `Driver`, `Warehouse` and `Vehicle`.
   * "Compensation incomplete term"."responsibility" are `Client`, `Ours`.
   * "Role"."score" are `Inside area`, `Cross areas`, `Regional areas`, `Cross regional area`.
   * "Branch schedule"."Day" are `Mon`,`Tues`, `Wed`,`Thu`, `Fri`, `Sun` and `SAT`.
   * "status event route"."created user type", "status event order"."created user type" are `Driver`,`Operational user`. 
9. Add creation field in all table to register the datetime of creation in database.
10. The "Driver" and "Operational user" tables use the same ID field associated to unique row of "User" table.
11. The datetime will be without timezone (utf-8).
12. Next

## Diagram

![Diagram of physical data model](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/data_modeling_in_operational__area_physical/Mandalo%20-%20Physical%20view%20data%20model%20_%20general.png)

### Note

_*_ : This field is built based in focus of field in case of resource from rule #5.

