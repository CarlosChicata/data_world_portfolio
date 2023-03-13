# Case 1: Document all process in operational area.

## Objective and understand Output artifacts

to understand the "mandalo" startup and implement a great data architecture, i need to understand all process they will implement to work. if i would like to give them a resilient and efficient architecture, i need to understand the  business in several parts:


* :heavy_check_mark: __Conceptual View of the business__ : understand the relationship between entities to define the business.
* :heavy_check_mark: __Data standard__: understand the attributes from entities and his semantic rules.
* :heavy_check_mark: __Workflow process__: understand all the processes that will use the end users in semantic focus.
* :heavy_check_mark: __Use cases of system__: Understand what user will use what processes in several systems.
* :heavy_check_mark: __Business glossary__: Document the understanding of entities, related organizational roles and others issues.
* :heavy_check_mark: __Data workflow process__: How the process generate data.

## Version and declarations

These declarations  about the case:

* These documents are selected based the diagrams of software engineering field, [this post of medium](https://medium.com/business-architected/conceptual-data-modelling-start-with-business-use-cases-10b3f2670d47) and [data architecture course Marco Aurelio's](https://www.linkedin.com/posts/marcoaurelioribeiro_just-a-gentle-reminder-that-my-practical-activity-7006729089021558784-zGe3?utm_source=share&utm_medium=member_desktop)
* The data standard is based in document of [repository of federal enterprise data resources of USA](https://resources.data.gov/standards/concepts/#data-standards-component) and [National center of biotechnology information](https://www.ncbi.nlm.nih.gov/books/NBK216088/)
* I applied a same structured a all entities because simplify to show. I know that all attribute need to own structured.
* If i'm wrong in generated document, image or diagram; please tell me! i wanna improve my skills! :blush:


| Version | Description |
|---------|-------------|
| 0.1.0   | Add conceptual view of the business section |
| 0.2.0   | Add Use case of system section |
| 0.3.0   | Add business glossary | 
| 0.4.0   | Add data standard | 
| 0.5.0   | Add workflow process | 
| 0.6.0   | Add data flow process | 
| 1.0.0   | Finish preliminar version to use | 

## Artifacts

### _Business glossary_

The purpose of this section is to list and explain all entities will be used, his defination, his relationship with roles & area, his metadata, his semantic rules and his names. Remenber that is a live document.

| Name | Definition | acronym | synonyms | Owner area | related Area | Owner role | Source system | Confidentiality level | Criticality level | Status |
|------|------------|---------|----------|------------|--------------|------------|---------------|-----------------------|-------------------|--------|
| __Shipment__ | Client request us to pick up his product and delivery his end user. |  | Cargo | Operational area | `Finance area`, `warehousing area`, `Customer experience` |  Operational regional manager | `Mandalo` | Confidential | High | Ok | 
| __Route__ | Group of shipment need to pick up and/or delivery based in his services. | | | Operational area | `Finance area` | Operational regional manager and financial regional manager | `Mandalo` | Internal | Low | Ok |
| __Order__ | Relationship between shipment and route. | | | Operational area | `Finance area` | Operationa regional manager and financial regional manager |  `Mandalo` | Internal | Low | Ok |
| __Driver__ | Driver works to us to pick up and/or delivery shipments our clients. | | Mandero |  Fleet area | `Operational area`| Fleet regional manager | `Mandalo` | Restrictive | High | Ok |  
| __Enterprise__ | Entity has a contract with us to give them in selected services by them. | | Client | Operatioanl area | `Finance area` |  Customer sucess manager | `Mandalo` | Confidencial | Low | Ok |
| __Branch__ | Sucursal of enterprise inside of city. ||| Operational area | `Customer sucess area` | Operational regional manager | `Mandalo` | Internal | low | Ok |
| __Service__ | specified operational flow to work in our team & infrastructure to give our clients. | | | Operational area | `Finance area` | Operational regional manager | `Mandalo` | Public | Low | Ok |
| __City__ | Location based in city to operate our team and infrastructure. |  | Sucursal | Operational area | `Finance area`, `Fleet area`, `Customer sucess area` | Operational regional manager | `Mandalo` | Public | Low | Ok |
| __Country__ | Location based in country to group several cities based geographically. | | Region | Operatinal area | `Finance area`, `Fleet area`, `Customer sucess area` | Operational regional manager | `Mandalo` | Public | Low | Ok |
| __Operational user__ | internal Staff to work in operational area | opt-user | operator | Operational area | | Operational regional manager | `Mandalo` | Restrictive | High | Ok |
| __Warehouse__ | Specified location point to store and process product of shipments. the staff will be operate from there and attend all drivers from the city. | WH | Storage | Operational area | `warehousing area` | Operational regional manager | `Mandalo` | Public | Low | Ok |
| __Vehicle__ | Means of transport used by the driver to move. it own by driver or not and there are several categories. | | | Fleet area | `Operational area` | Fleet regional manager | `Mandalo` | Internal | Medium | Ok |
| __Request__ | Notification of our client to us to indicate they need to use ur service based in resources. it can be deny or access. | | | Operational area | `Finance area` | Operational regional manager  | `Mandalo` | Confidential | High | Ok |
| __End user__ | Client of our client that they work in their system. | | end client | Operational area | `Customer experience` | Operatioanl regional manager | `Mandalo` | Restrictive | High | Ok |
| __Status event order__ | Registered status of activity from order. it generated when the order is working. ||| Operational area | | Operational regional manager | `Mandalo` | Restrictive | High | Ok | 
| __Status event route__ | Registered status of activity from route. it generated when the route is working. ||| Operational area | | Operational regional manager | `Mandalo` | Restrictive | High | Ok 
| __Crossdock__ | feature of some service that will use the warehouse as temporal point of storage to keep product. ||| Operational area | `Finance area` | Operational regional manager | `Mandalo` | Public | Low | Ok | 
| __Product__ | Objects that our client need to deliver their end users. ||| Operational area | `Finance area`, `Customer experience area` | Operational regional manager | `Mandalo` | Internal | High | Ok |
| __Incident__ | Event to effect  the order when it's working. it has a responsibility and price to discount to the order. ||| Operational area | `Finance area`, `Customer experience area` | Operational regional manager & financial regional manager  | `Mandalo` | Confidential | High | Ok |
| __Promise time__ | Deadline we need to deliver the shipment success. ||| Operational area | `Customer success area` | Operational regional manager | `Mandalo` | Internal | High | Ok |
| __Operational Resource__ | All means what client can use: drivers, warehouse, vehicle. | Opt-means | resource | Operational area | `Finance area`, `Customer sucess area` | Operational regional manager | `Mandalo` | Confidential | High | Ok |
| __handled shipment register__ | Register all changes applied to shipment to pass from the error to validated. ||| Operational area | `Customer experience area` | Operational regional manager | `Mandalo` | Confidential | High | Ok |
| __Historial of vehicle__ | Register what driver is used our vehicle to work and his status. ||| Operational area | `Finance area` | Operational regional manager | `Mandalo` | Confidential | High | Ok |
| __Historial of warehouse in moving vehicle__ | Register what vehicle is get in and get out of this warehouse, to store them. ||| Operational area | | Operational regional manager | `Mandalo` | Confidential | High | Ok |
| __Historial of driver__ | Register what service the driver was working and current one. ||| Operational area | `Fleet area`, `Finance area` | Operational regional manager | `Mandalo` | Confidential | High | Ok |
| __Historial of warehouse in moving shipment__ | Register what shipmen will be moving to other warehouse. ||| Operational area | `Customer experience area` | Operational regional manager | `Mandalo` | Confidential | High | Ok |


#### Semantic rules

##### Shipment

1. It always has a pick up and drop address, service, client, warehouse will store it, city, enterprise, promse time, minimum distance between both address, fullname , email and phone number of end user in both points.
2. The pick up and drop address need to be validate with geospatial location.
3. All shipment will assign a unique code of operation (track code) in all system.
4. The status of the shipment are: `Validated`, `With Errors`, `Cancelled`, `Picked up`, `Picking up`, `Delivering`, `Delivered`, `Failed pick up`, `Failed delivery`, `Damaged`, `Missing`, `In warehouse`, `Returning`, `Returned`, `Crossdocking` and `Crossdocked`.
5. Any shipment never will get a duplicated code/track code.
6. The price of shipment will be generated when its status is `Delivered` or `Returned`, and use to charge to client request it.
7. The shipment will get the last status of order or decisition indicated from operational user.
8. The client indicate when shipment fail in pick up or drop operation, it can be return to client or store in our warehouse.
9. If shipment in created with error, it will get a register of change, to monitoring all change applied this shipment before it already validated to work.
10. If shipment need to return to warehouse, return to warehouse specified in shipment information.

##### Order

1. The status of order are: `Validated`, `Start`, `Picked up`, `Picking up`, `Delivering`, `Delivered`, `Failed pick up`, `Failed delivery`, `Returning`, `Returned`, `Crossdocking`, `Finished` and `Crossdocked`.
2. It always has a shipment, driver asociated and route.
3. All orders need to be liquidated to pay the drivers.
4. All order with  `Delivered`, `Failed pick up`, `Failed delivery`, `Returned` and `Crossdocked` status have a price, and use to pay the drivers. 
5. Order can transfer to other driver, when original drive can't work anyway. When happened, you created other register.


##### Route

1. The status of route are: `Created`, `Dispatched`, `Completed`, `Working`, `Cancelled`, `Transfered`, `Accepted` and `Offered`
2. It always has a list of orders, vehicle to recommend to use in this route, driver, vehicle used by driver, liquidation( status and timestamp), user create it & code of route.
3. When route is in `Completed` status; calculate the price to pay the driver.
4. The route can assign an incentive to encourage take it.
5. the route can transfer to other driver then original drive can't work in this route.
6. All route can be assigned or offered to drivers.

##### Status event order

1. It has, status of event in order to work, the user changed it, incidents associated the event, timestampt to regist the event, reason of change.
2. All events associated to specified order need to follow the structure of status flow order.
3. No order has a previous timestamp than other if its status is after the status other.

##### Status event route

1. It has, status of event in order to work, the user changed it, incidents associated the event, timestampt to regist the event.
2. All events associated to specified order need to follow the structure of status flow route.
3. No order has a previous timestamp than other if its status is after the status other.

##### Enterprise

1. It has commercial name, business name, commercial, datetime of registration, country it works.

##### Branch

1. It has document of identify, city, corporative phone, corporative email, commercial name, business name, commercial representative, datetime of registration, address, opening hours, service used, enterprise related.
2. All enterprise need one o more contract to us using a specified service.
3. All enterprise can; not mandatory; receive notification of change status in their orders.

##### Operational user

1. It has fullname, role, team, list of permission, birthday datetime, registration datetime, city.
2. All user work limited by permissions.

##### Request

1. It always has a description, status, registration datetime, enterprise, datetime in started operation, datetime in finished operation, type of resource, list compensation of incomplete terms, price of usage service, list of emergency plans, price of devolution.
2. All request can be either rejected or accepted.
3. If request is incomplete will apply a compensation based incomplete specified terms.
4. If we need to use some requested resource; we apply any plan of emergency and return price of devolution based in selected plan.
5. Several request can be sent by one enterprise.

##### Incident

1. It has description, responsibility, relationship with status of order, discount value of driver, discount operator  of driver, apply discount in driver, city.
2. All options to responsibility are: `mandalo`, `end client`, `driver`, `external event`, `other`.

##### Driver

1. It always has document of identity, address, full name, birthday datetime, registrarion datetime, SOAT caducated datetime, SOAT Number, License caducated datetime, License number, Bank account number, vehicle, city, legal background documents, period of pay, is using internal vehicle.
2. All drivers always need to get the SOAT updated.
3. All drivers always need to get the driver license updated.
4. All drivers always need to be of legal age.
5. All drivers can work any corporative vehicle, but i will cost in the payment.
6. All drivers can use a own vehicle.
7. All drive get a historial about the service he is work with us.

##### Vehicle

1. It has a plate, type of vehicle, is ours or not, city, responsable user, warehouse store it.
2. All vehicle will get a historial of request, in case of borrow internal drivers.
3. Status of vehicle are: `Repaired`, `Available`, `Unavailable`, `Using by driver`.
4. Vehicle can move to other warehouse in same or other city.

##### Warehouse

1. It has address, max capacity of shipment, can receive vehicle from other city, max capacity of received vehicle, current vehicle internal store.
2. Each warehouse get a historial of internal vehicle store.
3. Status of warehouse are: `Available`, `Unavailable`.
4. If warehouse can't store shipment by over capacity, either it can sent  to other warehouse in same city and notify the client; or reject shipment.

##### Service

1. it has registration of service, cities it works, datetime in started application, datetime in finished application, min time of delivery shipment,  max time of delivery shipment, can use crossdock, kind of service, has apply in sunday, has apply in holi day, vehicle can use in this service, description, list compensation in incomplete terms.
2. No all service is available in cities, depend of context of city.
3. All shipment need to tie to specified service.
4. The service never have custom to enterprise.

##### Handled shipment register

1. It has shipment related, list of change will apply, registration datetime, user change shipment, status of changed shipment.
2. this register is created by user with permission.

##### Historial of vehicle

1. It has vehicle related, registration datetime, user register this event, driver will get it, datetime in start operation, datetime in finish operation, cost of usage, status of returned vehicle, datetime of paid cost of usage, is vehicle damaged?, cost of repairs in vehicle, is reject or accept, reason to reject/acces.
2. This register is created by user with permission.
3. The cost depend of type of vehicle will borrow.
4. If vehicle is damaged, the responsable pay all repairs.

##### Historial of warehouse in moving vehicle

1. It has warehouse request to get vehicle, user register this event, vehicle will move, permanent moving or not, datetime to start temporal store, datetime to finish  temporal store, reason to moving, reason to reject/accept, is reject or accept.
2. This register is created by user with permission.
3. Other user with same permission in selected warehouse can reject or accept the request.

##### Historial of warehouse in moving shipment

1. It has warehouse will store the shipment, shipment related, register this event, reason to reject/accept, is reject or accept, user register this event.  
2. This register is created by user with permission.
3. Other user with same permission in selected warehouse can reject or accept the request.

##### Historial of driver

1. It has a driver related, user register, reason to moving, reject or accept, reason to reject/access, service, datetime to start work in the service, datetime to finish work in the service.
2. This register is created by user with permission.
3. Other user with same permission in selected warehouse can reject or accept the request.


### _Data standard_

This section contain all information formatting and validation requirements our entities in this area in more detail. **Note**: you can use the conceptual

#### Shipment

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Code**_ | String | 14 | Not | First 3 characters (prefix of enterprise), and rest of number. It need to be unique inside enterprise. | Not available | code for easy recognition of an order for the customer. |||| String | Not available |
| _**Use crossdock**_ | Boolean | 1 | Not | One of all in value list. | False | Indicate is shipment will use in crossdock feature in operation. | | | `False`, `True` | Boolean | No available |
| _**Price of product**_ | Decimal number | 2 decimals and 1-15 integer. | Not | Never be null. | 0.00 | Price of product that client want to deliver their end client. | 0.00 | 999999999999999.99 | | Double precision | No available |
| _**pick up address**_ | String | 20 - 120 | Not | Minimun get 20 characters lenght. | Not available| Addresss to pick up the shipment. |||| String | Not available |
| _**pick up geolocation**_ | Coordinates | 40-60 | Not | Each coordinate need to be 15 decimals. | Not available | Location geospatial of address of picking up shipment. |||| JSON | Decimal degrees |
| _**pick up address reference**_ | String | 0 - 100 | Yes || Null | Reference of location to pick up shipment. |||| String | Not available | 
| _**pick up primary reference**_ | String | 3 - 50 | Not | Never be null | Not available | next national division of city; District per example in Perú. |||| String |Not available|
| _**pick up note**_ | String | 0-100 | Yes ||| Note to driver to know about the pick up operation. |||| Integer. Foreign key of another table. |Not available| 
| _**pick up contact fullname**_ | String |  20-60 | Not | Minimun length is 20 characters. || Fullname of user will give the shipment. |||| String |Not available| 
| _**pick up contact phone**_ | String | 6-15 | Not | Never be null. Make sure the minimum characters needed. Only Number, "+" , whitespace. | Not available | Cellphone of user will give the shipment. |||| String |Not available|
| _**pick up contact identity document type**_ | Option | 1 | Not | Never be null. | Not available. | Document of identity of contact. |||| String |Not available|
| _**pick up contact identity document value**_ | String | Not defined | Not | Never be null. It need to follow the rule of value of selected identity document type. |Not available. |  Value of document type of contact. |||| String |Not available|
| _**pick up contact email**_ | String | 20-50 | Yes | Valide this regex: `/^[a-zA-Z0-9.!#$%&'*+/=?^_{}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.`| Null | Email of user will give the shipment. |||| String | Not available |
|_**drop address**_ | String | 20 - 120 | Not | Minimun get 20 characters lenght. | Not available| Addresss to pick up the shipment. |||| String | Not available |
| _**drop geolocation**_ |  Coordinates | 40-60 | Not | Each coordinate need to be 15 decimals. | Not available | Location geospatial of address of picking up shipment. |||| JSON | Decimal degrees |
| _**drop address reference**_ | String | 0 - 100 | Yes || Null | Reference of location to pick up shipment. |||| String | Not available | 
| _**drop primary reference**_ | String | 3 - 50 | Not | Never be null | Not available | next national division of city; District per example in Perú. |||| String |Not available|
| _**drop note**_ | String | 0-100 | Yes ||| Note to driver to know about the pick up operation. |||| String |Not available| 
| _**drop contact fullname**_ |String |  20-60 | Not | minimun length is 20 characters. || Fullname of user will give the shipment. |||| String |No available| 
| _**drop contact phone**_ |String | 6-15 | Not | Never be null. Make sure the minimum characters needed. Only Number, "+" , whitespace. | Not available | Cellphone of user will give the shipment. |||| String |Not available| 
| _**drop contact email**_ | String | 20-50 | Yes | Valide this regex: `/^[a-zA-Z0-9.!#$%&'*+/=?^_{}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.` | Null | Email of user will give the shipment. |||| String | Not available |
| _**drop contact identity document type**_ | Option | 1 | Not | Never be null. | Not available. | Document of identity of contact. |||| String |Not available|
| _**drop contact identity document value**_ | String | Not defined | Not | Never be null. It need to follow the rule of value of selected identity document type. |Not available. |  Value of document type of contact. |||| String |Not available|
| _**creation**_ | datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**is damaged**_ | Boolean| 1 | Not | One of all in value list.| False | Indicate if shipment is damaged. ||| `False`, `True` | Boolean | Not available |
| _**promise time**_ | Timestamp |  YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Deadline to deliver this shipment success. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Distance**_ | Decimal | 4 decimals with 3 integers | Not | Always greater than 0.0000 | 0.0001 | Approximatly distance between 2 points. | 0.0001 | 999.9999 | |Double precision | Kilometers |
| _**Description product**_ | String | 3-120 | Not ||| Description of product. |||| String | Not available |
| _**Status**_ |Option | 1 | Not | Choose one of value list | Not available | Status last of shipment.||| `Validated`, `Start`, `Picked up`, `Picking up`, `Delivering`, `Delivered`, `Failed pick up`, `Failed delivery`, `Returning`, `Returned`, `Crossdocking`, `Finished` and `Crossdocked` |String | Status of order|

**Nota**: Hay una relacio a la entidad con branch (drop/pick up), warehouse location, city, service, status, enterprise, size of package|, empresas.

#### Enterprise

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Commerical name**_ | String | 3-5' | Not || Not available | Commercial Name of enterprise |||| String | Not available |
| _**Business name**_ | String | 3-5' | Not || Not available | Business Name of enterprise |||| String | Not available |
| _**Countries**_ | List of Country | 0-150 | Not | Never be null | [] | List of branch that enterprise works. |||| Array of ID |Not available|

Nota: debe enlazarse con sus sucursales, ordenes.

#### Branch

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Commerical name**_ | String | 3-5' | Not || Not available | Commercial Name of enterprise |||| String | Not available |
| _**Business name**_ | String | 3-5' | Not || Not available | Business Name of enterprise |||| String | Not available |
| _**Corporative phone**_ | String | 5 - 50 | Not | Never be null. Make sure the minimum characters needed. Only Number, "+" , whitespace. | Not available | Phone of warehouse. |||| String | Not available |
| _**Corporative email**_ | String | 20-50 | Yes | Valide this regex: `/^[a-zA-Z0-9.!#$%&'*+/=?^_{}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.` | Null | Email of user will give the shipment. |||| String | Not available |
| _**address**_ | String | 20 - 120 | Not | Minimun get 20 characters lenght. | Not available| Addresss of location the branch. |||| String | Not available |
| _**opening hours**_ | Schedule | Not define | Not | Never Null. It need at least one row. | Not available | Schedule of attention to end clients. |||| JSON | Not available | 
| _**Legal representative fullname**_ |String |  20-60 | Not | minimun length is 20 characters. || Fullname of user will give the shipment. |||| String |No available|

Nota: su relacion con empresa, servicios que utiliza, solicitudes

#### Order

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Start datetime**_ | datetime | YYYY/MM/DD HH:MM:SS | Not | After the creation of route associated. All value based in gregory calendar. timezone with UTC-0. | Not available | datetime to start to work it. | 1992/01/01 | 9999/12/31 || Timestamp with timezone | Gregory calendar |
| _**Finish datetime**_ | datetime | YYYY/MM/DD HH:MM:SS | Not | After the creation of route associated. All value based in gregory calendar. timezone with UTC-0. | Not available | datetime to finish to work it. | 1992/01/01 | 9999/12/31 || Timestamp with timezone | Gregory calendar |
| _**Price**_ | Decimal number | 2 decimals and 1-15 integer. | Yes || Null | Price assigned to operation | 0.00 | 999999999999999.99 | | Double precision | No available |
| _**Transfered**_ | Boolean | 1 | Not | One of all in value list. | False | Indicate it was transfered ||| `False`,`True` | Boolean | Not available |
| _**Reason of transferd**_ | String | 5-100 | Not | Never be null. Minimun length is 5 characters. | Not available | Reason to transfer order to other availabled driver. |||| String | Not available |  
| _**Datetime of transferd**_ | datetime | YYYY/MM/DD HH:MM:SS | Not | After the creation of route associated. All value based in gregory calendar. timezone with UTC-0. | Not available | datetime to transfered to other route to continue operate it. | 1200/01/01 | 9999/12/31 || Timestamp with timezone | Gregory calendar |
| _**Remove**_ | Boolean | 1 | Not | One of all in value list.. | False | Indicate it was deleted ||| `False`,`True` | Boolean | Not available |
| _**Reason of remove**_ |String | 5-100 | Not | Never be null. Minimun length is 5 characters. | Not available | Reason to delete this order. |||| String | Not available | 
| _**Status**_ |Option | 1 | Not | Choose one of value list | Not available | Status last of order.||| `Cancelled`, `Validated`, `Start`, `Picked up`, `Picking up`, `Delivering`, `Delivered`, `Failed pick up`, `Failed delivery`, `Returning`, `Returned`, `Crossdocking`, `Finished` and `Crossdocked` |String | Status of order|
| _**Shipment**_ | 14 | 1 | Not | Associated to any row in shipment table. | Not available | Shipment will operate. |||| Integer. Foreign Key in table. | Shipment |
| _**creation**_ | datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |

Nota: debe tener Shipment, route (para el original y otra para cuando fue transferido), driver, status, incidencia. usuario del staff (por lremoverlo)

#### Driver

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**First name**_ |String |  20-60 | Not | Minimun length is 20 characters. || First name of driver. |||| String |Not available|
| _**Last name**_ |String |  20-60 | Not | Minimun length is 20 characters. || Last name of driver. |||| String |Not available|
| _**Identity document type**_ | Option | 1 | Not | Never be null. | Not available. | Document of identity of contact. |||| String |Not available|
| _**Identity document value**_ | String | Not defined | Not | Never be null. It need to follow the rule of value of selected identity document type. |Not available. |  Value of document type of contact. |||| String |Not available|
| _**Birthday**_ | datetime | YYYY/MM/DD | Not |All value based in gregory calendar. timezone with UTC-0. | Not available | Birthday of driver | 1200/01/01 | 9999/12/31 || Timestamp with timezone | Gregory calendar |
| _**Registration**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register in system. |||| Timestamp with timezone UTF-0 | Gregorian calendar |
| _**is validated**_ | Boolean |1 | Not |  One of all in value list. | False | Indicate he is validated to operate with us.||| `False`,`True` | Boolean | Not available |
| _**validated datetime**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Indicate what time he is validated to operate with us. |||| Timestamp with timezone UTF-0 | Gregorian calendar |
| _**SOAT deadline**_ | datetime | YYYY/MM/DD | Not | All value based in gregorian calendar. timezone with UTC-0.|| Indicate his SOAT will caducate. |||| Timestamp with timezone UTF-0 | Gregorian calendar |
| _**SOAT number**_ |String | 8-30 | Not | Never be null. Only alphanumeric characters. | Not available | Number of SOAT he has. |||| String | Not available |
| _**has SOAT**_ | Boolean |1 | Not | One of all in value list. | False | Indicate he has a SOAT. ||| `False`,`True` | Boolean | Not available |
| _**License driver deadline**_ |datetime | YYYY/MM/DD | Not | All value based in gregorian calendar. timezone with UTC-0.|| Indicate his drive license will caducate. |||| Timestamp with timezone UTF-0 | Gregorian calendar |
| _**License driver number**_ |String | 10-30 | Not | Never be null. Only alphanumeric characters. | Not available | Number of driver license he has. |||| String | Not available |
| _**has License driver**_ |Boolean |1 | Not |  One of all in value list. | False | Indicate he has drive license.||| `False`,`True` | Boolean | Not available |
| _**Bank number account**_ | String | 10-30 | Not | Never be null. Only alphanumeric characters. | Not available | Number of bank account he will receive his payment. |||| String | Not available |
| _**has own vehicle**_ |Boolean | 1 | Not | One of all in value list. | False | Indicate he has own vehicle.||| `False`,`True` | Boolean | Not available |
| _**use internal vehicle**_ |Boolean | 1| Not |One of all in value list. | False | Indicate he will use internal vehicle to work.||| `False`,`True` | Boolean | Not available |
| _**has legal background documents**_ | Boolean |1 | Not |One of all in value list. | False | Indicate he had legal problem before to work to us.||| `False`,`True` | Boolean | Not available |
| _**period of pay**_ | date | MM/DD | Not | Never be null. Value based in gregorian calendar. | Not available | Month and day will pay the driver| 01/01 | 12/31 || date| gregorian calendar |

Nota: tipo de identidad de documento, vehicule, city

#### Route

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Start datetime**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0. Greater or equal than all order's creation. || Datetime to start route. |||| Timestamp with timezone UTF-0 | Gregorian calendar |
| _**Finish datetime**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0. Greater or equal than all order's creation.|| Datetime to finish route. |||| Timestamp with timezone UTF-0 | Gregorian calendar |
| _**Price**_ | Decimal number | 2 decimals and 1-15 integer. | Yes | | Null | Price we will pay to driver to work this route. | 0.00 | 999999999999999.99 | | Double precision | No available |
| _**Incentive operational**_ | Option | 1 | Yes | If it is not null, i must be a "Incentive price" not null. One of all in value list. | Null | Indicate what operation will use in incentive.||| `add`, `Multiply` | String | Not available |
| _**Incentive price**_ | Decimals | 1 integer and 3 decimals. | Yes |It always must be 1 integer and 3 decimals. If it is not null, i must be a "Incentive operational" | Null |Amount will use to add value to price. |  0.000 | 9.999 || Decimals | Not available|
| _**Creation**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Is liquidation**_ |Boolean |1 | Not | One of all in value list. | False | Indicate it was liquidated or not.||| `False`,`True` | Boolean | Not available |
| _**Route code**_ | String | 14 | Not | All characters are alphanumeric. Don't be duplicate. | Not available | code for easy recognition of an route. |||| String | Not available |
| _**Type of work**_ | Option | 1 | Not | Choose one of value list | Not available | Indicate if route is offered or assigned to specified driver. ||| `Offered`,`Assigned` | String | Type of work in drivers |
| _**Status**_ |Option | 1 | Not | Choose one of value list | Not available | Status of event in route.||| `Created`,`Dispatched`,`Completed`,`Working`,`Cancelled`, `Transfered`, `Accepted`, `Offered` |String | Status of route|

Nota: drivers, city, status, order, vehicle ( use and recommend)

#### Service

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Name**_ | String | 0-14 | Not | Unique name. | Not available | Name of service. |||| String | Not available |
| _**Type of service**_ | Option | 1 | Not | Never be null. One of all in value list. | Not available | Kind of service will be. One of all in value list. ||| `Resource based`,`Order based` | ID, foreign key to other table | Not available |
| _**Description**_ | Text | 10-120 | Not | Never be null and duplicated. | Not available | Description of service |||| String | Not available |
| _**is limit time**_ | Boolean | 1 | Not |  One of all in value list. It's exist, "min hours" and "max hours" are not null. | False | Indicat it works in limite range hours: 1-3 hours ||| `True`,`False` | Boolean | Not available |
| _**min hours**_ | Integer | 1 | Yes | if "is limit time" is not false, it must not be null. | Null | Min hours add to create the promise time.|||| Integer | Integer number |
| _**max hours**_ | Integer | 1 | Yes | if "is limit time" is not false, it must not be null. | Null | Max hours add to create the promise time.|||| Integer | Integer number |
| _**use crossdocking**_ |Boolean | 1 | Yes |  One of all in value list. | Null | Indicat if it can use crossdock feature. ||| `True`,`False` | Boolean | Not available |
| _**has work sundays**_ |Boolean | 1 | Yes |  One of all in value list. | Null | Indicat it works in sundays ||| `True`,`False` | Boolean | Not available |
| _**has work holidays**_ |Boolean | 1 | Yes | One of all in value list.. | Null | Indicat it works in holidays ||| `True`,`False` | Boolean | Not available |
| _**Limit time to delivery**_ | Setup | Not available | Yes | It can be null when "is limit time" field is true. | Not available | Setup the max time the shipment can delivere it |||| JSON | Not available |
| _**applied vehicle to use**_ | Options | 1 or more | Yes| Never be null. One of all in value list at least. | Null | Indicat what vehicle the driver can use in this service. ||| `Moto`, `Van,`,`Convoy`,`Car`| String | Vehicle |
| _**Resource**_ | Option | 1 | Not | Never be null. It need to be `Resource based` in "Type of service". One of all in value list. |`Not available | Resource can used in service. ||| `Vehicle`, `Driver`, `Warehouse` |  String | Operational Resource |
| _**List compensations in incomplete terms**_ | List of terms | Not available | Yes | | Null | List compensation in case of incomplete terms both ours and clients. |||| JSON | Not available |
| _**max time to notify us**_ | time and days | DD  HH:MM:SS | Yes | Available in `Resource based` and `Scheduled` service. | Indicate the minimum time to notify us about a service | 00 24:00:00 | 99 23:99:99 || timestampt | Time and days |

Nota: city, empresas, ordenes, tipo de vehiculos.

#### City

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Time zone**_ | timezone | 10-30 | Not | Never be null. | Not available | Time zone in city. |||| String | UTC |
| _**Geospatial area**_ | Geospatial | Polygon | Not | Never be null. | Not available | geospatial perimeter of the city. |||| Array of lines | Not available |
| _**Name**_ | String | 1-100 | Not | Never be null. | Not available | Common name of city inside Country. |||| String | Not available | 
| _**Governal name**_ | String | 1-150 | Not | Never be null. | Not available | Governal name of city inside Country. |||| String | Not available |
| _**Postal code list**_ | List of code | Not available | Not | Never be null. |Not available | List of postal code inside city. |||| Array of string | Not available |

Nota: relacion con shipment, country, route, warehouse, drivers, vehicle, request, branch

#### Country

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Name**_ |String | 1-100 | Not | Never be null. | Not available | Common name of Country. |||| String | Not available | 
| _**Governal name**_ |String | 1-150 | Not | Never be null. | Not available | Governal name Country. |||| String | Not available |
| _**prefix phone**_ | String | +(0-9){2,5} | Not | Never be null. | Not available | Prefix in all phone to call in this country. | +00 | +99999 || String | Not available |  
| _**currency ISO**_ | String | 1-3 | Not | Never be null. | Not available |Short name of currency inside country. |||| String | Not available |
| _**Acronomy**_ | String |2-5 | Not | Never be null. | Not available | Acronomy of name. |||| String | Not available |
| _**Capital**_ |String | 1-150 | Not | Never be null. | Not available | name of capital in country. |||| ID, foreign key of table. | Not available |  
| _**Geospatial area**_ | Geospatial | Polygon | Not | Never be null. | Not available | geospatial perimeter of the city. |||| Array of lines | Not available |

Nota: relation con warehouse, city, request, shipment

#### Request

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Code**_ | String | 14 | Not | First 3 characters (prefix of enterprise), and rest of number. It need to be unique inside enterprise. | Not available | code for easy recognition of request of client. |||| String | Not available |
| _**Price**_ | Decimal number | 2 decimals and 1-15 integer. | Yes | | Null | Price the client will pay for service | 0.00 | 999999999999999.99 | | Double precision | No available |
| _**Description**_ | Text | 20-400 | Not | Never be null| Not available | Description to explain the reasons to request our resources. |||| String | Not available |
| _**Response**_ | Option | 1 | Yes | If it's not null, the "Reason of response" field must not be null too. Choose one from the value list. | Null| Indicate if accept or reject the request. ||| `Accepted`,`Rejected` | String | Not available|
| _**Reason of response**_ | Text | 20-300 | Yes | If it's not null, the "Response" field must not be null too.|Null| Reason to choose the response |||| String | Not available |
| _**Resource type**_ | Option | 1 | Not | Choose one from the value list. || Indicate what type of resource the client wanna use. ||| `Driver`,`Warehouse`, `Vehicle` | String | Not available|
| _**Creation**_ | datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Response datetime**_ | datetime | YYYY/MM/DD HH:MM:SS | YES | If it's not null, the "Response" field must not be null too.All value based in gregorian calendar. timezone with UTC-0.|Null| Datetime the operational user responsed the client. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Start datetime**_ | datetime | YYYY/MM/DD HH:MM:SS | YES | All value based in gregorian calendar. timezone with UTC-0. It's greater than "Creation" field and obey the defined constraint in service. |Null| Datetime to start the request. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Finish datetime**_ | datetime | YYYY/MM/DD HH:MM:SS | YES | All value based in gregorian calendar. timezone with UTC-0. It's greater than "Creation" field and obey the defined constraint in service.| Null| Datetime to finish the request. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**List compensation of incomplete terms**_ | List of terms | Not available | Yes | | Null | List compensation in case of incomplete terms both ours and clients. |||| JSON | Not available |
| _**List of resource**_ | List of resource | Array de resource | Yes | If "Response" field is "Accepted"; It has at least one resource. | Null | List of resource the client will use. |||| Array of integer. All integer are foreign key. | Our resource|

Nota: Branch, user staff, Service, drivers, warehouse, vehicle

#### Operational user

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|---------------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|------|
| _**First name**_ |String |  20-60 | Not | Minimun length is 20 characters. || First name of driver. |||| String |Not available|
| _**Last name**_ |String |  20-60 | Not | Minimun length is 20 characters. || Last name of driver. |||| String |Not available|
| _**Identity document type**_ | Option | 1 | Not | Never be null. | Not available. | Document of identity of contact. |||| String |Not available|
| _**Identity document value**_ | String | Not defined | Not | Never be null. It need to follow the rule of value of selected identity document type. |Not available. |  Value of document type of contact. |||| String |Not available|
| _**Birthday**_ | datetime | YYYY/MM/DD | Not |All value based in gregory calendar. timezone with UTC-0. | Not available | Birthday of driver | 1200/01/01 | 9999/12/31 || Timestamp with timezone | Gregory calendar |
| _**Registration**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register in system. |||| Timestamp with timezone UTF-0 | Gregorian calendar |
| _**is validated**_ | Boolean |1 | Not |  One of all in value list. | False | Indicate he is validated to operate with us.||| `False`,`True` | Boolean | Not available |
| _**validated datetime**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Indicate what time he is validated to operate with us. |||| Timestamp with timezone UTF-0 | Gregorian calendar |
| _**Main role**_ | Option | 1 | Not | Never be null.| Not available | Main role of user in organization. ||| Not available | Integer, ID foreig to table | Not available |
| _**Bank number account**_ | String | 10-30 | Not | Never be null. Only alphanumeric characters. | Not available | Number of bank account he will receive his payment. |||| String | Not available |
| _**has legal background documents**_ | Boolean |1 | Not |One of all in value list. | False | Indicate he had legal problem before to work to us.||| `False`,`True` | Boolean | Not available |
| _**period of pay**_ | date | MM/DD | Not | Never be null. Value based in gregorian calendar. | Not available | Month and day will pay the driver| 01/01 | 12/31 || date| gregorian calendar |


Nota: roles, documento de identidad, city

#### Vehicle

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|---------------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Plate**_ | String | Not available | Not | Never be null | Not available | Plate of vehicle. |||| String | Not available |
| _**Registration datetime**_ | datetime | YYYY/MM/ | Not | Not available | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**who is owner**_ | Option | 1 | Not | Choose one of value list. Never be null. | Not available | Define who is own of vehicle. |||| `Driver`,`Ours` | String | List of owner |
| _**Status**_ | Option | 1 | Not | Choose one of value list. Never be null. |  Not available |Status of vehicle |||| `Repaired`, `Available`, `Unavailable`, `Using by driver` | String | List of status in vehicle | 
| _**warehouse keep**_ | Location |  polygon area | Not | Never be null. | Not available | Warehouse keep its. |||| Integer. Foreign key to other table. | List of warehouse |

Nota: tipo de vehiculo, route, city, warehouse que lo contiene, request

#### Warehouse

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Address**_ | String | 20 - 120 | Not | Minimun get 20 characters lenght. | Not available| Addresss of location the warehouse |||| String | Not available |
| _**Phone**_ | String | 5 - 50 | Not | Never be null. Make sure the minimum characters needed. Only Number, "+" , whitespace. | Not available | Phone of warehouse. |||| String | Not available |
| _**Email**_ | String | 20-50 | Yes | Valide this regex: `/^[a-zA-Z0-9.!#$%&'*+/=?^_{}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.` | Null | Email of the representative user in warehouse. |||| String | Not available |
| _**Area**_ | Geospatial | Polygon | Not | Never be null. | Not available | geospatial perimeter of the warehouse. |||| Array of lines | Not available |
| _**Can store vehicle**_ | Boolean |1 | Not |  One of all in value list. | False | Indicate it stores vehicle.||| `False`,`True` | Boolean | Not available |
| _**Can receive vehicle from other city**_ | Boolean |1 | Not |  One of all in value list. | False | Indicate it can receive vehicle from other warehouse in other city.||| `False`,`True` | Boolean | Not available |
| _**Max capacity of shipment**_ | Dimensions | {Height, Width, Length} | Not | All field need higher than 0.  Never be null | Not available | Maximum capacity that warehouse can store shipments. |||| JSON | Dimensions |
| _**Max capacity of received vehicle**_ |Dimensions | Not available | Not | It need at least one field  | Not available | Maximum capacity that warehouse can store vehicle. |||| JSON | Dimensions | 
| _**Current vehicle internal store**_ |Dimensions | Not available | Not | It need at least one field. It has same fields like "Max capacity of received vehicle" field. The account is less or equal than  similir field in "Max capacity of received vehicle" | Not available | Maximum capacity that warehouse can store vehicle. |||| JSON | Dimensions | 
| _**Code**_ |  String | 5 | Not | First 3 characters, and rest of number. It need to be unique inside warehouse. | Not available | code for easy recognition of warehouse. |||| String | Not available |

Nota: Order, vehicle, request, 

#### Incident

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Name**_ | String | 1-100 | Not | Never be null. | Not available | Common name of incidents. |||| String | Not available |
| _**Description**_ | Text | 10-120 | Not | Never be null and duplicated. | Not available | Description of incident. |||| String | Not available |
| _**Responsibility**_ |Option | 1 | Not | Choose one of value list. Never be null. | Not available | Define who is responsibility this incidents. |||| `mandalo`,`end client`,`driver`,`external event`,`other` | String | List of responsibility |
| _**Apply discount in driver**_ | Boolean |1 | Not |  One of all in value list. | False | Indicate it apply to discount in price of order.||| `False`,`True` | Boolean | Not available |
| _**Discount operator of driver**_ | Option | 1 | Yes | If it is not null, i must be a "Discount value of drive" not null. One of all in value list. | Null | Indicate what operation will use in discount.||| `add`, `Multiply` | String | Not available |
| _**Discount value of driver**_ | Decimals | 1 integer and 3 decimals. | Yes |It always must be 1 integer and 3 decimals. If it is not null, i must be a "Discount operator of driver" not null | Null |Amount will use to add value to price. |  0.000 | 9.999 || Decimals | Not available|

Nota: estados del orden, city

#### Status event route

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Creation**_ | datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Created by user**_ | String | 0-50 | Not | Never be null. It must be a operation user | Not available | Indicate what user create it. |||| Integer. Foreign key | Not available |
| _**created user type**_ | Option | 1 | Not | Never be null | Not available  | Indicate type of user. ||| `Driver`, `Operational user` | String | Not available |
| _**Status**_ |Option | 1 | Not | Choose one of value list | Not available | Status of event in route.||| `Created`,`Dispatched`,`Completed`,`Working`,`Cancelled`, `Transfered`, `Accepted`, `Offered` |String | Status of route|

Nota: incidents, Order, driver of staff related, status

#### Status event order

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Creation**_ | datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Created by user**_ | String | 0-50 | Not | Never be null. It must be a operation user | Not available | Indicate what user create it. |||| Integer. Foreign key | Not available |
| _**created user type**_ | Option | 1 | Not | Never be null | Not available  | Indicate type of user. ||| `Driver`, `Operational user` | String | Not available |
| _**Status**_ |Option | 1 | Not | Choose one of value list | Not available | Status of event in order.||| `Validated`, `Start`, `Picked up`, `Picking up`, `Delivering`, `Delivered`, `Failed pick up`, `Failed delivery`, `Returning`, `Returned`, `Crossdocking`, `Finished` and `Crossdocked` |String | Status of order|

Nota: route.

#### Handled shipment register

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Shipment**_ | 14 | 1 | Not | Associated to any row in shipment table. | Not available | Shipment will operate. |||| Integer. Foreign Key in table. | Shipment |
| _**Creation**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Status of changed shipment**_ | Option | 1 | Not | Choose one of value list | Not available | Status of shipment after applied all change.||| `Cancelled`, `Validated`, `Start`, `Picked up`, `Picking up`, `Delivering`, `Delivered`, `Failed pick up`, `Failed delivery`, `Returning`, `Returned`, `Crossdocking`, `Finished` and `Crossdocked` |String | Status of order| 
| _**Status of previous shipment**_ | Option | 1 | Not | Choose one of value list | Not available | Status of shipment befor applied all change.||| `Validated`, `Start`, `Picked up`, `Picking up`, `Delivering`, `Delivered`, `Failed pick up`, `Failed delivery`, `Returning`, `Returned`, `Crossdocking`, `Finished` and `Crossdocked` |String | Status of order|
| _**List of change**_ | List of change | Not available | Yes | Separate all lines using points| Null | List of changes will apply to shipment.|||| String | Not available |

Nota: shipment, operational user

#### Historial of vehicle

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Creation**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Associated driver**_ | String | 5-50 | Not | Reference to existed and validated row in Driver table. | Not available | Driver requested to us use a vehicle |||| Integer. Foreign key in other table. | Not available |
| _**Operational user**_ |String | 5-50 | Not | Reference to existed and validated row in Driver table. | Not available | Operational user to evaluate the request |||| Integer. Foreign key in other table. | Not available |
| _**Start apply**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime of start de operation in vehicle. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Finish apply**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime of finish de operation in vehicle. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Cost of usage**_ | Decimal number | 2 decimals and 1-15 integer. | Yes | | Null | Cost of usa the vehicle by drivers. | 0.00 | 999999999999999.99 | | Double precision | No available |
| _**Status of finish operation**_ |Option | 1 | Not | Choose one of value list | Not available | Status of shipment after applied all change.||| `Repairing`,`Repaired`, `Available`, `Unavailable` and `Using by driver`.` |String | Status of shipment|
| _**Cost of repair**_ | Decimal number | 2 decimals and 1-15 integer. | Yes | | Null | Cost of repairs the vehicle by drivers. | 0.00 | 999999999999999.99 | | Double precision | No available |
| _**Datetime of paid repair**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime Indicate when driver pay all  repairs. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Response**_ |Option | 1 | Yes | If it's not null, the "Reason of response" field must not be null too. Choose one from the value list. | Null| Indicate if accept or reject the request. ||| `Accepted`,`Rejected` | String | Not available|
| _**Reason of response**_ | Text | 20-300 | Yes | If it's not null, the "Response" field must not be null too.|Null| Reason to choose the response |||| String | Not available |
| _**Assigned vehicle**_ | String | 15 | Yes | If the "Response" field is "Accepted", it must not be null | Null | Assigned vehicle to driver. |||| Integer. Foreign key to other table | List of our vehicle |

Nota: driver, operational user, vehicle

#### Historial of warehouse in moving vehicle

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Response**_ |Option | 1 | Yes | If it's not null, the "Reason of response" field must not be null too. Choose one from the value list. | Null| Indicate if accept or reject the request. ||| `Accepted`,`Rejected` | String | Not available|
| _**Reason of response**_ | Text | 20-300 | Yes | If it's not null, the "Response" field must not be null too.|Null| Reason to choose the response |||| String | Not available |
| _**Operational user**_ |String | 5-50 | Not | Reference to existed and validated row in Driver table. | Not available | Operational user to evaluate the request |||| Integer. Foreign key in other table. | Not available |
| _**Vehicle**_ | String | 15 | Yes | If the "Response" field is "Accepted", it must not be null | Null | Vehicle will move. |||| Integer. Foreign key to other table | List of our vehicle |
| _**Type operation**_ | Option | 1 | Not | Never be null. | Not available | Type of operation to move a vehicle. ||| `Get in`,`Get out` | String | Operation of move |
| _**Destiny warehouse**_ | Option | 1 | Not | Never be null. Choose one of the list of warehouse. Don't be same value of "Start warehouse" field | Not available | warehouse receive request. |||| Integer. Foreign key of  table | List of warehouse |
| _**Origin warehouse**_ |Option | 1 | Not | Never be null. Choose one of the list of warehouse. Don't be same value of "Destiny warehouse" field | Not available | warehouse send request. |||| Integer. Foreign key of  table | List of warehouse |
| _**Creation**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Code**_| String | 14 | Not | First 3 characters, and rest of number. It need to be unique inside internal request. | Not available | code for easy recognition of internal request. |||| String | Not available |

Nota: warehouse, vehicle, operational user

#### Historial of warehouse in moving shipment

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Response**_ |Option | 1 | Yes | If it's not null, the "Reason of response" field must not be null too. Choose one from the value list. | Null| Indicate if accept or reject the request. ||| `Accepted`,`Rejected` | String | Not available|
| _**Reason of response**_ | Text | 20-300 | Yes | If it's not null, the "Response" field must not be null too.|Null| Reason to choose the response |||| String | Not available |
| _**Operational user**_ |String | 5-50 | Not | Reference to existed and validated row in Driver table. | Not available | Operational user to evaluate the request |||| Integer. Foreign key in other table. | Not available |
| _**Shipment**_ | 14 | 1 | Not | Associated to any row in shipment table. | Not available | Shipment will operate. |||| Integer. Foreign Key in table. | Shipment |
| _**Type operation**_ |  Option | 1 | Not | Never be null. | Not available | Type of operation to move a shipment. ||| `Get in`,`Get out` | String | Operation of move |
| _**Destiny warehouse**_ |Option | 1 | Not | Never be null. Choose one of the list of warehouse. Don't be same value of "Start warehouse" field | Not available | warehouse receive request. |||| Integer. Foreign key of  table | List of warehouse |
| _**Origin warehouse**_ |Option | 1 | Not | Never be null. Choose one of the list of warehouse. Don't be same value of "Destiny warehouse" field | Not available | warehouse send request. |||| Integer. Foreign key of  table | List of warehouse |
| _**Creation**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Code**_| String | 14 | Not | First 3 characters, and rest of number. It need to be unique inside internal request. | Not available | code for easy recognition of internal request. |||| String | Not available |


Nota: warehouse, shipment, operational user

#### Historial of driver

| Atribute | Generic type | Length/Format | Accept null | Check conditions | Default | Description | Min value | Max value | Value list | Physical data type | Unit |
|----------|--------------|--------|-------------|------------------|---------|-------------|-----------|-----------|------------|--------------------|-------|
| _**Creation**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime to create this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Start apply**_ |datetime | YYYY/MM/DD HH:MM:SS | Not | All value based in gregorian calendar. timezone with UTC-0.|| Datetime of start this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Finish apply**_ |datetime | YYYY/MM/DD HH:MM:SS | Yes | All value based in gregorian calendar. timezone with UTC-0.| Null| Datetime of finish this register. |||| Timestamp with timezone UTF-0 | gregorian calendar |
| _**Response**_ |Option | 1 | Yes | If it's not null, the "Reason of response" field must not be null too. Choose one from the value list. | Null| Indicate if accept or reject the request. ||| `Accepted`,`Rejected` | String | Not available|
| _**Reason of response**_ |Text | 20-300 | Yes | If it's not null, the "Response" field must not be null too.|Null| Reason to choose the response |||| String | Not available |
| _**Operational user**_ |String | 5-50 | Not | Reference to existed and validated row in Driver table. | Not available | Operational user to evaluate the request |||| Integer. Foreign key in other table. | Not available |
| _**Service**_ | Options | 1 | Not | Associated to Service available to drivers | Not available | Service the driver will use. |||| Integer. Foreign key in other table. | Service of drivers | 
| _**Driver**_ | String | 5-50 | Not | Reference to existed and validated row in Driver table. | Not available | Register historial event of driver. |||| Integer. Foreign key in other table. | Not available |


Nota: driver, service, operational user

### _Conceptual View of the business_

The purpose of these images is to explain in high level what entities will be to know, how they relationship between them and explain the main process in high level with details, but all it focus in business level. I would like to show it separated in kind of service.

#### Order based service

![operational entities based in order service](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20Conceptual%20View%20of%20the%20business%20-%20order%20based%20service.png?raw=true)

#### Resource based service

![operational entities based in resource service](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20Conceptual%20View%20of%20the%20business%20-%20resource%20based%20service.png?raw=true)

#### Database focus

![Conceptual view of data from database based in relationship entities](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20conceptual%20view%20data%20model%20_%20general.png?raw=true)

#### Note:
* Both image share several entities but the relationship that they are using not same. That's based in focus of service they use, so that's a reason to separate to easy the understanding the conceptual views.
* I don't explain the some situation like error and unreception of order; i will explain it in process diagrams in details.
* The processes will explain in details in others diagrams.
* The main items are entities will need to know in all others diagrams.

### _Use cases of system_

![Use case in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20use%20cases%20diagram.png?raw?true)

we can see the three main actors: the drivers, clients and operational users. They can use differents focus services of systems:

* Management resource (operational users)
* Management Orders (client, drivers and operational users)
* Management Incidents (drivers, and opeational users)
* Notifications (drivers, clients & operational users)
* Management Routes (operationals user and drivers)
* Liquidations of Routes (operational users and drivers)


### _Workflow process_

There are many process in this operational area, we will focus in basic operational process what all operational user will use.

#### _Create a manually validated order by opt-user_

In this process, the operational user can be have shipment edition role.

![Use case in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20create%20validated%20order%20by%20manual.png)

#### _Create a validated order by API_

In this process, the operational user can be have shipment edition role.

![Use case in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20create%20validated%20order.png)

#### _Create a route_

In this process, the operational user can be have route creation role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20create%20route.png)

#### _Assign an offered route_

In this process, the operational user can be have route assignation role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo-%20assign%20offered%20route%20to%20driver.png)

#### _Assign an offered route_

In this process, the operational user can be have route assignation role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20assign%20a%20assigned%20route%20to%20driver.png)

#### _Execute a route_

In this process, the operational user can be have route close role and route solution role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo-%20execute%20a%20route.png)

#### _Evaluate request of client about resource_

In this process, the operational user can be have resources assigner role and resource approved request role. It applied to all kind of resources (warehouse, drivers and vehicle).

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20Evaluate%20request%20of%20client%20about%20resource.png)

#### _Execute client request_

In this process, the operational user can be have resource guard role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20execution%20of%20client%20request.png)

#### _Evalute request of internal moving_

In this process, the operational user can be have resources assigner role and resource approved request role. It applied to all kind of resources (shipment of vehicle).

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20Evalute%20request%20of%20internal%20moving.png)

#### _Execute internal request_

In this process, the operational user can be have moving resource monitoring role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20execution%20of%20internal%20request.png)

#### _Transfer order to other route_

In this process, the operation user can be have a transfer route role and approved transfering order role. All orders must be given independently of status.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20Transfer%20order%20to%20other%20route.png)

#### _Change of service to driver_

In this process, the operation user can be have a change service driver role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20change%20service%20of%20driver.png)

#### _Driver requests vehicle to ours_

In this process, the operation user can be have a renting vehicle to driver role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20use%20corporate%20vehicle%20by%20driver.png)


#### _Execution of renting vehicle to drive_

In this process, the operation user can be have a renting vehicle monitoring role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20execution%20of%20renting%20vehicle.png)

#### _Register new drivers_

In this process, the operation user can be have a evaluate driver request and creation driver role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20register%20a%20new%20driver.png)

#### _Fire a drivers_

In this process, the operation user can be have a fire driver and liquidate personal role.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20fire%20a%20driver.png)


#### _Register new resource_

In this process, the operation user can be have monitoring resource and creater resource role. Only warehouse and vehicle like resource.

![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20register%20new%20resource.png)
 
 
#### _Createa new service_
 
In this process, the operation user can be have service editor role.
 
![Use cas in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo-%20create%20new%20service.png)

#### _Register new city to operate_

In this process, the operation user can be have opertional setup role. This applies to country too.

![Use case in mandalo](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20Createa%20new%20city.png)

### _Data workflow process_

i drawn all integrated view of data workflow process based in all process.

![Main](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/document_all_process_in_operational_area/info/Mandalo%20-%20main%20data%20flow%20view.png)
