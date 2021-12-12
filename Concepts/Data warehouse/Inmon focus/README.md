# Data warehouse based in Inmon focus

======================================

## Purpose
Contain all concepts, best practices, patterns, architectures and concepts about data warehouse i learned based in Inmon focus.


## Index of readme
This is a index to best navigation inside document.

- [External data in data warehouse](#external-data-in-data-warehouse)
  - [The problems of external data sources: unified storage of data](#the-problems-of-external-data-sources)
  - [Modeling, storing and metadata about external data in data warehouse](#modeling-storing-metadata-of-external-data-in-data-warehouse)
- [Architecture in Data Warehouse](#arquitecture-in-data-warehouse)
  - [Inmon model](#inmon-model)
    - [Diagram of enviroment](#diagram-of-enviroment-in-inmon)
    - [Integrations between levels](#integrations-between-levels-in-inmon)
    - [Development life cycle](#development-life-cycle-in-inmon)
    - [Important aspects of the desing](#important-aspects-of-the-desing-in-immon)
    - [Process models in enviroment](#process-models-in-enviroment-in-inmon)
    - [Data models in enviroment](#data-models-in-enviroment-in-inmon)
      - [High level of data model](#high-level-of-data-model-in-inmon)
      - [Middle level of data model](#middle-level-of-data-model)
      - [Low level of data model](#low-level-of-data-model)
    - [Work Units: Snapshot and Profile Records](#snapshot-and-profile-records-in-inmon)
    - [Interaction between operational and data warehouse enviroment  in access of data](#interaction-between-operational-and-data-warehouse-enviroment-in-access-of-data)
    - [Distributed architecture models](#distributed-architecture-models)
      - [Global data warehouse model](#global-data-warehouse-model)
      - [Technologically distributed data warehouse model](#technologically-distributed-data-warehouse-model)
      - [Independently evolving distributed data warehouse model](#independently-evolving-distributed-data-warehouse-model)
- [Requirements of technology](#requirements-of-technology)
  - [Main features needed to support data warehouse](#main-features-needed-to-support-data-warehouse)
  - [Difference transactional database and data warehouse enviroment](#difference-transactional-database-and-data-warehouse-enviroment)
  - [Multidimensional DBMS and data warehouse](#multidimensional-dbms-and-data-warehouse)
- [Solutions](#solutions)
  - [Techniques to scanning data in operational-datawarehouse extract process](#techniques-to-scanning-data-in-operational-datawarehouse-extract-process)
  - [Alternatived techniques to design data warehouse](#alternatived-techniques-to-design-data-warehouse)
    - [Dual level of granularity: manage granularity and access the data](#Dual-levels-of-granularity)
    - [Living sample database](#living-sample-database)
  - [Techniques of enhanced performance in data model](#techniques-of-enhanced-performance-in-data-model)
  - [Techniques to control refreshed data from operational enviroment](#techniques-to-control-refreshed-data-from-operational-enviroment)
  - [Consideration in types of development efforts in distributed data warehouse](#consideration-in-types-of-development-efforts-in-distributed-data-warehouse)
    - [Completely unrelated data warehouses](#completely-unrelated-data-warehouses)
    - [Distributed Data Warehouse Development](#distributed-data-warehouse-development)
    - [Building the warehouse on multiple levels](#building-the-warehouse-on-multiple-levels)
    - [Multiple Groups Building the Current Level of Detail](#multiple-groups-building-the-current-level-of-detail)
  - [Inverted Data warehouse: Alternative to storage management](#inverted-data-warehouse-alternative-focus)
- [Migration to the architected enviroment](#migration-to-the-architected-enviroment)
  - [A migration Plan](#a-migration-plan)
  - [Data driven and spiral methodologies](#data-driven-and-spiral-methodologies)
- [Unstructed data in data warehouse](#unstructed-data-in-data-warehouse)
  - [Integrating the 2 worlds](#integrating-the-2-worlds)
  - [Infrastructure of integration of data](#infrastructure-of-integration-of-data)
  - [Structure and topics of data warehouse for unstructured data](#structure-and-topics-of-data-warehouse-for-unstructured-data)
- [Relational and dimensional model for database design](#relational-and-dimensional-model-for-database-design)
  - [Dimensional or relational models](#dimensional-or-relational-models)
  - [Differences between the Models](#differences-between-the-models)
  - [Data Marts types: independent or dependent](#data-marts-types)
- [Large Data warehouse](#large-data-warehouse)
  - [Impact of large data warehouse](#impact-of-large-data-warehouse)
  - [Disk storage in usage of data](#disk-storage-in-usage-of-data)
  - [Moving data from enviroment to another](#moving-data-from-enviroment-to-another)
  - [Maximum capacity](#maximum-capacity)
- [The life cycle of data](#the-life-cycle-of-data)
- [Testing and the data warehouse](#testing-and-the-data-warehouse)
- [References](#references)

# External data in data warehouse
 whole host of other data is of legitimate use to a corporation that is not
generated from the corporatio's own systems. This class of data is called external data and usually enters the corporation in an unpredictable format.

There are 2 types of external data:
1. Records of external data collected by some source (such as a drug store,
a supermarket, and so forth).
2. External data from random reports, articles, and other sources. 


##  The problems of external data sources
You wanna extract data of external sources to analyze them to get insight/knowledge. The extract process is good for 2 reason:
* don't degrade the performance of the source system when you need to analyze in mass.
* control this data because you move this data into your system.

But you will have a problem if you don't structure a unified infraestructure to store this data:
![alt text](image/ExtractDataFromExternalProblem.png?raw=true)

Based in above image, we have 3 problems in this bad infraestructure:
* **Lack of credibility**: if 2 departments generate a report same focus, it's possibly both are difference in results, because both use difference data source in their report. there are some reason associated:
  * Change data continually in all sources.
  * Sources can have difference type of data.
  * Don't share sources in all department.
  * When you extract data of external, i need to capture of identity source to accredit those data.
* **Productivity low**: it's so hard to access and processing several sources in diference locations inside organization.
* **From data to information**: it's so hard to reconciliate and normalize structure of data from several different sources to generate a column in report.

## Modeling storing metadata of external data in data warehouse

The metadata is critical to manage and store external data by this is use to access and control it in data warehouse enviroment, feature like id of document, date of entry into enviroment, source of the document, date of source of the document, description of the document, classification of document, index words, related references, purge date and others are part to the looking of manager of metadata to control those data.

If it's convenient and cost-efficient to do, the external data will store in data warehouse but usually this data is stored in secondary storage like fiche or magnetic tape while a entry of this document of external data is stored in metadata of the warehouse describing where the document can be found. The implication is that once the data is captured and managed centrally, the organization has to undergo the expense of dealing with such data only once.

![Storing external data inside data warehouse enviroment](image/metadataStoringOfExternalData.png?raw=true)

Maybe appears  that  there  is  very  little  relationship between the data model and external data by external  data  is  not  malleable  to any  extent  at  all when he is creating the data modeling. Attempting to use the data model for any serious reshaping of the external data is a mistake. About the best that can be done is to note the differences between the data model and external data as far as the interpretation of key phrases and words are concerned. The most that
can be done is to create subsets of the data that are compatible with the existing internal data

# Arquitecture in Data Warehouse
There are 2 common models to implement data warehouse in enterprised world: Inmon and Kimball. Those are considered parents of data warehouse and define severel attributes, process and practices to implement it.



## Inmon model
### Diagram of enviroment in Inmon

![Diagram of arquitecture of data warehouse in Inmon model](image/ArchitectureLevelInmon.png?raw=true)

As shown in the diagram, there are 4 level in model:
* **Operational level**: this level contains the most detailed, current and application-oriented data in organization. it's generated by systems of organization and others users.
* **data warehouse level**: this level contains most integral, subject-oriented, historical/time variant and non-overlapping data in organization. All change in data in operational layer, will create a new records inside data warehouse layer.
* **data mart level**: this level contains specified subject-oriented, and different granular data. it contains some summarized and details data for a specified department, and can be denormalized and shaped by the operating requirements of a single department.
* **individual level**: this is temporary and small data passed by heuristic. it supported by the PC.



## Integrations between levels in inmon

You need to garantize the integral data of data warehouse level from operational level because this is core of enviroment and next levels depend it. This is hard by complex, time-consuming process to access several operational data sources to generate a integral data. `You must need a ETL focus program can automate this tedious process and only mantain this program`. From granular data focus, this model based top-down focus to implement the management of data.

![Integration from operationa level to data warehouse level](image/ETLProcesssOperationalDatawarehouseLevel.png?raw=true)
 
In case of integration of operational - data warehouse level, there are some problem you need to confront with data and its sources:
1.  Normalize data in its name, metrics to apply and value to shows to integrate in data warehouse. (integration problem)
2.  Different formats under many different DBMSs. This trasnlations of technology could be hard. (integration problem)
3.  The efficiency of accessing from operational system. This can impact in performance of warehouse and implementations of requirements. (performance problem)
4.  The operational data must undergo a time-basis shift as it passes into the data warehouse. A important shift in the modes de processing surrounding the data is necesary. (processing design problem).
5.  When passing data is the need to manage the volumen of data that resides in and passes into the data warehouse. You must be condensed both at the moment of extraction and as it arrives at the data warehouse. (Volumen of data problem)
 
In general, all level in architecture using ETL program to passing data between them. The complex of programm depending from requirement of level but it's so easy comparing with ETL process between operational-datawarehouse level.



## Development life cycle in inmon
To build the functionality of system, you need to understand the methodology to evaluate and building system based in end user will use it. In classic software development, you need the requirements to define capacity of software; but you'll build this system you need to start of data!.

This focus is called data-driven development and the phrase "Give me what I say I want, and then I can tell you what I really want" can summary all life cycle you will be implementing. This focus is a spiral development methodology.

Those are the steps to use the methodology:
1. Get a datasets to work.
2. Integrate of all data inside data warehouse.
3. Test it to see what bias there is to the data, if any.
4. Write the program against the data and analyze it.
5. Undestand requirements of system.
6. Adjustment of the design of system and start the cycle from new dataset data inside warehouse.

In general, build a level of enviroment is a end users needing based process which it's a long time . Remember the data warehouse are not built all at once. Instead they are designed and populated a step at a time. While the data warehouse is populated with several subjects, you will need to best the performance, then i need to create a next level: data mart level. This phenomenon is named "the 1 day to n day".

![The 1 day to n day process](image/developmentCycleLifeInmon.png?raw=true)

The critical resource to get a good process is the data model. Not only does the data model tell what needs to be done, also it suggests how any one development effort will be integrated with any other development effort. Remember: the data warehouse serves as a roadmap for each of the development efforts, and data model produces a cohesive and tightly orchaestrated whole to achieve long-term integration and harmonious effort in the incremental and iterative development.


## Important aspects of the desing in immon
When you design of data warehouse you need to note some the following crucial aspects; if you ignored it, you will hard to modify and get a poor performance in the environment.

### Granularity
This is a level of details or summarization of the units of data in the data warehouse. The more detail there is, the lower the level of granularity.  The less detail there is, the higher the level of granularity. 

In almost all cases, data comes into the data warehouse at too high a level of granularity. This means that the developer must spend a lot of design and development resources breaking the data apart before it can be stored in the
data warehouse.

The granularity impact following issues:

1.  The high of level in granularity means lowest storage capacity for data and the low of level in granularity means highest storage capacity for data.
2.  More storage capacity, you need more capacity to process it.

![Granularity in data warehouse](image/GranularityInmon.png?raw=true)

Those are the benefits of granularity:

1. **Reausability of data**: The granular data found in the data warehouse is the key to use by many people in different ways.
2. **reconciliation of data**: When same data is used in different ways,if you need to reconciliate the data, it's so easy.
3. **Flexibility to query**: Depending of the granular data, can you answer all o a subset of query.
4. **Get all history events**: it contains all historical events in company. And the level of granularity is detailed enough that the data can be reshaped across the corporation for many different needs.
5. **Fast solution to unknown requirements**: When new requirements of knowledge need by the company, the granularity of data must support those requirements.

### Partition
The breakup of data into separate physical units that can be handled independently. This feature to add flexibility to manage data from physical unis.

Following are some of the tasks that cannot easily be performad when data resides in large physical units: restructuring, indexing, reorganization, recovery, monitoring and sequential scanning. The partition can benefit the data warehouse by loading, accessing archiving, deleting, monitoring and storing data. 

![partitions of data warehouse](image/PartitionInmon.png?raw=true)

The matter inside feature is how it should be done rather whether it should be done. The choices for partitioning data are strictly up to the developer. In the datawarehouse environment, however, it is almost mandatory that one of the criteria for partitioning be by date.

Partitioning can be done in 2 levels:
* **System**: it is a function of the DBMS and the operating system to some extent.
* **Application**: it is done by application code and is solely and strictly controlled by the developer, so the DBMS and the system know of no relation between one partition and the other.

The best option is application level for some reasons:

1.  There can be a different definition of data by each partition.
2.  Data can be moved from one processing complex to another with impunity.

## Process models in enviroment in inmon
The data designer must undestand the applicability and the limitations of those techniques. Process model is used process in organizetion. Process model applies only to the operational level.

![process adn data modeling in enviroment](image/procesModelingInInmon.png?raw=true)

There are many contexts and environments in which a process models is invaluable; for example, when you buildin the data mart level. However, `the process model assumes that a set of known processing requirements exists a priori; such an assupmption can be made but those assumptions do not hold for the data warehouse level`.

## Data models in enviroment in inmon
The data models is representations of entity in real world inside system. data model is applicable to both the existing systems enviroment and the data warehouse enviroment. There are 3 level to implementation of data model.

The data model applied in operational level passed following process: this model represents only primitive data, performance factor are added into it and it's transported to operational level with few changes. but the data model applied in data warehouse level is: removed operational only focus fields in model; enhace to model with time field, if they don't already have one; derived  data  is  added  to  the  corporate  data  model  where  the derived data is publicly used and calculated once, not repeatedly. Finally, data relationships in the operational environment are turned into “artifacts” of the relationship in the data warehouse.

The final design activity in data models to the data warehouse data model is stability analysis. `The stability analysis involves grouping aatributes of data together based on their propensity for change`. 

### High level of data model in inmon
Also name "entity-relation diagram" o ERD. In this level, you will modeling features entities and relationships using a UML o ERD.

The data model need to define the scope of integration to determinate what data can be or can't be inside the model before to modeling processes. It need to be written in language understable to the business person.

![Generate a coporated ERD of organization](image/createCorporateERDFromDifferentUser.png?raw=true)

The recommendation is created ERD per user of different areas across the corporation, to merge those into the single and corporated ERD represents the organization.

### Middle level of data model
For each major subject area; or entity; identified in high level data model, a midlevel mode is created. This model is gradually expanded part by part. This model use 4 basic constructs to build:
1.  `Primary grouping`: it exists once and only once for each subject area, it holds attributes that exists only once for each major area.
2.  `Secondary grouping`: it holnd data attributes that can exist multiple times for each major subject area.
3.  `Connector`: it relates data from one grouping to another. Generally use a foreign key. and represents a relationship in ERD.
4.  `Type of `: this data is indicated by a line leading to the right of a subtype of data.

![Diagram of middle level of data model](image/MiddleLevelOfDataModel.png?raw=true)

### Low level of data model
Also named the physical data model, It is created from midlevel data model merely by extending it to include keys and physical characteristics of the model, to looks like a series of relational tables.

![Mapping Middle level to low level of data model](image/lowLevelOfDataModel.png?raw=true)

Issues like partitions, granularity, I/O performance of storage-compute are relevant in this level.


## Snapshot and Profile records in inmon

### Snapshot
All types of data warehouse around a structure of data called a snapshot. The snapshots are created as a result of some event occuring. A event is the recording of information about a discrete activity, and types of event: predictable by scheduled time and random by operational activity. When there is a one-to-one correspondence between the activities in the operational environment and the snapshots in the data warehouse, the data warehouse tracks the history of all the activity relating to a subject area.

The snapshot has a following components:
1.  **Key**: it can be unique or nonunique. the key is a composite made up of many elements of data that serve to identify the primary data but it can be a single of element of data. `it use to identify the record and the primary data`.
2.  **Unit Time**: The unit of time when the event being described by the snapshot has occurred. Occasionally, the unit of time refers to the moment when the capture of data takes place.
3.  **Primary data**: it is data relates directly to the key of the record inside snapshot.
4.  **Secondary data**: it is optional. this is data offers other extraneous information captured at the momento when the snapshot was created. if this data sources from other table, you would get a inferred relationship between primary and secondary data, this type of occurences is named artifact.

### Profile records
There are cases in which data does not meet the criteria of stability and infrequency of change, a massive volumes of data, changes data frequently or not business need for meticulous historical details of data. When one or more of theses conditions prevail, you need to use profile records.

A profile records groups many different, detailed occurrences of operational data into a single record and represents the many operational records in aggregation. it is created by events too. The ways to aggregate those records inside profile record depending of developer and its affect the case of usage to analyze and accesss of profile records.

You can created multiple profile records with several focus of analysis. Usually create the profile record involves sorting and merging data. Passing profile records to other level of enviroment require a customize this records.


## Interaction between operational and data warehouse enviroment in access of data

Its natural passing data from operation enviroment to data warehouse enviroment; but in occasion is good passing data from the data warehouse to operational enviroment but it's a not natural flow of process.

A direct access of data warehouse data is limited by constraint of data warehouse: time responde of request to use in operation enviroment; compatible communication in technology level in operational and data warehouse enviroment: protocols, capacity, formatting and so on; minimal amount of data in request. In general, it's not good choice this type of access.

A undirect acces of data warehouse data is efficient focus: the data warehouse is analyzed periodically by a program that examines relevant and criteria, then creates a small file in the online enviroment that contains succinct information about the business of the enterprise. this file is used quickly and efficiently in criterias of operational enviroment.

![Pattern of undirect access data of data warehouse from operation enviroment](image/undirectAccessOfDataInDataWarehouse.png?raw=true)


## Distributed architecture models

There are 3 types of distributed data warehouse model based in focus of architecture:

### Global data warehouse model

`In case you need to store information locally and globally data; use this focus`. This method consistent in 2 parts: a local data warehouse to store and manage data in local level ;like region sede in example; and global data warehouse to store and manage a global level; Like a corporation finance operations in example. Others example is there are geographically or distributed business distributed data warehouse makes sense.

![Architecture of operation in Global/Local distributed data warehouse](image/GlobalLocalDistributedDWH.png?raw=true)

The local data warehouse is autonomous to operate with its data and enhancement this architecture enviroment, everything without coordination any another local data warehouse. Only on occasion and for certain type of processing will data be sent to the global data warehouse. If there are intersection/commonality of data between local data warehouses is coincidental by there are not common structure or processing its data with coordination.

The global data warehouse's scope is the business that is integrated across the corporation, so that depending case it will be massive or a little integrated data. it contains historical data, as do the local data warehouses. In some cases a direct update can go into global data warehouse. if there are intersection of data between local sites, it is best contained in a global data warehouse by local data warehouse need to support to store data to fed the global data warehouse.

A important thing in this method is the mapping of data from local data warehouse to global data warehouse. this determines which data goes into the global data warehouse, the structure of the data, definitions and identification of common corporate data and any conversion that must be done. it will be different for each implementation in local data warehouse and depending of local developer/designer, this local mapping will be improves over the time to solidicate the global mapping. Remember: `the global mapping is more about corporation needs rather the local mapping is more local and specified in site.`

![Example of Global data warehouse staging in local data warehouse](image/GlobalDataWarehouseStaging.png?raw=true)

A variation of the local/global data warehouse structure is to allow a global data warehouse staging area to be kept at the local level, to support storing data will be moving the global data warehouse to achieve the mapping. 

How transfering data between global and local data warehouse is a complex issue by you need to meet legal, security, functional and technical requirements between the parties to achieve.

The issue of access of data is matter in this method. Depending what is being asked for and how to require in process, this may or may not be appropiate use data of global data warehouse from local data warehouse; but the general principle is the same: local data should be used locally and global data should be used globally. 

The issue of routing of requests for information into the architected environment is a complex in this method that the enviroment need to routing the appropiated place. 

### Technologically distributed data warehouse model

In this method, use the distribuited architectured to support data warehouse. This focus has several advantage:  the entry cost os cheap in hardware and software, there is not theoretical limit to how much data can be placed in the data warehouse and computes to process it.

There are considerations: when data warehouse start to expand, an excessive amount of traffic starts to appear on the network by overlapping data in several processors or transfering data between processors. In crucial issues in this focus is how organize to manage better the queries of user from enviroment.


### Independently evolving distributed data warehouse model

In this method in which independent data warehouses are developed concurrently and in an uncontrolled manner by result of political and organizational differences, so that the data warehouse architecture has to manage and coordinate multiple data warehouse efforts within the organization but he isn't know what kinds of efforts are occuring and how they relate to the overall architecture, the management and coordination is more difficult.

![Type of development efforts to build a independently evolving distributed data warehouse model based in cases](image/TypeOfEfforts.png?raw=true)

In general there are different types of efforts require very different approaches to management, it is based in above image this phrase:

1.  The rare case, `a corporation has totally separate and unintegrated lines of business` for which enviroment are being independently built by different develoment teams. Accordingly there is a little or no need for cross-management and coordination of development efforts with a little dange that one development efforst will conflict with another.
2.  The case is when `corporate distributed data warehouse is being built and various development team are creating different parts of the same data warehouse`. This case require a discipline, atenttion and close coordination among teams to achievere a collectively satisfying result.
3.  This case is when `multiple different development teams are building different levels of data (summarized, archived and detailed data) inside data warehouse enviroment`. this is easier to management then either of the two previous cases: the relations and hierarchy of use and expectations in data inside of the enviroment.
4.  The last case occurs when `multiple teams are trying to build different part of the current level of details of the data warehouse enviroment in a nondistributed manner`. This is a rare phenomenon and require a special attention, data architecture must be aware of what the issues are and how they relate to success.



# Requirements of technology

## Main features needed to support data warehouse
The data warehouse enviroment requires a simple set of technological features than its operations predecessors. This is a list of  following  needed features:

1.  `Managing large amounts of data`: The explosion of data volume came about because  the data warehouse required that both detail and history be mixed in the same environment. it's a issue about the cost of storage and processing to manage large amounts of data, so then its need to do well.
2.  `Managing multiple media`: The technology underlying the data warehouse must handle multiple  storage  media like cache, main memory, magnetic tape and others. it's manage following a hierarchy of storage of data in terms of speed of access and cost of storage.
3.  `Indexing and monitoring data`: The data warehouse needs a easily and efficiently  several techiques of indexing; like example: sparse, temporary or dynamic indexes; to get the flexibility. the monitoring of data to determinate what data has and has been used. The purpose of monitoring evaluation of performance of data warehouse to usage of data.
4.  `Interfaces to many technologies`: the ability both to receive data from and to pass data to a wide variaty of technologies. This interface need to easy to use and operate in a batch and online mode.
5.  `Control of data placement`: the designer must have a specific control over the placement of data at the physical block or page level. Designer often can arrange for the physical placementof data to coincide with its usage to gain more efficient access of data.
6.  `Parallel storage and management of data`: When data is stored and managed in a parallel fashion, the gains in performance can be dramatic.As a rule, the performance boost is inversely proportional to the number of phys-ical devices over which the data is physically distributed, assuming there is an even probability of access for the data.
7.  `Metadata management`: Without a good source of metadata to operate from, the job of users is much more difficult. There are differents varieties in metadata: business metadata is use by business person. Technical metadata is use by developer. Note: every technology in the business inteligence enviroment has its own metadata: Tools, ETLS, reports and others.
8.  `Language interface`: The data warehouse must have a rich language to access data inside. This language should be easy to use and robust, and operate efficiently. Only technical peoples write direct SQL queries, others need to have a language interface more simple than SQL that you need to create. Each of these language has its own strengths and weakness based in focus to use: analysis. data mining and others.
9.  `Efficient loading of data`: The need of efficient load data capacity is important everywhere, but even more so in a large warehouse. 2 fundamentals ways: records at a time through a language interface or in masse with a utility. a techniques to manage load of data to use a staging data to storing data.
10.  `Efficient Index Utilization`: The indexes must be able to be accessed efficiently and support several ways: using bit map, multilevels, storing all or part in main memory, create selective indexes and range indexes and others.
11.  `Compaction of data`: When you compact data, you get small volume, reduce consume of I/O resource and access of the data efficiently.
12.  `Compound keys`: Support compound keys occur everywhere in data warehouse because of time variancy and key foreign relationships are quite common in the atomic data that makes up the data warehouse.
13.  `Variable-length data`: manage variable length data efficiently to support the access of variety of data.
14.  `Lock management`: to able to selectively turn lock manager of and on is necessary to manage a cost of resource used by lock manager.
15.  `Index-only processing`: it is possible to service a request by simply looking in a index without going to the primary source of data.
16.  `Fast restore`: it is a capacity to quickly restore a data warehouse table from a secondary storage; you need to support restore full and partial database operation. you need use tools to detect corrupted data inside of data warehouse.

## Difference transactional database and data warehouse enviroment
There are differences between 2 parts:

* Data warehouse processing can be characterized as load-and-access processing: the data is accessed and analyzed there, an update is not normally done once the data is loaded, corrections or adjustments to be made at off hours.
* Data warehouse holds much more data because have atomic, granular, historial and summaried information. 
* Transactional database must be able to accommodate record-level, transaction-based updates as a normal part of operation with a own set of commands to support. In data warehouse doesn't need it.
* Transactional database DBMS include reserved space for future block expansion at the moment of update or insert. Data warehouse not include extra space to insert rows.
* Data warehouse has more technique of index than transactional database to get best access of data.
* Transactional database is optimized for transaction access, and a data warehouse is optimized a physical location to access and analysis.

## Multidimensional DBMS and data warehouse

A Multidimensional DBMS or OLAP processing provide an information system with the structure that allows an organization to have very flexible access to data, to slice and dice data any number of ways, and to dynamically explore the relationship between summary and detail data. It is called data marts too and this focus is used in data mart level inside data warehouse arquitecture.

`The data warehouse is an architecture infraestructure and Multidimensional DBMS is a technology`. The data warehosue serves as a foundation for the data that will flow into multidimensional DBMS by data warehouse have a centralized and integrated data across organization to avoid those problem in Multidimensional DBMS to get best performance to query it.

![Example of architecture in data warehouse and multidimensional DBMS](image/MultiDimensionalDBMSInFinance.png?raw=true)

Another advantages is that summary data may be calculated and collected in the OLAP processing and then stored in the data warehouse to archived long time. `So data warehouse and OLAP processing can be bidirectional communication` if it is need.

There are 2 type of Multidimensional: relational technology or "slicing and dicing" technology, this last options is called a "Cube". the relationa option can support a lot of data, dynamic joining of data, general-purpose update processing and good structure to support no known pattern of usage; but it is less perfomance and  can not optimized for access processing. the "Cube" option get a good performance, can be optiomized for very fast access of data, can "sliced and diced" data, can be examined in many way and if pattern of access if know, then the structure of data can be optimized; but it take a long time to load, can't control as mucho data as a relational option and dont support a dynamic joins of data.



# Solutions
There are some ideas, best practics and methods to solve some problem you might confront while you implement a data warehouse.

## Techniques to scanning data in operational datawarehouse extract process
Loading data on an ongoing basis — as changes are made to the operationalenvironment — presents the largest challenge to the data architect. Efficientlytrapping those ongoing daily changes and manipulating them is not easy. Scanning existing files is a major issue facing the data warehouse architect.

5 common techniques are used to limit the amount of operational data scanned at the point of refreshing the data warehouse:
1. `Scan data that has been timestamped in the operational enviroment`: When an application stamps the time of the last change or updateon a record, the data warehouse scan can run quite efficiently because data witha date other than that applicable does not have to be touched.
2. `limiting the data to be scanned is to scan a delta file`: A delta file contains only the changes made to an application as a result of the transactions that have run through the operational environment. With a deltafile, the scan process is very efficient because data that is not a candidate for scanning is never touched. Not many applications, however, build delta files.
3. `scan a log file or an audit file created as a by-productof  transaction  processing`: A log  file  contains  essentially  the  same  data  as  adelta file. However, there are some major differences: it's more protected (main used to recovery process),formatting internal system is built for system purposes and not applications, more useless data that data warehouse need to process.
4. `modify application code to report this changes`: don't use because much application code is old and fragile.
5. `comparing images of the operational file together`: comparing "before" and "after" image to determine the activity that has transpired. This is a complex, resourcer-utilizations and cumbersome approach.

![5 common techniques to scanning data in ETL operational- data warehouse level](image/techniquesExtractDataOperationDatawarehouse.png?raw=true)



## Alternatived techniques to design data warehouse
There are some techniques you can use to modeling a arquitecture enviroment of data.



### Dual levels of granularity
`When a organization has lots of data in data warehouse and you need to efficiently storing and accessing data in great detail; you can use this techniques.`

This technique say you that manage a data from data warehouse level using 2 instance with different levels of granularity:
* **Lightly summarized data**: In primary level of data warehouse because it will be a part of enviroment. this is a data is lightly summarized only to a very small extent. This summary of data did into fields that are likely to be used to analyze but there are a level of details that can be accessed in the lightly summarized data.
* **True archival data**: this data contain all details comming from the operational enviroment is stored. this a separated part of the data mart level.

While a Lightly summarized data tier is more frecuently and easy to access but a true arhival data tier is rare and hard to access. All it because the access of data to analyze. 

![Dual levels of granularity in data warehouse](image/DualLevelOfGranularity.png?raw=true)


### Living sample database
`When a organization has a volumn of data very large to hard analyzeimage/ this data because the time of accessing and cost of resources; you can use this techniques`.

This technique say you must sample data from a so-large volumen of data in data warehouse into subset DB and you need to periodically refresh data. You get a most performance in the accessing of data, best utilization of resources to be productive.

When you use this technique, you must know how data will load, the amount of data will store in subset and how randomg the data will be. You can sample either lightly summarized or true archival data.

![Living sample database](image/LivingSampleDatawarehouse.png?raw=true)

You must use this subset to statistical analysis, looking at trends or analytical focus or preparing process; don't use as general-purpose database because it hasn't all data. Because the living sample DB is refreshed with current data, your analytical answers or implementation of processes will not suffer in accurancy.

## Techniques of enhanced performance in data model
When you create a data model and it applied in architecture (either at the operational level or at the data warehouse level), you wanna get a good performance and if you have a several tables you will suffer performance in I/O by queries several tables to get answer.

There are some techniques i can use to enhance this performance:

1.  `Merge some of tables` so that minimal I/O is consumed by a get a large table.
2.  `Create an array of data`. When normalized data so that each occurrence of a sequence of data reside in a different physical location. Only when there are a stable number of occurrences, where data is accessed in sequence, where it is created and/or updated in a statistically well-behaved in sequence; it is a good choice.
3.  `Replicate common accessed data inside several tables` that those data are common between tables. Enhace performance in read queries but update queries is complex. 
4.  `Separate of data when there is a wide disparity in the probability of access in differenct tables`. Get a short I/O cost and access of data, so then you get a efficient performance in queries.
5.  `Use derived data into data model` can reduce the amount of I/O needed: if program accesses regularly data in order to calculate something and you need to create this data in specified time; you can use this techniques.
6.  `Use creative index/profile`. it's created as data is passed from the operational level to the data warehouse level.  Because each unit of data must be handled in any case, it requires very little overhead to calculate or create an index at this point. The creative index/profile does a profile on items of interese to the end user: largest purchases, the most inactive accounts, etc. If the requiriements that might be of intereset of management can be anticipated, it makes sesnse to build a creative index.
7.  `Referential integrity as artifact` of relationships in the data warehouse between databases. Therefore some data will be duplicated and some data will be deleted when other data is still in the data warehouse. 


## Techniques to control refreshed data from operational enviroment

The ongoing updates of old data from operational environment to data warehouse environment is a load that need to manage by data warehouse because this is a largest unexpected expense in day-to-day operations.

There are several focus to manage this load that is part of data warehouse integrity:
1.  `read data to legacy database`: this is an inefficient and expensive method, because a process scanning all file inside legacy database to identify change that it will be few. You must get a online legacy database while process work to scanning database.
2.  `data replication`: this method need know that data to be trapped be identified prior to the update, then as update occurs, the data is trapped. This method can be selectively control that data need to trap and well documented by understand of structure of data. it need a extra I/O to trap data.
3.  `Changed data capture`: this method use the logs to capture and identify teh changes that have occurred. this method no need a extra I/O to trap data, and get all update processing; but i will get more data in log that you need.
4.  `lift the changed data out of the DBMS buffers`: when change occurs, the change is reflected immediately so saving time but you need more online required resource (like software snesitive to  change), there is a performance impact. This focus can handle large amount of processsing at a very high speed.

## Consideration in types of development efforts in distributed data warehouse

There are many considerations about all development efforts to build of distributed data warehouse you need to know.

### Completely unrelated data warehouses

If all business/regions/areas are autonomous to build a data warehouse with difference stack technology based in requirements; there is a common aspect of integration all at one : financial area; so then the organization need to build a corporation financial data warehouse to store this data. This data warehouse contains simple entities and don't get a integration of entity. this data warehouse will feed either local data warehouse or operational system of the local area.

!["Integrated" data warehouse : financial area](image/CompletelyUnrelatedDataWarehouses.png?rraw=true)

The metadata is vital at the local level and it is also need at the corporate financial level inside corporate data warehouse; however, there is not real integration between data warehouses, there is no need to tie any of the metadata together.

### Distributed Data Warehouse Development

In this effort, there is a degree of business integration by the corporation entities are sharing among the different areas, independently its implementation of data warehouse.

If there are many similarities between this method and datawarehouse of the unrealted companies, the is one major difference: the  corporate  distributed  data  warehouse  represents  the  very  fabric  of  the business itself in several aspects.; In other cases, if users try to use the data warehouse beyond the financial area, they will be disappointment with the data warehouse.

after all areas get a data model to build a data warehouse; the corporate data model will create to build a data warehouse. This corporate data model reflects the integrations of business at the corporate level and maybe overlap considerably with parts of the local data models. the local teams are better to reshape their data based in requirements of corporate data model.

![Similar Unrelated distributed and distributed cases](image/SimilarUnrealatedAndMultieDWH.png)

In corporate data model, there is not overlap in content of data; the source of data are either local data warehouses or local operational systems and this decision to pasing data is unique of local teams. 

The important issue is how to create and transport the local system of record data into corporate data warehouse at the technology level. In some cases, staged data is kept at the local level; or other cases, the staged data is passed on to the corporate enviroment with no access at the local level.

The metadata plays a very important role across the distributed corporate data warehouse, it will provides the consistency and uniformity tools to coordinate the structure of data betweeen the local data warehouses to move the distributed data warehouse.

### Building the warehouse on multiple levels

In this case; the easier all cases; like data architecture, you need to coordinate the efforts of the different development teams, both in terms of the specification of content and structure and in terms of the timing of development.

The  data  model  for  the  data  warehouse  directly  reflects  the  design  and development  effort  by  the  group  doing  current-level  detailed  analysis  and design. Of course, indirectly the data warehouse data model reflects the needs of all groups. the groups working on the higher levels of summarization have their own data models that reflect their own specialized needs.

![Multiple development teams implement multiple levels of data warehouse](image/TeamsInMultiLevelCase.png?raw=true)

The different teams can use difference technology tools to implement the different detailed levels of data based in performance and other criterios. whether the different levels of data are on a single platform or on multiple platforms, metadata must be carefully stored and managed, so that continuity from one level of detail to the next can be maintained. 

`Because  different  platforms  are  commonly  used  for  the  different  levels  of data that are being developed by different groups, the issue of interconnectivity arises.` the effective bandwidth of the interface or the compatibility of access at the call level are part of this problem.

The coordination among the groups can be as simple as an agreement on a data model that satisfies the needs of all parties, or the agreement can be much more elaborate if circumstances warrant.

### Multiple Groups Building the Current Level of Detail

As long as the groups that are developing the current level of detail are developing mutually exclusive sets of data, there is little difficulty. This is a exception reathre than the rule. It is much more common for the multiple development groups to be designing and populating some or all of the same data. The metadata in this case is critical to manage all efforts.

There are problems arises when the groups overlap: cost of storage and processing by redundacy of data; create a spider web into the enviroment by uneffective reconcilability data in several parts. The solutions of problems is a data model that it will reflect the collective need among the teams. there is no need to build all of the tables at once, the teams implement some table at a time and the end-user feedback can be factored into the modification of the table or  add new tables at a later time ti reflect new requirements.

`Normally, different groups have unique requirements. These requirements  result  in  what  can  be  termed  “local”  current-level  detail.` The local data is certainly part of the data warehouse. It is, however, distinctively different from the “common” part. The local data has its own data model, usually much smaller and simpler than the common detailed data model. Just because data is not common to all development groups does not mean that it does not belong in the current-level detail of the data warehouse

![Several Team will get difference requirements of implementation](image/NonredundancyByNonKey.png?raw=true)

`There is nonredundancy of data across all of the detailed data.` Of course, the nonredundancy of the data is restricted to nonkey data. Redundancy exists at the key level because a form of foreign key relationships is used to relate the different types of data.

Another strategy is to use different platforms for the different types of datafound at the detailed level. This option is certainly one that isvalid, and it often satisfies the different political needs of the organization. With  this option, each  group doing development can feel that it has some degree of control of at least its own peculiar needs.

there are several drawbacks in strategy from previous phrase: multiple technologies must be purchased and supported, the end user needs to be trained in this tech stacks and the boundaries between them may not be as easy to cross and will transform in problems of performance and manage of the access of data.

![Problem to use several tech stack to implement a detailed data](image/ProblemWithMultiTechInDetailData.png?raw=true)

## Inverted data warehouse alternative focus

When i have large data warehouse; the common focus in storage management to put the data in the disk storage, then, after the data ages, the data is placed on near-line or archival storage.  There is an alternative: first to put the data into near-line storage and not disk storage.

When a query is done, the data is "staged" from the near-line enviroment to the disk enviroment. Once  in  the  disk environment, the data is accessed and analyzed as if the data resided there permanently. Once the analysis is over, the data is returned to near-line storage.

The inverted data warehouse have a price: every request must be stage and staging takes time but; depending on the analysis being done; stagin may not be an onerous penalty. If there are a lot of explorers accessing and analyzing the data, then staging may simply be part of the price to be paid for satisfying irregular requests. sSome of the performance penalty can be mitigated by running more than one instance of the disk-based DBMS. In other words, with two disk-based DBMSs running, two queries and analyses can be accommodated, thereby mitigating some of the time needed for queuing the data waiting for staging.  By  using  more  than  one  instance  of  the  disk  based  DBMS,  a  certain amount of parallelism can be achieved.



# Migration to the architected enviroment

## A migration Plan
`A plan starts to build a corporate data model`. This model represents the information neeed of the corportation and not necessarily what it currerntly has in legacy systems. This one may be built internally or it may be have been generated from a generic data model; and need to identify major subjects with theirs attributes, keys, definitions and relationship between them.

The corporate data model identifies corporate information at a high level and this use to build a lower-level model, this low level identifies details that have been glossed over by the  corporate data model. this mid-level model is built from the identified subject areas in corporate data model and built one at a time. both high-level and mid-level model focus only on the atomic data of the corporation and excluded derived data by several reasons: change frequently, are created from atomic data, deleted altogether frequently, there are many variations in the creations and others.

![Step of interation of data model in a migration plan](image/dataModelInMigrationPlan.png?raw=true)

`After the corporate data model and the mid-level model are in place, you need define the system record`. This system is defined based in legacy systems of company and other systems inside organization. This activity is identify the "best" data have in all legacy system, you use data model like a benchmark to determinate what the data is best to goald of requirements of data models. criterias like what data is the most complete, the timeliest, the most accurate and others are part to process.

Once the system of record is defined, you identify the technological challenges are to bring data of system of records into data warehouse enviroment. Others challenges you need to face are: volumen of data will move, processing data previously to store in data warehouse: cleasing and/or summarized data.

`After  the  system  of  record  is  defined  and  the  technological  challenges are solved, you need to design the data warehouse`. If all previous activities has been done properly, this activity is simple. Adding array of data, adding data redundantly, separating data under the right conditions and merging table are appropiated methods when the structure of the data need.

![design data warehouse in a migration plan](image/designDataWarehouseInMigrationPlan.png?raw=true)

Principally, the following things need to be done:
* An element of time needs to be added to the key structure if one is not present.
* All purely operation data need to be eliminated.
* Referential integrity relationships need to be turned into artifacts.
* Derived data that is frequently needed is added to the design.

Stability  analysis  of  the  data  needs  to  be  done. In stability analysis,  data whose content has a propensity for change is isolated from data whose content is very stable. Once the data warehouse is designed, is organized by subject areas with its separated tables. 

Depending of the number of occurrences of data would have a difference considerations of design this part: summarized, aggregated or partitions data or using profile records. The same case is applied to arrival rate of data into data warehouse: you will need to use staging of data, parallelization of the load stream, delated indexing and other methods to handle the data flow. There are consideration to see in process of design of data warehouse.

`After the data warehouse design, the next step is to design and build the interfaces between the system of record and the data warehouses`. This method to populate the data warehouse and consuming more time of process the plan; if the interfaces appear to be merely and extract process but it contains more activities:

* Integration of data from the operational, application-oriented enviroment.
* Alteration of the time basis of data.
* Efficient scanning of the existing systems environment
* Condensation of data

`Once the interface programs are designed and built, the next activity is to
start the population of the first subject area`. In theory you need to read data from legacy system, move and store data in warehouse enviroment, directories are updated, metadata is created and indexes are made.

There are many good reasons to populate a fraction of warehouse: changes to the data easily and quickly, get feedback of user by interation of warehouse enviroment, data architect can adjust of enviroment by feeadback quickly.

![Running of migration plan](image/activitiesInMigrationPlan.png?raw=true)

Remember: he population and feedback processes continue for a long period. In  addition,  the  data  in  the  warehouse  continues  to  be  changed.  Of course, over time, as the data becomes stable, it changes less and less. End users don’t know what their requirements are until they see what the possibilities are.

you need to schedule the refreshment of data in data warehouse. As a rule, data warehouse data should be  refreshed  no  more  frequently  than  every  24  hours. By  making  sure  that there is at least a 24-hour time delay in the loading of data, the data warehouse developer minimizes the temptation to turn the data warehouse into an operational environment. **By strictly enforcing this lag of time, the data warehouse serves the DSS needs of the company, not the operational needs**.

The lag of time can be use to adjust the enviroment without impact of performance of warehouse. there  are  cases  where  rapidly  placing  data  in  the  warehouse  may  be what the requirements are. In this case, it helps to have technology suited for what is termed active data warehousing. Active data warehousing refers to the technology of being able to support some small amount of online access processing  in  the  data  warehouse.

## Strategic Considerations

The migration plan that has been discussed is solely for the construction of the data warehouse. Isn’t there an opportunity to rectify some or much of the operational  “mess”  at  the  same  time  that  the  data  warehouse  is  being  built? The answer is that, to some extent, the migration plan that has been described presents an opportunity to rebuild at least some of the less than aesthetically pleasing aspects of the operational environment.

![Data arquitect using agent of change to becomecompelling and ally the efforts toward the architected environment with the appropriate agents](image/StrategistToChangeOperationalSystems.png?raw=true)

One approach is to use the data model as a guideline and make a case to management that major changes need to be made to the operational enviroment. The amount of effort, the amount of resources, and the disruption to the end userin  undertaking  a  massive  rewrite  and  restructuring  of  operational  data  andsystems  is  such  that  management  seldom  supports  such  an  effort  with  the needed level of commitment and resources.

Other focus is to coordinate the effort to rebuild operational system with the "agents of change": the aging of systems, the radical changing of technology, organizational upheaval, massive business changes. The steps the data architect takes to restructure the operational environment are:

1.  **Create a delta list**: it is an assessmeent of the differences between the  operational environment and the environment depicted by the data model. The delta list is simple, with very little elaboration.
2.  **The impact analysis**: At this point an assessment is made of the impact of each item on the delta list. Some items may have a serious impact; other items may have a negligible impact on the running of the company.
3.  **Create resource estimate**: This estimate is for the determination of how many resources will be required to “fix” the delta list item.
4.   **Report that goes to information systems management**: Management then makes a decision as to what work should proceed, at what pace, and so forth. The decision is made in light of all the priorities of the corporation

## Data driven and spiral methodologies

`The methodology for the building of the data warehouse is called a spiral development methodology`. This methodology is much larger than just a development methodology by it contain information about how to build and alse describes how to use the data warehouse. The migration plan describes general activities dynamically but the spiral development methodology describes specific activities, deliverables from those activities and the order of the activities.

The spiral methodology is difference of waterfall methodology: all of one activity is completed before the next activity can begin and the result of one activity feed another.

![Comparing spiral and waterfall methodologies](image/SpiralAndWaterfallMethodologies.png?raw=true)

One of the salient aspect of a data driven methodology is that it builds on previous efforts using both code and processes that have been developed and it can be achieved is through the recognition of commonality: before the developer to start the design or build, he need to know what already exist and how it affects the development process. Don't reinvent the whell is the essences of data driven development.

Anohter aspect is an emphasis on the central store of data as the basis of Analysis processing, recognizion that processing has a very different development life cycle than operational system: processing begins with data and ends with requirements

# Unstructed data in data warehouse

Emails, ppts, sms, and others file are part of unstructured data that organization need to manage any degree. Those unstructured data file can be divied into 2 bradd groups: Communication and documents. The Communications are short and are for very limited distributed. The documents tend to live a lot longer than communications, are larger than communication and to be a wider audience. Both are based in Text.

## Integrating the 2 worlds

There are part to integrated unstructed and structured data in enviroment.

`The text is the common link between them`. if applied a match of words between both world, you will get several problems: 
* Mispelling words are found in the two enviroments that arise the question: should there be a match made between these worlds by those word?
* Context to use those words: are words used in same context?
* Same name on subject in both worlds: are words reference the same person?
* Nicknames on subject in both words: are difference nicknames reference the same person?
* Diminutives of unique word: is the group of words reference the unique word?
* Incomplete names of subject: is word reference to the subject.
* Word steams match.

The fundamental mismatch between both world is the enviroment representation: the unstructured data represents document and communications while the structured data represents transactions. In structured data, the textula data is used to identify and clarify the transaction; but the unstructured data, the text can be verbose, cryptic, eloquent and/or confusing.  Despite the difficulties of matching text across the enviroments, it still is the key to the integrations.

To match both world, you need to remove stop words and reduce all words to stem of this word to normalize the text. Then you get normalized words in both enviroment, you can apply probabilistic models to find match in words of two enviroments to create link of worlds. In General, you can use any NLP model to find similarity of words from two enviroments to create links in both enviroment.

![Using probability matching in both worlds](image/probabilityMatchedInBothEnviroment.png?raw=true)

There are others methods to matching: Collecting documents of unstructured data and match the content of document and list of word from industrially recognized theme; clustering documents of unstructured data by phrases and words to find a theme of document group; using raw matching of data: create link if word in unstructured data document is found anywhere in the structured data; to create a link the two enviroments using metadata and abstraction of data of unstructured data with theme of unstructured data

## Infrastructure of integration of data

There are 2 approaches to the usage of unstructured data in the data warehouse:

* One approach is to access the unstructured enviroment and pull data over into the structured enviroment. This works well for certain kinds of unstructured of data.
* Another approach is one tier of the data warehouse is for unstructured data and another tier of the data warehouse is for structured data.

The last approach is name two-tier data warehouse. there may be either tight ir a casul relationshio of data between the 2 enviroment, or there may be no relationshio at all.

Both enviroments share similar parts: it exists at a low level of granularity, has an element of time attached and it is typically organized by area or theme. But the someone of differences between both of enviroment in the data: the unstructured data can be dividied in two groups: Communications and documents, the difference to access if that the communications are organized by identifies main parts of text while the documents are organizaed according to words or/and theme.

`Depending on quite a few variables, it may be desirable to store the actual document in the unstructured data warehouse, or it may make sense to store only references to the location of the document in the data warehouse`: How many documents are there?, What is the size of the documents?, How critical is the information in the document?, Can subsections of the document be captured? or Can the document be easily reached if it is not stored in the warehouse?. An intermediate solution between having the document in storage or out of storage is storing the sentence before and after where the themed word lies

There are many commercial products `that are used to embody structured visualization` based in analyze, clustering, counting and otherwise preparation. The  SOM (self-organizing map)  produces  a  display  that appears to be a topographical map. The SOM shows how different words and the documents are clustered, and displayed according to themes. The SOM has several features: clustering  of information based on the data found in different document, toing drill-down processing.

## Structure and topics of data warehouse for unstructured data

In next image you see the structure of records in unstructured data warehouse for communication and documents. There are common parts to manage this data inside the data warehouse.

![Records of unstructured data inside data warehouse](image/recordsOfUnstructuredDataInDataWarehouse.png?raw=true)

The volumen of data inside data warehouse are an order of magnitude more important simply because there is so much more unstructured data than structured data; and developer can mitigate: Do not store all of the documents; remove communications blather; Create an area where the documents or communications are stored separately, if they have to be stored at all; age data off by date wherever possible; do not store too many context references; monitor the usage of the unstructured data warehouse to determine what the patterns of usage are.

![Record of structured data in data warehouse](image/recordsOfStructuredDataInDataWarehouse.png?raw=true)

In the previous image, you show what text that relates the two environments. In structured enviroment has several components: an abstract level (metadata and repository) and record level ( raw data, identifiers and close identifiers). The identifiers are unique and use to locate a specified and unique records while close identifiers are good probability to specified records but it can use to more records.

In the next image, it shows to how data in the differenct enviroment relate them based in fields in records.

![Relation by text based of recrods from unstructured and structured data warehouse](image/RelationUnstructuredAndStructureDW.png?raw=true)

# Relational and dimensional model for database design

There are some issues based in model approach to design a database in datawarehouse and data marts and other parts inside enviroments: kimball (dimensional model) or Inmmon (relational model).

## Dimensional or relational models

The relational model has different properties in tables, characteristic in columns, type of index and properties. one can use keys and foreign keys to establush relationships between rows, use SQL to interface to querying and manage data. The data in the relational model can be organized in several level of granularity by normalization process.

`The value of relational model to design a database for the data warehouse is the flexibility` you have to use detailed level of normalized data, discipline to design and clarity of the meaning; `and the versability` because the detailed data is collected and can be combined, many different views of the data can be supported when the design for the data warehouse is based on the relational model.

The multidimensional model is based in design of star join from main table (called fact table) that contains many occurrrences of data related with dimension table that contains details of context of occurences. When you need more fact table to represent the process, you need to use snowflake structure then one share dimension tables between them to shape a snowflake.

`The value of multidimensional model is the efficiency of access` to delivery data to user but the achieve it you need the requirements must be gathered and assimilated: this is a heart of defining the model.

## Differences between the Models

This comparation is for a data warehouse design.

The multidimensional model is good in the performance but it isn't in the flexibility while the relational model is good in the flexibility but it isn't in 
the performance. The roots of the differences is the shaping of models: the multidimensional model is shaped by the user requirements while the relational model is shaped by enterprise data model.

The consequences of the shaping of model are: 

* **Abstraction to use of data**: the relational model have a high level of abstraction to design the model, so then model can support many differents requirements of differents user. The multidimensional model is focus a set of user in their specified requirements to solve because the abstraction is not higher.
* **Access of data**: The flexibility of model makes the relatonal model has not  terribly optimal for the performance of the direct access of data, if you want optimal access you need to create a model based in data warehouse model to do; while  in the multidimensional model will get a fast access by this model is designed to specified queries.

`The capacity of build new customer tables based in corportation data model from relational model is it has not redundant of data organized in its simplest form.` if a specified group of user need to change data, it will impact in their customer tables and don't tables of another groups of users, this capacity can be easy in relational model but in multidimensional model has not.

![Capacity of build customer tables in relation model](image/capacityOfCustomerTableRelationalModel.png?raw=true)

`Manage the future unknown requirements of unknown users is part the process, the granular data is the secrets to manage those situations`, so then the relational model is more capacity to control those but depending of model in multidimensional model , it can or not controls those.

## Data marts types

Based in previous models in data marts enviroment, it can divide: all data marts based in multidimensional model are created from directly legacy systems and it's called independe data marts; while all data marts based in relational model are created from data warehouse enviroment and it's called dependent data marts.

The independent data marts are very popular because it can a relatively inexpensive thing to build, allow an department of organization get information in its own hands, only think in deparment constraints. It focus has a big problem: in the long-tem all data mart can be inconsistent to share information in same focus if the process are not consistent at all, you have several same interface with few change you need to maintain and/or writted and get several resources to manage programs executed.

![Problems of indepent data mart](image/independentDataMart.png?raw=true)

`Ìn general dependent data marts are best in long-term with global thinking focus while independet data marts are short-term with limited scope solution`.

# Large Data warehouse
When the data warehouse is so large, some consideration need to know about this situation. The main components to grow the data warehouse are: detailed data, historical data and diverse data in time frame of usage in corporation.

## Impact of large data warehouse

When the data warehouse collect large volumes of data; issues about cost, usefulness anda data management are relevant in design. This issues are explain in differents aspects.

`The basic data-management activities are harder`: when the data is growing in data warehouse, to load, indexing and access take more time to complete this activities.

![Management of activities in data](image/basicDataManagementActGrowData.png?raw=true)

`The cost of storage is high`: when the data grows, the cost of budget to store data increments exponently as well component like processor and software to control the usage of the data increments to support this activity.

![Cost of storage](image/costBudgetGrowData.png?raw=true)

`The usage pattern of data is differents based in usage`: when the data grows, the data will use is fewer in all storage and don't scanning all storage to get this data. you will get 2 type of usage of data: unfrequent and frequent usage of data.

![Pattern of usage in data ](image/patternOfUsageDataGrowData.png?raw=true)

## Disk storage in usage of data

When you have frequent and unfrequent usage of data, you need to store this data in different storage to get optimal queries to answer enviroment. The disk storage is common storage into DBMS and use in transactional DB.

You need to store the frequently used data in storage of fast access mechanist; called near-line storage; to get the data while the data used unfrequenly stored a archival storage. The near-line storage are storage with robotically controlled, get bulk amounts of data, reliable over a long period of time; while a archival storage is more taped storage or ; in general; slow access and long live storage.

![Storage system in big data warehouse](image/SplitStorageMedia.png?raw=true)

Get a split-storage media incurs a loss of speed in process of moving between thoses storages; but in general performance in access of data the split-storage media better then a disk storage in performance depending of case and probability of usage in data.

![Analogy in performance in two options of storage media in big data warehouse](image/PerformanceDiskAndSplitStorageMedia.png?raw=true)

The main difference in archival and near-line enviroment is the near-line storage is seen an extension of data warehouse: the disk and near-line storages are only unit of storage and get transparent into end user to query this enviroment; while a archival enviroment, the end user need know that your query is proccess in this enviroment.

![Logical units in storage inside data warehouse enviroment](image/StorageEnviromentInBigDWH.png?raw=true)

This transparency in near-line and data warehouse enviroment is achieved in format of data row, compability in technology terms and the near-line system available to the database system.

## Moving data from enviroment to another

The moving data from the near-line and the data warehouse enviroment can be accomplished in many ways:
* **The manually moving the data** between enviroments by database administrator; this focus is very flexibility and work well and it's a low-tech option and avaible to anyone.
* **Use a hierarchical storage management approach**: whole data sets are moved, it can be automatic. In this focus, you loss the granularity in moving data sets.
* **Use a cross-media storage management approach**: this option is fully automated and operates at the row level of granularity between enviroments. It's a complex and expensive focus to implement.

![Table of disadvantage and advantage in data moving management](image/TableDataMovingManagement.png?raw=true)

The cross-media storage management can be streamlined by the usage of a data warehouse monitor: monitoring the SQL query and result, the system tell what data is and is not being used in the data warehouse. it can allow a more finely tuned in data warehouse system. In general, as a rule; use a third-party monitors to implement in enviroment.

## Maximum capacity

The capacity of enviroment is meaning by combination with a fair parameters: volumen of data, number of users, workload complexity.



# The life cycle of data

There is a life cycle of data as it enters the corporation and then is used there. It makes sense to match the life cycle of data to the different technologies found in the  data warehouse enviroment based in usage of data.

![life cycle of data in data warehouse enviroment](image/lifeCycleOfDataInDWHEnviroment.png?raw=true)

When the flow of dara throughout the information life cycle does not follow work in prevous image; those data becomes bloated and clogged up and analysis will be hard or impossible.



# Testing and the data warehouse

In operational enviroment need the testing enviroment like part of enviroment because operational code need to correct once it meets the production; it is a expectative in operational enviroment. `In data warehouse enviroment, the expectative is constant adjustment and readjustment based in the constant feedback of end users to get the accuracy and completeness data in data warehouse enviroment`.

![Constant feedback loop of end users ](image/ConstantFeedbackLoopOfEndUsers.png?raw=true)

Then the question will arise is: does the data warehouse enviroment places bad data? or does the data in data warehouse enviroment is perfect?; the answer to both questions is Not, the principles is: `The data placed in the data warehouse is the best data that can be placed there, but no one guarantees the perfection of the data`.  This principle is based in the type of decision made with the data: business decision of data, features or properties in data, and others.


# References
1.   build of data warehouse, fourth edition. W. H. Inmon. 2005
