# Case of study and work: 

## Purpose and warning

I will create a hypothetical case about a logistics company and its business model. This is based on my personal experience within the area, and it is not a specific case of any company that I worked for or currently work for.

The purpose is to create a context to use it to create a case of build tools, models and analysts in my portfolio projects.


## List of portfolio cases

This is my portfolio projects i built it based in this case.

| N° of Case | Title | Short description | Topics | skills | Input | Outputs | Status |
|------------|-------|-------------------|--------|--------|-------|---------|--------|
| 1 | Document all process in business: operational area. | Understand and document processes of operational area. | `Understanding business` | `Documents`, `Process Diagrams`, `Data flow Diagrams`, `Organization` | Readme of project. | Use case diagram, sequence diagram, Activity diagram  | `Finished` |
| 2 | Data modeling in operational area: logical focus to operational activities | Modeling data in logical based  all requirements to case 1°. | `Understanding business`, `Data modeling` | `Logical data model`, `Documents`, `Understanding of business` | All documents in case 1° | logical data model | `Finished` |
| 3 | Data modeling in operational area: Physical  focus to operational activities| Modeling data in Physical focus based  all requirements to case 1° and 2°. Result is operational focus. | `Understanding business`, `Data modeling` | `Physical data model`, `Documents`, `Understanding of business`, `Operational activities` | All documents in case 1° and 2° | Physical data model | `Finished` |
| 4 | Implement a physical data model of operational area. | Create all scripts need to implement a database to work in operational area. | `Database` |  `Database`, `Postgresql` |  All documents in case 3° | Scripts implements all tables | `Finished` |
| 5 | Data modeling in operational area: Inmon analytical logical design | Design a logical data model to support analytic operations in startups. This is based in Inmon model focus. | `Data warehouse modeling`, `Logical data modeling` | `Inmon Data warehouse modeling`, `Logical data modeling` | Case 1, 2 | A logical data model based in Inmon data warehouse focus. | `Finished` |
| 6 | Data modeling in operational area: Inmon analytical Physical design | Design a physical data model to support analytic operations in startups. This is based in Inmon model focus. | `Data warehouse modeling`, `Physical data modeling` | `Inmon Data warehouse modeling`, `Physical data modeling` | Case 5 | A physical data model based in Inmon data warehouse focus. | `Finished` |
| 7 | Data modeling in operational area: Inmon analytical Physical implement | Implement a physical data model to support analytic operations in startups. This is based in Inmon model focus. | `Relational database`, `SQL` | `Postgresql`, `SQL` | Case 6 | Get several SQL script to implement a data warehouse data model. | `Finished` |
| 8 | Data modeling in operational area: kimball analytical logical design | Design a logical data model to support analytic operations in startups. This is based in Kimball model focus. | `Data warehouse modeling`, `Logical data modeling` | `Kimball Data warehouse modeling`, `Logical data modeling` | Case 1, 2 | A logical data model based in kimball data warehouse focus. | `Progress` |
| 9 | Data modeling in operational area: kimball analytical Physical design | Design a physical data model to support analytic operations in startups. This is based in Kimball model focus. | `Data warehouse modeling`, `Physical data modeling` | `Kimball Data warehouse modeling`, `Physical data modeling` | Case 5 | A physical data model based in kimball data warehouse focus. | `Ready to start` |
| 10 | Data modeling in operational area: kimball analytical Physical implement | Implement a physical data model to support analytic operations in startups. This is based in Kimball model focus. | `Relational database`, `SQL` | `Postgresql`, `SQL` | Case 6 | Get several SQL script to implement a data warehouse data model. | `Ready to start` |
| 11 | Document all process in business: financial area | Understand and document processes of financial area. | `Understanding business` | `Documents`, `Process Diagrams`, `Data flow Diagrams`, `Organization` | Readme of project. | Use case diagram, sequence diagram, Activity diagram  | `Ready to start` |


## Study case: "mandalo"

## Operational Area

### General description

The "mandalo" is a peruvian project to want to be a startup and the next unicorn in latam. This project is based in logistics and want to get impact in 3 parts of supply chain:

- __First mile__: product will travel from factory to warehouse or distribution center of our specified client.
- __Middle mile__: product will travel from distribution center or warehouse of client to the individual retail store of our clients.
- __Last mile__: product will travel from individual retail store of our clients to end user of our clients.

We using technology and infrastructure, connect clients with drivers in his free time they want to get more money to deliver orders; This delivery apply all part of the supply chain of our clients by our drivers want to work. Each part of the supply chain, they implement several kind of service to support the difference needs of clients:
 
##### Order-based service

Services focus in the management of operation in order based in time. Each order has a dead line timestamp based in kind of services that it's created in the system.

* __Scheduled__: The client notify what timestamps the orders will need to pick it up and what deadline need to delivery it. Client will notify 24 hours in advance. Its work included on Sundays or holidays.
* __Rush__: Any orders created in any days of week; independently it's created in sundays or holidays; have a deadline at least 1 hrs more the that was created.
* __Express__: The orders has a range of time; it's less or equal than 3 hrs and higher or equal than 1 hr; to deliver a end users. Don't included in sundays or holidays.
* __Same day__: Any orders created before 10AM, have 23:59PM at same day to deliver a end users. Don't included on sundays or holidays.
* __Next day__: Any orders created before 4PM, have 23:59PM at the next day to deliver a end users. The next day can't be on sundays or holidays.

##### Resources-based service

Services focus in the management of our resources when we are outsourcing by clients. The resources we have are Warehouses, drivers, vehicles and system.

* __Dedicated__: Drivers works us a full time dedicated to specified city.
* __Asigned__: The client notify what range of time they need to use our drivers to operate their routes.
* __Warehousing__: The client notify what range of time they need to use our warehouses to store temporaly products.
* __Moving__: The client notify what range of time they need to use our corporatived vehicles to they operate it.

We have an investment of 2.5 millones of soles! and they planning to stay in 5 main cities: Arequipa, Lima, Cusco, Trujillo and Tacna to start the nation level operation.

### Services in details
 
i will explain all previoues listed service in details.

The __Scheduled__ service; the client needs to deliver their order but not now, so they notify us the timestamp to pick up and deadline to deliver their order. This notification need to sent 24hrs in advance. It works all day of week and holidays. The interval of created and deliveried timestamp can be between 1hr into 2 days. This service can use our warehouse to store it temporally. it's available in vehicle: van, moto, convoy and can.

The __Rush__ service; the client rushes to deliver their order with deadline between 1hr to 3hrs in all moment and time of the week; included holidays after it's requested. it's available in vehicle: van, moto and car.

The __Express__ service;  the client rushes to deliver their order with deadline between 1hr to 3hrs in all moment and time of the weekdays after it's requested. if order is requested with deadline on sunday and holiday, it costs 20% plus; it's available in vehicle: van, moto and car.

The __Same day__ service; the client need to deliver their order in same day (max. 23:59PM) that it was requested. The requested order need to send before 10AM to validate the request. otherwise, it's denied. This service can use our warehouse to store it temporally. It's available in these vehicle: moto, van, car.

The __Next day__ service; the client need to deliver their order in next day (max. 23:59PM) that it was requested. The requested order need to send before 4PM to validate the request; otherwise, it's denied. This service can use our warehouse to store it temporally. It's available in these vehicle: moto, van, car and convoy.

The __Freelo__ service; he can work in any time or day depende his free time, so  the driver can accept route or not. this is default service to all drivers.

The __Dedicated__ service; some drivers works to us a full time and the exclusived way. They can't work in asigned service and dedicated in specified city. The full time is 8hrs, included holidays and sundays.

The __Asigned__ service; The client needs to get drivers to operate their routes, so they request us a amount of drivers and what range of time they will operate with their; then we sent them the amount of drivers will participate. If client accepts our notification; our drivers work in that period of time, and it finished the client will send us a all routes operated in this period to register it. The notify need to send 24hrs berfore the operation.

The __Warehousing__ service; the client need to store some orders, so they notify us they will use any our warehouse in specified citiy; if we accept it, we will separate space in the selected warehouse in that period of time, and then we notify the location of data warehouse in city, the cost of period and penalties of cost if the client don't comply the contract. The client can request a specified warehouse too.

The __Moving__ service; the client need to move some orders from specified location to destination location, so they notify us they need to use our convoy to move. If we accept it, we contract them, the contract focus on range of time, penalties in non-compliance and damage to the vehicle. The locations need to be any of operating cities. The vehicle available is convoy.


### Organization and roles

![Organization, service and roles](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/Logistic/info/diagrama%20de%20operaciones%20mandalo.drawio.png?raw=true)

All services are clustered my vertical, all vertical focus in specified topic; and All vertical are created in operational strategy.

The operational strategy is defined by operational regional manager, so they create strategies to operate on multi-regional level, each strategies is the base to create one specified vertical. the vertical is managed by vertical regional manager, they create, modify and evaluate the high level tactical plan (services) derived from strategy, then they implement it in him asigned region. the vertical regional manager assign each region a vertical manager to monitoring, and evaluate the work plan  in his region and modify it based in feature of region. Each region, the vertical manager has an operational team, this team is made up of an operator works in  daily operational task and operator leader to guide them in their work.

