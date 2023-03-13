# Case 2: Data modeling in operational area: logical focus to operational activities

## Purpose and warning

In case 1; I understood how mandalo will work in process, generate data and how entities need. So then, in this part i need to extend the data modeling; it's in conceptual level; to logical level to give more details to IT and business views.

In this case the artifact will be a logical data modeling; but a thinking i will implement  in operational system and not analytical.

## Why will i do?

There are any difference in operational and analytical data model. The operational data model support update and insert operations in high amount, need to be process so fast so possible then the operations need to be minimum amount, not too complexity processing aggregation queries, not too integrated and few data use. Analytical data model support read in high amount and insert in middle amount but last one dependent in type of consume from user; process complex aggregation queries; too integrated and/or return high amount of data.

So then, i need to implement a operational data model focus logical view; **why logical view?** because the logical data model _translate the conceptual model into structure of specified tables and columns that any DBMS can implement it_ (The main feature that separate it the physical model); that comply the operational focus. In physical data model;  dependently the chosen DB i can implement more details to achieve a performance in operations; but the logical model will give me the amount of operations, complexity of query to support insert and read data operations and indicate how the evolution of corporate data architecture model will be

## Common queries will use

This section is need because i need to know what common queries will be implement to support main process in operation, and understand what this structure.

| N° | Description of query | What will it need | Needed fields to support operation | Related entities |
|----|----------------------|-------------------|------------------------------------|------------------|
| 1 | _Get all orders from the route_ | Check current status orders inside route | Current status of orders, code shipment of orders, name of branch created the shipment, datetime of dispatch of route, code of route, datetime of creation route. | `Shipment`,`Order`, `Route`, `Status event order`, `Status event route`, `Vehicle`, `Driver`, `Branch` |
| 2 | _Get all info of route_ | Check current status of route | All info of route, driver and vehicle associated. More Code and current status of order associated the route. | `Order`, `Route`, `Status event order`, `Status event route`, `Vehicle`, `Driver` |
| 3 | _Get historial of shipment_ | Check historial of events in shipment | All info of shipment ,order and historial events of order. Name of branch of shipment, Type of service, routes associated the orders of shipment.  | `Order`,`Shipment`,`Status event order`,`Route`, `City`, `Branch` |
| 4 | _Get Info of Driver_ | I need to check historial and status of driver | All info of driver and historial of vehicle that he used and change of service. City and country i live. | `Driver`, `Historial of driver`,`Historial of vehicle`, `City`, `Country` |
| 5 | _Get info of Branch_ | Check the entity work with us | All info of branch and enterprise associated. Count of shipment and currents status; type of service and historial of requests and its status. | `Branch`,`Enterprise`,`Country`,`City`,`Shipment`,`Request`,`Status event order` |
| 6 | _Get info of request_ | Check info request of client. | All info of request, Branch send request and resource was requested. | `Request`, `Branch`, `Vehicle`,`Driver`,`Warehouse` |
| 7 | _Get list of request_ | Get a list of request in chunk of 20 elements. It can be filtered based in resource, warehouse associated, datetime of creation and status. | All code of request, status, creation datetime and type of resource. | `Request` |
| 8 | _Get list of shipments_ | Get a list of shipment in chunk of 30 elements. It can be filtered based in branch, enterprise, creation datetime and status. | Code of shipment, branch created a shipment, enterprise of shipment, drop and pickup address, status of shipment. | `Branch`,`Shipment`,`Enterprise` |
| 9 | _Get list Resources_ | Get a list of resources associated to warehouse. return all resource of drivers and vehicle | Show name or plate, status of resource and registration datetime | `Warehouse`, `Vehicle`, `Driver` |
| 10 | _Get vehicle_ | Check all info about the vehicle. | All info of vehicle and historial | `Vehicle`,`City`,`Country`, `Historial of vehicle`, `Driver` |
| 11 | _Get warehouse_ | Check all info about the warehouse. | All info of warehouse. Count of drivers and vehicle. | `Warehouse`,`City`,`Country`, `Drivers`, `Vehicle`|
| 12 | _Get list of internal request_ | Get a list of internal request in chunk of 30 elements. It can be filtered based in shipment and vehicle. | Code of request, warehouse receive the request, City of destination warehouse, creation datetime and status. | `Historial of warehouse in moving vehicle`, `Historial of warehouse in moving shipment`, `City`,`Country`, `Warehouse` |
| 13 | _Get internal request_ | Check internal request that we send | All info of internal request | `Historial of warehouse in moving vehicle`, `Historial of warehouse in moving shipment`, `City`,`Country`,`Shipment`,`Vehicle`,`Operational user` |
| 14 | _Get an operational user_ | Get information of operational user. | All info of opt-user. When he lives and roles. | `Rol`,`City`,`Country`,`Operational user`|
| 15 | _Create a shipment_ | Create a new shipment | All info of shipment. Branch, warehouse associated. | `Shipment`, `City`, `Country`, `Branch`, `Warehouse` |
| 16 | _Register a branch_ | Create a new cliente | All info of branch, associated to enterprise and service contracted. | `Service`, `Branch`, `Enterprise`, `City`, `Country` |
| 17 | _Register an enterprise_ | Create a new enterprise to associate a clients. | All info of enterprise. | `Enterprise` |
| 18 | _Create a route_ | Create a route to deliver a shipment to clients. | All info of route, driver associated, vehicle and order of shipments. | `Order`, `Vehicle`, `Driver`, `Route`, `City`, `Country` |
| 19 | _Register a driver_ | Create a new register of driver in system. | All info of driver. Service he applied and warehouse associated. | `Warehouse`, `Driver`, `City`, `Country`, `Vehicle` |
| 20 | _Register a warehouse_ | Create a new warehouse to operate. | All info of warehouse. City it will locate. | `City`, `Country`, `Warehouse` |
| 21 | _Register a vehicle_ | Create a register of new vehicle associated to warehouse. | All info of vehicle; and warehouse stored it. If apply, the owner of vehicle.  | `Vehicle`, `Warehouse`, `City`, `Country`, `Driver` |
| 22 | _Create an internal request_ | Create a new register of internal request to move shipment of vehicle. | All info of moving of shipment/vehicle, warehouse will store and city of operations. | `City`, `Country`, `Warehouse`, `Shipment`, `Vehicle`, `Historial of warehouse in moving shipment`, `Historial of warehouse in moving vehicle`, |
| 23 | _Update driver_ | Update all personal info of driver | All personal info of driver. | `Driver`,`City`,`Country` |
| 24 | _Change owner of vehicle_ | Change of vehicle assign to vehicle. It can be a driver or ours |  field of owner in vehicle entity. | `Drivers`,`Vehicle` |
| 25 | _Assign resource to warehouse_ | Assign resource(vehicle, driver or shipment) to warehouse | field of resource and ID of warehouse | `Warehouse`, `Shipment`, `Vehicle`, `Driver` |
| 26 | _Update shipment_ | Update all info of shipment. | All info of shipment| `Shipment`, `City`, `Country`, `Branch`, `Warehouse`, `Enterprise` |
| 27 | _Update warehouse_ |Update all info of warehouse. | All info of warehouse| `City`, `Country`, `Warehouse` |
| 28 | _Create status event route_ | Create a new event associated to route. | All info of event in route. | `Route`, `Status event route` |
| 29 | _Create status event order_ | Create a new event associated to order. | All info of event in order. | `Order`, `Status event order` |
| 30 | _Update vehicle_ | Update all info of vehicle | All info of vehicle except owner of vehicle. | `Vehicle` |
| 31 | _Update internal request_ | Update all info of internal request. | All info of internal request, include resources. | `Shipment`, `Vehicle`, `Historial of warehouse in moving vehicle`, `Historial of warehouse in moving shipment`, `Warehouse` |
| 32 | _Update request_ | Update all info of request from client. | All info of request; plus change of resource. | `Request`, `Warehouse`, `Vehicle`, `Driver` |
| 33 | _Update branch_ | Update info of branch. | All info of branch. | `Branch`, `City`, `Country`, `Enterprise` |
| 34 | _Update route_ | Update all info of route. | All info of route, include drivers, vehicles, orders and other issues| `Route`, `Vehicle`, `Orders`, `Drivers` |
| 35 | _Transfer orders to another route_ | Transfer one o more order to another new route; and remove the order of previos route and indicate reason of moving | All info of order. | `Order`, `Route`, `Incidents` |
| 36 | _Delete driver_ | Delete a driver. | Change access of driver register.| `Driver` |
| 37 | _Delete shipment_ | Delete a shipment. | Change access of shipment register. | `Shipment` |
| 38 | _Delete warehouse_ | Delete a warehouse. | Change access of warehouse register. | `Warehouse` |
| 39 | _Delete vehicle_ | Delete a vehicle. | Change access of vehicle register. | `Vehicle` |
| 40 | _Delete internal request_ | Delete a internal request. | Change access of internal request register. | `Historial of warehouse in moving shipment`, `Historial of warehouse in moving vehicle` |
| 41 | _Delete route_ |Delete a route.| Change access of route register. | `Route` |
| 42 | _Delete request_ |Delete a route.|Change access of request register.| `Request` |
| 43 | _Find shipment in active route_ | Find if a shipment has a active route. | Code, status and creation datetime of route. Full name of driver associated to route.  | `Route`, `Shipment`, `Order`, `Status event order`, `Status event route` | 
| 44 | _Find order worked by driver_ | Find all orders was worked by specified driver. | All info of driver. Route and shipment code, datetime of creation of order and last status | `Driver`, `Order`, `Shipment`, `Route`, `Status event order` |
| 45 | _Create incident_ | Create a new incidents to management errors in operations. | All info of incidents an| `Incident`|
| 46 | _Delete incident_ |Delete a incident.| Change access of incident register. |`Incident`|
| 47 | _Change incidents in order status_ | Correct error of incidents associated to order. | ID of new and old incidents and ID of order. | `Order`, `Incident` |
| 48 | _Remove incidents from order status_ | Disconnet an incidents associated to order. | ID of current incidents and ID of order. | `Order`, `Incident` |
| 49 | _Find shipments based in geopositions_ | Find shipment based in spatial region. I need to filtered based in drop or pick up address. | All info shipment. | `Shipment` |
| 50 | _Change address in shipment_ | Change my pick up or drop address in shipment. | Position and description of drop / pick up address in shipment. | `Shipment` |


## Technical decision to create it 

This section in separate in 2 parts: analyze the previous section and decisions derived from it.

### Analyzing common queries

I checked all common queries from previous section, i detected some points:

* In general and regular cases, there are master data entities that are more accessed to read than other ones:
  * Shipment, route, order, branch, incidents, city and country.
  * Vehicle, driver, enterprise, Warehouse.
  * Request, internal request.
  * Others.
* In general and regular cases, there are master data entities that are more update and write than other ones:
  * Shipment, Status event order, order.
  * Route, Status event route.
  * Request and internal request.
  * Vehicle, warehouse, drivers.
  * Others.
* I need to apply soft delete in all register of master data, to keep all context in operations as long as possible.
* In amount of queries generated from mobile into entities: status event order, order(some fields), route (some fields), driver, vehicle(some fields), historial of driver.
* In mobile devices, it need to read more setup data, entities like: city, country, warehouse, incidents, vehicle, historial of driver, shipment (some fields).
* Some fields of shipment entity need to be in others entities to improve the reading opts by improve the operation read: order, city and country.
* I need to get flexibility to extend the follow entities by others areas will come (finance or operational): shipment, route, order, request, driver, warehouse.
* I need support geospatial queries: point inside of polygon.
* There are a group of entities classified like resource that are management in some points of operation: warehouse, vehicle and drivers.

### Decisión of design

These are decision making based on previous subsection.

* I need to separate the geospatial queries of tradicional queries in difference tables.
* Based in high write operations; these following table don't need to get extra info in its own table: Shipment and Status event order.

## Diagram

![Diagram of logical data model in mandalo startup](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/data_modeling_in_operational__area_logical/Mandalo%20-%20logical%20view%20data%20model%20_%20general.png)

### Note in diagram

_*_ The field in the table have a relationship with other table that define a schema of data. Generally it's applied in array of custom data type like field.

_**_ The Driver, vehicle and warehouse table are classified like resource, so then any one of them (only one of them) can be referenced to resource. It can be selected in operational act.

_***_ This field can be implemented freely and it not require a fixed schema. 

