# Data warehouse based in Kimball focus.

======================================

## Purpose
Contain all concepts, best practices, patterns, architectures and concepts about data warehouse i learned based in kimball focus


## Index of readme
This is a index to best navigation inside document.

- [Dimensional modeling introduction](#dimensional-modeling-introduction)
  - [General issues in dimensional modeling](#general-issues-in-dimensional-modeling)
  - [Star schema vs OLAP cube](#star-schema-vs-olap-cube)
- [Star schema modeling](#star-schema-modeling)
  - [Fact tables](#fact-tables)
  - [Dimensional tables](#dimensional-tables)
- [Arquitecture models](#arquitecture-models)
  - [Kimball arquitecture](#kimball-arquitecture)
    - [Operation source system](#operation-source-system)
    - [ETL system](#etl-system)
    - [Presentation Area](#presentation-area)
    - [Business intelligence applications](#business-intelligence-applications)
  - [Alternative models](#alternative-models)
    - [Independent Data mart Architecture](#independent-data-mart-architecture)
    - [Hub and spoke corporate information Factory Inmmon Architecture](#hub-and-spoke-corporate-information-factory-inmmon-architecture)
    - [Hybrid hub and spoke and kimball architecture](#hybrid-hub-and-spoke-and-kimball-architecture)
- [Techniques in Star modeling](#techniques-in-star-modeling)
  - [Techniques and concepts about fact tables](#techniques-and-concepts-about-fact-tables)
    - [Fact Table structure](#fact-table-structure)
    - [Additive, Semi Additive and Non additive facts](#additive-and-semi-additive-and-non-additive-facts)
    - [Nulls in Fact Tables](#nulls-in-fact-tables)
    - [Conformed Facts](#conformed-facts)
    - [Transaction Fact Tables](#transaction-fact-tables)
    - [Periodic Snapshot Fact Tables](#periodic-snapshot-fact-tables)
    - [Accumulating Snapshot Fact Tables](#accumulating-snapshot-fact-tables)
    - [Factless Fact Tables](#factless-fact-tables)
    - [Aggregate Fact Tables or OLAP Cubes](#aggregate-fact-tables-or-olap-cubes)
    - [Consolidated Fact Tables](#consolidated-fact-tables)
    - [Fact Table Surrogate Keys](#fact-table-surrogate-keys)
    - [Centipede Fact Tables](#centipede-fact-tables)
    - [Numeric Values as Attributes or Facts](#numeric-values-as-attributes-or-facts)
    - [Lag/Duration Facts](#lag-or-duration-Facts)
    - [Header/Line Fact Tables](#Header-or-Line-Fact-Tables)
    - [Allocated Facts](#Allocated-Facts)
    - [Profit and Loss Fact Tables Using Allocations](#Profit-and-loss-fact-tables-using-allocations)
    - [Multiple Currency Facts](#Multiple-Currency-Facts)
    - [Multiple Units of Measure Facts](#Multiple-Units-of-Measure-Facts)
    - [Year-to-Date Facts](#Year-to-Date-Facts)
    - [Multipass SQL to Avoid Fact-to-Fact Table Joins](#Multipass-SQL-to-Avoid-Fact-to-Fact-Table-Joins)
    - [Timespan Tracking in Fact Tables](#Timespan-Tracking-in-Fact-Tables)
    - [Late Arriving Facts](#Late-Arriving-Facts)
  - [Techniques and concepts about Dimension Tables](#techniques-and-concepts-about-dimension-tables)
    - [Dimension Table Structure](#dimension-table-structure)
    - [Dimension Surrogate Keys](#dimension-surrogate-keys)
    - [Natural, Durable and Supernatural Keys](#natural-and-durable-and-supernatural-keys)
    - [Drilling Down](#drilling-down)
    - [Degenerate Dimensions](#degenerate-dimensions)
    - [Denormalized Flattened Dimensions](#denormalized-flattened-dimensions)
    - [Multiple Hierarchies in Dimensions](#multiple-hierarchies-in-dimensions)
    - [Flags and Indicators as Textual Attributes](#flags-and-indicators-as-textual-attributes)
    - [Null Attributes in Dimensions](#null-attributes-in-dimensions)
    - [Role Playing Dimensions](#role-playing-dimensions)
    - [Junk Dimensions](#junk-dimensions)
    - [Snowflaked Dimensions](#snowflaked-dimensions)
    - [Outrigger Dimensions](#outrigger-dimensions)
    - [Dimension-to-Dimension Table Joins](#Dimension-to-Dimension-Table-Joins)
    - [Multivalued Dimensions and Bridge Tables](#Multivalued-Dimensions-and-Bridge-Tables)
    - [Time Varying Multivalued Bridge Tables](#Time-Varying-Multivalued-Bridge-Tables)
    - [Behavior Tag Time Series](#Behavior-Tag-Time-Series)
    - [Behavior Study Groups](#Behavior-Study-Groups)
    - [Aggregated Facts as Dimension Attributes](#Aggregated-Facts-as-Dimension-Attributes)
    - [Dynamic Value Bands](#Dynamic-Value-Bands)
    - [Text Comments Dimension](#Text-Comments-Dimension)
    - [Multiple Time Zones](#Multiple-Time-Zones)
    - [Measure Type Dimensions](#Measure-Type-Dimensions)
    - [Step Dimensions](#Step-Dimensions)
    - [Hot Swappable Dimensions](#Hot-Swappable-Dimensions)
    - [Abstract Generic Dimensions](#Abstract-Generic-Dimensions)
    - [Audit Dimensions](#Audit-Dimensions)
    - [Late Arriving Dimensions](#Late-Arriving-Dimensions)
  - [Integration via Conformed Dimensions](#integration-via-conformed-dimensions)
    - [Conformed Dimensions](#conformed-dimensions)
    - [Shrunken Dimensions](#shrunken-dimensions)
    - [Drilling Across](#drilling-across)
    - [Value Chain](#value-chain)
    - [Enterprise Data Warehouse Bus Architecture](#enterprise-data-warehouse-bus-architecture)
    - [Enterprise Data Warehouse Bus Matrix](#enterprise-data-warehouse-bus-matrix)
    - [Detailed Implementation Bus Matrix](#detailed-implementation-bus-matrix)
    - [Opportunity or Stakeholder Matrix](#opportunity-or-stakeholder-matrix)
  - [Dealing with Slowly Changing Dimension Attributes](#dealing-with-slowly-changing-dimension-attributes)
    - [Type 0 or Retain Original](#type-0-or-retain-original)
    - [Type 1 or Overwrite](#type-1--d-overwrite)
    - [Type 2 or -td N-w Row](#type-2-or-add-new-row)
    - [Type 3 or Add New Attribute](#type-3-or-add-new-attribute)
    - [Type 4 or Add Mini-Dimension](#type-4-or-add-mini-dimension)
    - [Type 5 or Add Mini-Dimension and Type 1 Outrigger](#type-5-or-add-mini-dimension-and-type-1-outrigger)
    - [Type 6 or Add Type 1 Attributes to Type 2 Dimension](#Type-6-or-add-type-1-attributes-to-type-2-dimension)
    - [Type 7 or Dual Type 1 and Type 2 Dimensions](#type-7-or-dual-type-1-and-type-2-dimensions)
  - [Approaches for Dimension Hierarchies](#approaches-for-dimension-hierarchies)
    - [Fixed Depth Positional Hierarchies](#fixed-depth-positional-hierarchies)
    - [Slightly Ragged or Variable Depth Hierarchies](#slightly-ragged-or-variable-depth-hierarchies)
    - [Ragged or Variable Depth Hierarchies with Hierarchy Bridge Tables](#ragged-or-Variable-depth-hierarchies-with-hierarchy-bridge-tables)
    - [Ragged or Variable Depth Hierarchies with Pathstring Attributes](#ragged-or-variable-depth-hierarchies-with-pathstring-attributes)
- [Special Purpose Schemas](#Special-Purpose-Schemas) 
  - [Supertype and Subtype Schemas for Heterogeneous Products
](#Supertype-and-Subtype-Schemas-for-Heterogeneous-Products
)
  - [Real-Time Fact Tables](#Real-Time-Fact-Tables)
  - [Error Event Schemas](#Error-Event-Schemas)


# Dimensional modeling introduction
## General issues in dimensional modeling
This technique to analyze data because it addresses two simultaneous requirements: deliver data fast and understandable to the business users by make simple database from complex data base.

The dimensional modeling and 3NF models (or called ERD model) are compared in query performance issues, but the main diferent is in the degree of normalization: the RDMS can't efficiently query a efficient normalized data model, so you need to some degree of unnormalize into those queries.

## Star schema vs OLAP cube

The dimensional models implemented in RDMS are referred to as Star schema while the dimensional models implemented in Multidimensional Database are referred to as OLAP Cubes.

![Start schema and OLAP Cube](Images/StarSchemaVsOLAPCube.png?raw=true)

The OLAP cube is stored and indexed using techniques for dimensional data, performance aggregations or precalculated summary tables are created and managed by the OLAP cube engine and this deliver super query performances, flexibility to analyze and robust functions that exceed those available with SQL. The downside is that you pay a load performance price in generate this cube, especially with large data sets.


# Star schema modeling

![Example of star schema modeling](Images/StartModeling.png?raw=true)

This schema focus in dimensional modeling is the simplicity and symmetry. You can navigate easily in schema; `The reduced number of tables and use of meaningful business descriptors make it easy to navigate and less likely that mistakes will occur`.

This schema get a great performance to query because there are few joins to use. With indexed dimensional tables, the dabase optimizer get a best plan to query run.

The last benefit is the extent fo accommodate change. Every dimension table is equivalent into the fact table and the dimensional model has no built-in bias regarding expected query patterns. `You can add new dimension table to the schema
as long as a single value of that dimension is defined for each existing fact row from fact table`. Data would not need to be reloaded, and existing BI
applications would continue to run without yielding different results.

## Fact tables

The fact table in a dimensional model stores the performance measurements resulting from an organization’s business process events. `remember; the fact tables represents a business measure. You store the low-level measurement data resulting from a business process in a single dimensional model`. The volumen of data is overwhelmingly and represent the 90% of data in dimensional modeling, so then i don't duplicate in multiple places, then the all users access a central and consistent data  throughout the enterprise.

Like recommendation for the most usefull facts are numeric and additive; it can be aggregate in all dimensions, Like example sales units price are added to get a total price while you buying a product in market. Likely, the fact tables can be semi-additive; such as account balance, can't be summed across the time dimension or some dimensions; or Non-additive: such as unit price, can neve be added in all dimensions.

The textual measure are possible in theorical focus but in the practice, in general it is constraints into discrete list of values and the recomendation is to put it in dimension table. `you shouldn't store redundant textual information in fact table. Unless the text is unique for every row in the fact table, it belongs in the dimension table`. 

All fact tables have 2 or more foreign keys that connect to the dimension table' primary key. When all the keys in the fact table correctly match their respective primary keys in the corresponding dimension tables, the tables satisfy referential integrity. `The fact table generally has its own primary key composed of a subset of the foreign keys. This key is often called acomposite key. Every table that has a composite key is a fact table. This compositive key is unique for each row in fact tables`.

## Dimensional tables

`The dimension tables contain the textual context associated with a business process measurement event`. They describe the “who, what, where, when, how, and why” associated with the event.

The dimensional tables have a single primary key which serves as the basis for referential integrity with any given fact table. it is common for a dimenstion table to have many columns/attributes with few rows. Dimension attributes serve as the primary source of query constraints, group-ings, and report labels.

You should strive to minimize the use of codes in dimension tables by replacing them with more verbose textual attributes. You should make standard decodes for the operational codes available as dimension attributes to provide consistent labeling on queries, reports, and BI applications. You need to get embbeded structure from textual field into dimensional table. `In many ways, the data warehouse is only as good as the dimension attributes: The more time spent providing attributes with verbose business terminology, the better`. 

![Dimensiona tables sample with denormalized hierarchies](Images/DimensionTables.png?raw=true)

InDimensiona tables sample with denormalized hierarchies previous image,  shows that dimension tables often represent hie?raw=truerarchical relationships. For example, products roll up into brands and then into categories. For each row in the product dimension, you should store the associated brand and category description. The hierarchical descriptive information is stored redundantly in the spirit of ease of use and query performance. You should resist the perhaps habitual urge to normalize data by storing only the brand code in the product dimension and creating a separate brand lookup table, and likewise for the category description in a separate category lookup table. This normalization is called snowflaking. `The dimensional table are highly unnormalized with flattened many-to-one relationships within a single dimension table`. Using normalizin or snowflaking is almost always trade off for simplicity and accessibility in dimensional table.
 
# Arquitecture models

## Kimball arquitecture

This arquitecture has 4 components: operational source system, ETL system, presentation are and bi application.

![Kimball Arquitecture model](Images/KimballArquitecture.png?raw=true)

### Operation source system

Operational Source system capture the business's transactions with own format of data and indepent system to operational activities in enterprise. `The main prioroties of this system are processing performance and availability`. it has a little historical information, and the datawarehouse manage this situation.

### ETL system

ETL system is a work area wth a set of process to moving data from operational source system and Data warehouse. This system is focus in Extract-transform-load processes to build it. The transformation process can cleaning, combining from other source and deduplicate data; and you can use thses activities to create diagnostic meatadata, eventually leading to business process reengineering to improve data quality in the source system over time. `The primary mission of the ETL system os to hand off the dimension and fact table`.

Many of these defi ned subsystems focus on dimension table processing, such as surrogate key assignments, code lookups to provide appropriate descriptions, splitting, or combining columns to present the appropriate data values, or joining underlying third normal form table structures into flattened denormalized dimensions. In contrast, fact tables are typically large and time consuming to load, but preparing them for the presentation area is typically straightforward.

The ETL system is typically dominated by the simple activities of sorting and sequential processing to load data into presentation area's dimensional structure for querying and reporting.

### Presentation Area

`This area is where data is organized, stored and made available for direct querying by usersm report writers and other analytical BI applications`. The star schema or OLAP cube is used to implement this area and always have atomic data and optionally summaried data.

The presentation data area should be structured around business process measurement events and dimensional model should correspond to physical data capture events and it need to be cross all departments in enterprise.

### Business intelligence applications

The term BI application loosely refers to the range of capabilities provided to business users to leverage the presentation area for analytic decision making. A BI application can be as simple as an ad hoc query tool or as complex as a sophisticated data mining or modeling application.

## Alternative models

### Independent Data mart Architecture

With this approach, analytic data is deployed on a departamental basis without concern to sharing and integrating information across the enterprise. The departament work with IT staff to build a database that satisfies ther departamental need, reflecting their business rules and preferred labeling in isolation.

![Data mart architecture model](Images/DataMartArchitectureModel.png?raw=true)

This focus consuming resources to generate ETL system, unefficient don't get homogenous data to use between deparments and generate confusing all users, generate more work to operational source system to interact to get data.

### Hub and spoke corporate information Factory Inmmon Architecture

This focus is advocated by Bill Inmon and others in the industry. The follow image is a simplified version of this model.

![Inmon architecture Model](Images/InmonArchitectureModel.png?raw=true)

In this model, data is extracted ffrom the operational system and processed through an ETL system. The resulted atomic data from this process is loading in a 3NF database and this part is mandatory in this model, it is call Enterprise data warehouse (EDW). The kimball and Inmon model advocates a enterprise data coordination and integration same in Inmon the EDW fill this role and Kimball using enterprise bus with conformed dimensions. 

All users access to EDW to get detailed data, however subsequent ETL data delivery processes also populate downstream reporting and analytic environments to support business users with summary and departmentally data. 

### Hybrid hub and spoke and kimball architecture

This architecture is focus to mix kimball and inmon architecture. This architecture populates a Inmon models with centric EDW that is completely off-limits to business users for analysis and reporting. it is the source to populate a kimball-esque presentation area in which the data is dimensional, atomic, process-centric and conform to the enterprise data warehouse bus architecture.

![Mix kimball and Inmon architecture model into One](Images/HybridKimballAndInmonModel.png?raw=true)

This is the best of both worlds: it may leverage a preexisting investment in an integrated repository while addressing the performance and usability issues associated with the 3NF EDW by offloading queries to the dimensional presentation area to delivering data based on kimball tenets. If you've already invested in 3NF EDW and you need to improve in the speed and flexibility of analysis an reporting into users, this models is good.

# Techniques in Star modeling

## Techniques and concepts about fact tables 
There are techniques to define and build the fact tables inside star schema modeling.

### Fact Table `structure
`A fact table contain the numeric measures produced by an operational measurement event in the real world`. Each row has the lowest grain in event; and the fundamental design is entirely based on physical actitvity in real world.

The fact table always contains foreign keys for each of its associated dimensions; abd the primary target of the fact table to compute and dynamic aggreation arising from queries.

### Additive and Semi Additive and Non additive facts
The numeric measures in fact tables fall in 3 categories: **additive** es el most flexible and usefull, that it can be summed accross any of the associated dimensions. **Semi-additive**: It can be summed accross some dimensions but not all dimensions except time. **Non-additive**: it can't summed accross any of the associated dimensions.

A good approach for non-additive facts is, where possible, to store the fully additive components of the non-additive measure and sum these components into the fi nal answer set before calculating the fi nal non-additive fact.

### Nulls in Fact Tables
`Null-valued measurements behave gracefully in fact tables`. The aggregate functions all do the “right thing” with null facts. However, `nulls must be avoided in the fact table’s foreign keys because these nulls would automatically cause a referential integrity violation`. Rather than a null foreign key, the associated dimension table must have a default row (and surrogate key) representing the unknown or not applicable condition.

### Conformed Facts
`If the same measurement appears in separate fact tables, care must be taken to make sure the technical definitions of the facts are identical if they are to be compared or computed together`. If the separate fact definitions are consistent, the conformed facts should be identically named; but if they are incompatible, they should be differently named to alert the business users and BI applications.

### Transaction Fact Tables

`A row in a transaction fact table corresponds to a measurement event at a point in space and time`. Atomic transaction grain fact tables are the most dimensional and expressive fact tables; this robust dimensionality enables the maximum slicing and dicing of transaction data. Transaction fact tables may be dense or sparse because rows exist only if measurements take place. These fact tables always contain a foreign key for each associated dimension, and optionally contain precise time stamps and degenerate dimension keys. The measured numeric facts must be consistent with the transaction grain

### Periodic Snapshot Fact Tables

`A row in a periodic snapshot fact table summarizes many measurement events occurring over a standard period, such as a day, a week, or a month`. The grain is the period, not the individual transaction. Periodic snapshot fact tables often contain many facts because any measurement event consistent with the fact table grain is permissible. These fact tables are uniformly dense in their foreign keys because even if no activity takes place during the period, a row is typically inserted in the fact table containing a zero or null for each fact

### Accumulating Snapshot Fact Tables

`A row in an accumulating snapshot fact table summarizes the measurement events occurring at predictable steps between the beginning and the end of a process`. There is a date foreign key in the fact table for each critical milestone in the process. An individual row in an accumulating snapshot fact table, corresponding for instance to a line on an order, is initially inserted when the order line is created.  This consistent updating of accumulating snapshot fact rows is unique among the three types of fact tables. In addition to the date foreign keys associated with each critical process step, accumulating snapshot fact tables contain foreign keys for other dimensions and optionally contain degenerate dimensions. They often include numeric lag measurements consistent with the grain, along with milestone completion counters

### Factless Fact Tables
`Is possible that the event merely records a set of dimensional entities coming together at a moment in time`. For example, an event of a student attending a class on a given day may not have a recorded numeric fact, but a fact row with foreign keys for calendar day, student, teacher, location, and class is well-defined. 

These queries always have two parts: a factless coverage table that contains all the possibilities of events that might happen and an activity table that contains the events that did happen. When the activity is subtracted from the coverage, the result is the set of events that did not happen.

### Aggregate Fact Tables or OLAP Cubes
Aggregate fact tablesare simple numeric rollups of atomic fact table data built solely to accelerate query performance. These aggregate fact tables should be available to the BI layer at the same time as the atomic fact tables so that BI tools smoothly choose the appropriate aggregate level at query time.

### Consolidated Fact Tables
`It is often convenient to combine facts from multiple processes together into a single consolidatedfacttable if they can be expressed at the same grain`. Consolidated fact tables add bur-den to the ETL processing, but ease the analytic burden on the BI applications. They should be considered for cross-process metrics that are frequently analyzed together.

### Fact Table Surrogate Keys
Surrogate keys are used to implement the primary keys of almost all dimension tables. In addition, single column surrogate fact keys can be useful, albeit not required. `Fact table surrogate keys, which are not associated with any dimension, are assigned sequentially during the ETL load process` and are used 1) as the single column primary key of the fact table; 2) to serve as an immediate identifier of a fact table row without navigating multiple dimensions for ETL purposes; 3) to allow an interrupted load process to either back out or resume; 4) to allow fact table update operations to be decomposed into less risky inserts plus deletes.

### Centipede Fact Tables
`Some designers create separate normalized dimensions for each level of a many-to-one hierarchy, such as a date dimension, month dimension, quarter dimension, and year dimension, and then include all these foreign keys in a fact table. This results in a centipede fact table with dozens of hierarchically related dimensions. Centipede fact tables should be avoided`. All these fixed depth, many-to-one hierarchically related dimensions should be collapsed back to their unique lowest grains, such as the date for the example mentioned. Centipede fact tables also result when designers embed numerous foreign keys to individual low-cardinality dimension tables rather than creating a junk dimension.

### Numeric Values as Attributes or Facts
`Designers sometimes encounter numeric values that don’t clearly fall into either the fact or dimension attribute categories`. A classic example is a product’s standard list price. If the numeric value is used primarily for calculation purposes, it likely belongs in the fact table. If a stable numeric value is used predominantly for filtering and grouping, it should be treated as a dimension attribute; the discrete numeric values can be supplemented with value band attributes (such as $0-50). `In some cases, it is useful to model the numeric value as both a fact and dimension attribute, such as a quantitative on-time delivery metric and qualitative textual descriptor`.

### Lag or duration facts
`Accumulating snapshot fact tables capture multiple process milestones, each with a date foreign key and possibly a date/time stamp. Business users often want to analyze the lags or durations between these milestones; sometimes these lags are just the differences between dates, but other times the lags are based on more complicated business rules`. If there are dozens of steps in a pipeline, there could be hundreds of possible lags. Rather than forcing the user’s query to calculate each possible lag from the date/time stamps or date dimension foreign keys, just one time lag can be stored for each step measured against the process’s start point. Then every possible lag between two steps can be calculated as a simple subtraction between the two lags stored in the fact table.

### Header or Line Fact Tables
Operational transaction systems often consist of a transaction header row that’s associated with multiple transaction lines. With header/line schemas (also known as parent/child schemas), all the header-level dimension foreign keys and degenerate dimensions should be included on the line-level fact table.

### Allocated Facts
`It is quite common in header/line transaction data to encounter facts of diff er-ing granularity, such as a header freight charge. You should strive to allocatethe header facts down to the line level based on rules provided by the business, so the allocated facts can be sliced and rolled up by all the dimensions`. In many cases, you can avoid creating a header-level fact table, unless this aggregation delivers query performance advantages.

### Profit and Loss Fact Tables Using Allocations
`Fact  tables that expose the full equation of profit are among the most powerful deliverables of an enterprise DW/BI system`. The equation of profit is (revenue) – (costs) = (profit). `Fact tables ideally implement the profit equation at the grain of the atomic revenue transaction and contain many components of cost`. Because these tables are at the atomic grain, numerous rollups are possible, including customer profitability, product profitability, promotion profitability, channel profitability, and others. However, `these fact tables are difficult to build because the cost components must be allocated from their original sources to the fact table’s grain. This allocation step is often a major ETL subsystem and is a politically charged step that requires high-level executive support`. For these reasons, profit and loss fact tables are typically not tackled during the early implementation phases of a DW/BI program.

### Multiple Currency Facts
`Fact  tables that record financial transactions in multiple currencies should contain a pair of columns for every financial fact in the row`. One column contains the fact expressed in the true currency of the transaction, and the other contains the same fact expressed in a single standard currency that is used throughout the fact table. The standard currency value is created in an ETL process according to an approved business rule for currency conversion. This fact table also must have a currency dimension to identify the transaction’s true currency.

### Multiple Units of Measure Facts
`Some  business processes require facts to be stated simultaneously in several units of measure`. If the fact table contains a large number of facts, each of which must be expressed in all units of measure, a convenient technique is to store the facts once in the table at an agreed standard unit of measure, but also simultaneously store conversion factors between the standard measure and all the others.

### Year-to-Date Facts
`Business  users often request year-to-date (YTD) values in a fact table. It is hard to argue against a single request, but YTD requests can easily morph into “YTD at the close of the fiscal period” or “fiscal period to date”`. A more reliable, extensible way to handle these assorted requests is to calculate the YTD metrics in the BI applications or OLAP cube rather than storing YTD facts in the fact table.

### Multipass SQL to Avoid Fact-to-Fact Table Joins
`A BI application must never issue SQL that joins two fact tables together across the fact table’s foreign keys`. It is impossible to control the cardinality of the answer set of such a join in a relational database, and incorrectresults will be returned to the BI tool.  For instance, if two fact tables contain customer’s product shipments and returns, these two fact tables must not be joined directly across the customer and product foreign keys. `Instead, the technique of drilling across two fact tables should be used, where the answer sets from shipments and returns are separately created, and the results sort-merged on the common row header attribute values to produce the correct result`.

### Timespan Tracking in Fact Tables
There are three basic fact table grains: transaction, periodic snapshot, and accumulating snapshot. `In isolated cases, it is useful to add a row effective date, row expiration date, and current row indicator to the fact table, much like you do with type 2 slowly changing dimensions, to capture a timespan when the fact row was effective`. Although an unusual pattern, this pattern addresses scenarios such as slowly changing inventory balances where a frequent periodic snapshot would load identical rows with each snapshot. 

### Late Arriving Facts
`A fact row is late arriving if the most current dimensional context for new fact rows does not match the incoming row`. This happens when the fact row is delayed. In this case, the relevant dimensions must be searched to find the dimension keys that were effective when the late arriving measurement event occurred.

## Techniques and concepts about Dimension Tables
There are techniques to define and build the dimension tables inside star schema modeling.

### Dimension Table Structure

Every  dimension table has a single primary key column. This primary key is embedded as a foreign key in any associated fact table where the dimension row’s descriptive context is exactly correct for that fact table row. Dimension tables are usually wide, fl at denormalized tables with many low-cardinality text attributes. Dimension table attributes are the primary target of constraints and grouping specifi cations from queries and BI applications. 

### Dimension Surrogate Keys
A dimension table is designed with one column serving as a unique primary key. This primary key cannot be the operational system’s natural key because there will be multiple dimension rows for that natural key when changes are tracked over time. In addition, natural keys for a dimension may be created by more than one source system, and these natural keys may be incompatible or poorly administered. The DW/BI system needs to claim control of the primary keys of all dimensions; rather than using explicit natural keys or natural keys with appended dates, you should create anonymous integer primary keys for every dimension. These dimension surrogate keys are simple integers, assigned in sequence, starting with the value 1, every time a new key is needed.

### Natural and Durable and Supernatural Keys
**Natural keys** created by  operational source systems are subject to business rules outside the control of the DW/BI system. 

When the data warehouse system wants to have a single natural key, it's using a **durable key**, this is a persistent and unchanged key in system. Other name for this key is Supernatural key. The best durable keys have a format that is independent of the original business process and thus should be simple integers assigned in sequence beginning with 1. While multiple surrogate keys may be associated, the durable key never changes.

### Drilling Down
Drilling downis the most fundamental way data is analyzed by business users. Drilling down simply means adding a row header to an existing query; the new row header is a dimension attribute appended to the GROUP BY expression in an SQL query. The attribute can come from any dimension attached to the fact table in the query. Drilling down does not require the defi  nition of predetermined hierarchies or drill-down paths.

### Degenerate Dimensions
Sometimes  a dimension is defi ned that has no content except for its primary key. For example, when an invoice has multiple line items, the line item fact rows inherit all the descriptive dimension foreign keys of the invoice, and the invoice is left with no unique content. But the invoice number remains a valid dimension key for fact tables at the line item level. This degenerate dimension is placed in the fact table with the explicit acknowledgment that there is no associated dimension table. Degenerate dimensions are most common with transaction and accumulating snapshot fact tables.

### Denormalized Flattened Dimensions
In  general, dimensional designers must resist the normalization urges caused by years of operational database designs and instead denormalize the many-to-one fi xed depth hierarchies into separate attributes on a fl attened dimension row. Dimension denormalization supports dimensional modeling’s twin objectives of simplicity and speed.

###  Multiple Hierarchies in Dimensions
Many  dimensions contain more than one natural hierarchy. For example, calendar date dimensions may have a day to week to fi scal period hierarchy, as well as a day to month to year hierarchy. Location intensive dimensions may have multiple geographic hierarchies. In all of these cases, the separate hierarchies can gracefully coexist in the same dimension table.

### Flags and Indicators as Textual Attributes
Cryptic  abbreviations, true/false fl ags, and operational indicators should be sup-plemented in dimension tables with full text words that have meaning when independently viewed. Operational codes with embedded meaning within the code value should be broken down with each part of the code expanded into its own separate descriptive dimension attribute.

### Null Attributes in Dimensions
Null-valued  dimension attributes result when a given dimension row has not been fully populated, or when there are attributes that are not applicable to all the dimension’s rows. In both cases, we recommend substituting a descriptive string, such as Unknown or Not Applicable in place of the null value. Nulls in dimension attributes should be avoided because diff erent databases handle grouping and constraining on nulls inconsistently.

### Role-Playing Dimensions
A single physical dimension can be referenced multiple times in a fact table, with each reference linking to a logically distinct role for the dimension. For instance, a fact table can have several dates, each of which is represented by a foreign key to the date dimension. It is essential that each foreign key refers to a separate view of the date dimension so that the references are independent. These separate dimen-sion views (with unique attribute column names) are called roles.

### Junk Dimensions
Transactional  business processes typically produce a number of miscellaneous, low-cardinality fl ags and indicators. Rather than making separate dimensions for each fl ag and attribute, you can create a single junk dimension combining them together. This dimension, frequently labeled as a transaction profi le dimension in a schema, does not need to be the Cartesian product of all the attributes’ possible values, but should only contain the combination of values that actually occur in the source data

### Snowflaked Dimensions

When  a hierarchical relationship in a dimension table is normalized, low-cardinal-ity attributes appear as secondary tables connected to the base dimension table by an attribute key. When this process is repeated with all the dimension table’s hierarchies, a characteristic multilevel structure is created that is called a snowflake. Although the snowflake represents hierarchical data accurately, you should avoid snowflakes because it is difficult for business users to understand and navigate snowflakes. They can also negatively impact query performance. A flattened denormalized dimension table contains exactly the same information as a snowflaked dimension.

### Outrigger Dimensions
A dimension can contain a reference to another dimension table. For instance, a bank account dimension can reference a separate dimension representing the date the account was opened. These secondary dimension references are called outrigger dimensions. Outrigger dimensions are permissible, but should be used sparingly. In most cases, the correlations between dimensions should be demoted to a fact table, where both dimensions are represented as separate foreign keys.

### Dimension-to-Dimension Table Joins
`Dimensions can contain references to other dimensions`. Although these relationships can be modeled with outrigger dimensions, in some cases, the existence of a
foreign key to the outrigger dimension in the base dimension can result in explosive growth of the base dimension because type 2 changes in the outrigger force corresponding type 2 processing in the base dimension. `This explosive growth can often be avoided if you demote the correlation between dimensions by placing the
foreign key of the outrigger in the fact table rather than in the base dimension`. This means the correlation between the dimensions can be discovered only by traversing the fact table, but this may be acceptable, especially if the fact table is a periodic snapshot where all the keys for all the dimensions are guaranteed to be present for each reporting period.

### Multivalued Dimensions and Bridge Tables
`In a classic dimensional schema, each dimension attached to a fact table has a single value consistent with the fact table’s grain. But there are a number of situations in which a dimension is legitimately multivalued`. For example, a patient receiving a healthcare treatment may have multiple simultaneous diagnoses. In `these cases, the multivalued dimension must be attached to the fact table through a group dimension key to a bridge table with one row for each simultaneous diagnosis in a group`.

### Time Varying Multivalued Bridge Tables
`A multivalued bridge table may need to be based on a type 2 slowly changing dimension`. For example, the bridge table that implements the many-to-many relationship between bank accounts and individual customers usually must be based on type 2 account and customer dimensions. `In this case, to prevent incorrect linkages between accounts and customers, the bridge table must include effective and expiration date/time stamps`, and the requesting application must constrain the bridge table to a specific moment in time to produce a consistent snapshot.

### Behavior Tag Time Series
`Almost all text in a data warehouse is descriptive text in dimension tables. Data mining customer cluster analyses typically results in textual behavior tags, often identified on a periodic basis`. In this case, the customers’ behavior measurements over time become a sequence of these behavior tags; `this time series should be stored as positional attributes in the customer dimension, along with an optional text string for the complete sequence of tags`. The behavior tags are modeled in a positional design because the behavior tags are the target of complex simultaneous queries rather than numeric computations.

### Behavior Study Groups
`Complex customer behavior can sometimes be discovered only by running lengthy iterative analyses. In these cases, it is impractical to embed the behavior analyses inside every BI application that wants to constrain all the members of the customer dimension 
who exhibit the complex behavior`. The results of the complex behavior analyses, however, `can be captured in a simple table, called a study group, consisting only of the customers’ durable keys. This static table can then be used as a kind of filter on any dimensional schema with a customer dimension by constraining the study group column to the customer dimension’s durable key in the target schema at query time`. Multiple study groups can be defined and derivative study groups can be created with intersections, unions, and set differences.

### Aggregated Facts as Dimension Attributes
`Business users are often interested in constraining the customer dimension based on aggregated performance metrics`, such as filtering on all customers who spent over a certain dollar amount during last year or perhaps over the customer’s lifetime. `Selected aggregated facts can be placed in a dimension as targets for constraining and as row labels for reporting`. The metrics are often presented as banded ranges in the dimension table. `Dimension attributes representing aggregated performance metrics add burden to the ETL processing, but ease the analytic burden in the BI layer`.

### Dynamic Value Bands
`A dynamic value banding report is organized as a series of report row headers that defi ne a progressive set of varying-sized ranges of a target numeric fact`. For instance, a common value banding report in a bank has many rows with labels such as “Balance from 0 to $10,” “Balance from $10.01 to $25,” and so on. `This kind of report is dynamic because the specific row headers are defined at query time, not during the ETL processing`. The row definitions can be implemented in a small value banding dimension table that is joined via greater-than/less-than joins to the fact table, or the definitions can exist only in an SQL CASE statement. The value banding dimension approach is probably higher performing, especially in a columnar database, because the CASE statement approach involves an almost unconstrained relation scan of the fact table.

### Text Comments Dimension
`Rather  than treating freeform comments as textual metrics in a fact table, they should be stored outside the fact table in a separate comments dimension` (or as attributes in a dimension with one row per transaction if the comments’ cardinality matches the number of unique transactions) with a corresponding foreign key in the fact table.

### Multiple Time Zones
To capture both universal standard time, as well as local times in multi-time zone applications, dual foreign keys should be placed in the affected fact tables that join to two role-playing date (and potentially time-of-day) dimension tables.

### Measure Type Dimensions
`Sometimes  when a fact table has a long list of facts that is sparsely populated in any individual row, it is tempting to create a measure type dimension that collapses the fact table row down to a single generic fact identified by the measure type dimension`. We generally do not recommend this approach. Although it removes all the empty fact columns, it multiplies the size of the fact table by the average number of occupied columns in each row, and it makes intra-column computations much more difficult. This technique is acceptable when the number of potential facts is extreme (in the hundreds), but less than a handful would be applicable to any given fact table row.

### Step Dimensions
`Sequential  processes, such as web page events, normally have a separate row in a transaction fact table for each step in a process`. To tell where the individual step fits into the overall session, a step dimension is used that shows what step number is represented by the current step and how many more steps were required to complete the session.

### Hot Swappable Dimensions
`Hot swappable dimensionsare used when the same fact table is alternatively paired with different copies of the same dimension`. For example, a single fact table containing stock ticker quotes could be simultaneously exposed to multiple separate investors, each of whom has unique and proprietar y attributes assigned to different stocks.

### Abstract Generic Dimensions
`Some  modelers are attracted to abstract generic dimensions. For example, their schemas include a single generic location dimension rather than embedded geographic attributes in the store, warehouse, and customer dimensions`. Similarly, their person dimension includes rows for employees, customers, and vendor contacts because they are all human beings, regardless that significantly different attributes are collected for each type. `Abstract generic dimensions should be avoided in dimensional models. The attribute sets associated with each type often differ. If the attributes are common, such as a geographic state, then they should be uniquely labeled to distinguish a store’s state from a customer’s`. Finally, dumping all varieties of locations, people, or products into a single dimension invariably results in a larger dimension table. `Data abstraction may be appropriate in the operational source system or ETL processing, but it negatively impacts query performance and legibility in the dimensional model`.

### Audit Dimensions
`When a fact table row is created in the ETL back room, it is helpful to create an audit dimension containing the ETL processing metadata known at the time. A simple audit dimension row could contain one or more basic indicators of data quality, perhaps derived from examining an error event schema that records data quality violations encountered while processing the data`. Other useful audit dimension attributes could include environment variables describing the versions of ETL code used to create the fact rows or the ETL process execution time stamps. 
`These environment variables are especially useful for compliance and auditing purposes` because they enable BI tools to drill down to determine which rows were created with what versions of the ETL software. 

### Late Arriving Dimensions
`Sometimes the facts from an operational business process arrive minutes, hours, days, or weeks before the associated dimension context`. For example, in a real-time data delivery situation, an inventory depletion row may arrive showing the natural key of a customer committing to purchase a particular product. `In a real-time ETL system, this row must be posted to the BI layer, even if the identity of the customer or product cannot be immediately determined. In these cases, special dimension rows are created with the unresolved natural keys as attributes. Of course, these dimension rows must contain generic unknown values for most of the descriptive columns; presumably the proper dimensional context will follow from the source at a later time`. When this dimensional context is eventually supplied, the placeholder dimension rows are updated with type 1 overwrites. Late arriving dimension data also occurs when retroactive changes are made to type 2 dimension attributes. In this case, a new row needs to be inserted in the dimension table, and then the associated fact rows must be restated

## Integration via Conformed Dimensions
Techniques to integrate data from diff erent business processes.

### Conformed Dimensions
Dimension tables conform when attributes in separate dimension tables have the same column names and domain contents. Information from separate fact tables can be combined in a single report by using conformed dimension attributes that are associated with each fact table. When a conformed attribute is used as the row header (that is, the grouping column in the SQL query), the results from the separate fact tables can be aligned on the same rows in a drill-across report. This is the essence of integration in an enterprise DW/BI system. Conformed dimensions, defined once in collaboration with the business’s data governance representatives, are reused across fact tables; they deliver both analytic consistency and reduced future development costs because the wheel is not repeatedly re-create.

### Shrunken Dimensions
Shrunken dimensions are conformed dimensions that are a subset of rows and/or columns of a base dimension. Shrunken rollup dimensions are required when constructing aggregate fact tables. They are also necessary for business processes that naturally capture data at a higher level of granularity, such as a forecast by month and brand (instead of the more atomic date and product associated with sales data). 

Another case of conformed dimension subsetting occurs when two dimensions are at the same level of detail, but one represents only a subset of rows

### Drilling Across
Drilling across simply means making separate queries against two or more fact tables where the row headers of each query consist of identical conformed attributes. The answer sets from the two queries are aligned by performing a sort-merge operation on the common dimension attribute row headers. BI tool vendors refer to this functionality by various names, including stitch and multipass query.

### Value Chain
A value chain identifies the natural flow of an organization’s primary business processes. For example, a retailer’s value chain may consist of purchasing to warehousing to retail sales. A general ledger value chain may consist of budgeting to commitments to payments. Operational source systems typically produce transactions or snapshots at each step of the value chain. Because each process produces unique metrics at unique time intervals with unique granularity and dimensionality, each process typically spawns at least one atomic fact table.

### Enterprise Data Warehouse Bus Architecture
The enterprise data warehouse bus architecture provides an incremental approach to building the enterprise DW/BI system. `This architecture decomposes the DW/BI planning process into manageable pieces by focusing on business processes, while delivering integration via standardized conformed dimensions that are reused across processes`. It provides an architectural framework, while also decomposing the program to encourage manageable agile implementations corresponding to the rows on the enterprise data warehouse bus matrix. The bus architecture is technology and database platform independent; both relational and OL AP dimensional structures can participate. 

### Enterprise Data Warehouse Bus Matrix
`The enterprise data warehousebus matrix is a tool for designing and communicating the enterprise data warehouse bus architecture`. The rows of the matrix are business processes and the columns are dimensions. `The shaded cells of the matrix indicate whether a dimension is associated with a given business process`. The design team scans each row to test whether a candidate dimension is well-defined for the business process and also scans each column to see where a dimension should be conformed across multiple business processes. Besides the technical design considerations, the bus matrix is used as input to prioritize DW/BI projects with business management as teams should implement one row of the matrix at a time.

### Detailed Implementation Bus Matrix
`The detailed implementation bus matrix is a more granular bus matrix where each business process row has been expanded to show specific fact tables or OLAP cubes`. At this level of detail, the precise grain statement and list of facts can be documented.

### Opportunity or Stakeholder Matrix
After  the enterprise data warehouse bus matrix rows have been identified, you can draft a different matrix by replacing the dimension columns with business functions, such as marketing, sales, and finance, and then shading the matrix cells to indicate which business functions are interested in which business process rows.

It helps identify which business groups should be invited to the collaborative design sessions for each process-centric row.

## Dealing with Slowly Changing Dimension Attributes
 It is quite common to have attributes in the same dimension table that are handled with diff erent change tracking techniques.
 
### Type 0 or Retain Original
With type 0, `the dimension attribute value never changes`, so facts are always grouped by this original value. Type 0 is appropriate for any attribute labeled “original,” such as a customer’s original credit score or a durable identifier.

### Type 1 or Overwrite
With type 1, `the old attribute value in the dimension row is overwritten with the new value; type 1 attributes always reflects the most recent assignment, and therefore this technique destroys history`. Although this approach is easy to implement and does not create additional dimension rows, you must be careful that aggregate fact tables and OLAP cubes affected by this change are recomputed.

### Type 2 or Add New Row
Type 2 changes `add a new row in the dimension with the updated attribute values`. This requires generalizing the primary key of the dimension beyond the natural or durable key because there will potentially be multiple rows describing each member.
When a new row is created for a dimension member, a new primary surrogate key is assigned and used as a foreign key in all fact tables from the moment of the update until a subsequent change creates a new dimension key and updated dimension row. A minimum of three additional columns should be added to the dimension row with type 2 changes: 1) row effective date or date/time stamp; 2) row expiration date or date/time stamp; and 3) current row indicator.

### Type 3 or Add New Attribute
Type 3 changes `add a new attribute in the dimension to preserve the old attribute value; the new value overwrites the main attribute as in a type 1 change`. This kind of type 3 change is sometimes called an alternate reality. A business user can group and filter fact data by either the current value or alternate reality. This slowly changing dimension technique is used relatively infrequently.

### Type 4 or Add Mini Dimension
The type 4 technique `is used when a group of attributes in a dimension rapidly changes and is split off to a mini-dimension`. This situation is sometimes called a rapidly changing monster dimension. Frequently used attributes in multimillion-row dimension tables are mini-dimension design candidates, even if they don’t frequently change. The type 4 mini-dimension requires its own unique primary key; the primary keys of both the base dimension and mini-dimension are captured in the associated fact tables.

### Type 5 or Add Mini-Dimension and Type 1 Outrigger
The type 5 technique `is used to accurately preserve historical attribute values, plus report historical facts according to current attribute values. Type 5 builds on the type 4 mini-dimension by also embedding a current type 1 reference to the mini-dimension in the base dimension`. This enables the currently-assigned mini-dimension attributes to be accessed along with the others in the base dimension without linking through a fact table. Logically, you’d represent the base dimension and mini-dimension outrigger as a single table in the presentation area. The ETL team must overwrite this type 1 mini-dimension reference whenever the current mini-dimension assignment changes.

### Type 6 or Add Type 1 Attributes to Type 2 Dimension
`type 6 delivers both historical and current dimension attribute values`. Type 6 builds on the type 2 technique by also embedding current type 1 versions of the same attributes in the dimension row so that fact rows can be filtered or grouped by either the type 2 attribute value in effect when the measurement occurred or the attribute’s current value. In this case, the type 1 attribute is systematically overwritten on all rows associated with a particular durable key whenever the attribute is updated.

### Type 7 or Dual Type 1 and Type 2 Dimensions
Type 7 is the final hybrid technique used to support both as-was and as-is reporting. A fact table can be accessed through a dimension modeled both as a type 1 dimension showing only the most current attribute values, or as a type 2 dimension showing correct contemporary historical profiles. The same dimension table enables both perspectives. Both the durable key and primary surrogate key of the dimension are placed in the fact table. For the type 1 perspective, the current flag in the dimension is constrained to be current, and the fact table is joined via the durable key. For the type 2 perspective, the current flag is not constrained, and the fact table is joined via the surrogate primary key. These two perspectives would be deployed as separate views to the BI applications

## Approaches for Dimension Hierarchies
This section describes approaches for dealing with hierarchies, starting with the most basic.

### Fixed Depth Positional Hierarchies
`A fixed depth hierarchy is a series of many-to-one relationships, such as product to brand to category to department`. the hierarchy levels should appear as separate positional attributes in a dimension table. A fixed depth hierarchy is by far the easiest to understand and navigate as long as the above criteria are met. It also delivers predictable and fast query performance.

### Slightly Ragged or Variable Depth Hierarchies
`Slightly ragged hierarchies don’t have a fixed number of levels, but the range in depth is small`. Geographic hierarchies often range in depth from perhaps three levels to six levels. Rather than using the complex machinery for unpredictably variable hierarchies, you can force-fit slightly ragged hierarchies into a fixed depth positional design with separate dimension attributes for the maximum number of levels, and then populate the attribute value based on rules from the business.

### Ragged or Variable Depth Hierarchies with Hierarchy Bridge Tables
`Ragged hierarchies of indeterminate depth are difficult to model and query in a relational database`. Although SQL extensions and OLAP access languages provide some support for recursive parent/child relationships, these approaches have limitations. With SQL extensions, alternative ragged hierarchies cannot be substituted at query time, shared ownership structures are not supported, and time varying ragged hierarchies are not supported. `All these objections can be overcome in relational databases by modeling a ragged hierarchy with a specially constructed bridge table`. This bridge table contains a row for every possible path in the ragged hierarchy and enables all forms of hierarchy traversal to be accomplished with standard SQL rather than using special language extensions.

### Ragged or Variable Depth Hierarchies with Pathstring Attributes
`The  use of a bridge table for ragged variable depth hierarchies can be avoided by implementing a pathstring attribute in the dimension. For each row in the dimension, the pathstring attribute contains a specially encoded text string containing the complete path description from the supreme node of a hierarchy down to the node described by the particular dimension row`. Many of the standard hierarchy analysis requests can then be handled by standard SQL, without resorting to SQL language extensions. However, the pathstring approach does not enable rapid sub-stitution of alternative hierarchies or shared ownership hierarchies. The pathstring approach may also be vulnerable to structure changes in the ragged hierarchy that could force the entire hierarchy to be relabeled.

# Special Purpose Schemas
The following design patterns are needed for specific use cases.

## Supertype and Subtype Schemas for Heterogeneous Products
`Financial services and other businesses frequently offer a wide variety of products in disparate lines of business`. For example, a retail bank may offer dozens of types of accounts ranging from checking accounts to mortgages to business loans, but all are examples of an account. Attempts to build a single, consolidated fact table with the union of all possible facts, linked to dimension tables with all possible attributes of these divergent products, will fail because there can be hundreds of incompatible facts and attributes.
`The solution is to build a single supertype fact table that has the intersection of the facts from all the account types (along with a supertype dimension table containing the common attributes), and then systematically build separate fact tables (and associated dimension tables) for each of the subtypes`. Supertype and subtype fact tables are also called core and custom fact tables

## Real-Time Fact Tables
`Real-time fact tables need to be updated more frequently than the more traditional nightly batch process. There are many techniques for supporting this requirement`, depending on the capabilities of the DBMS or OLAP cube used for final deployment to the BI reporting layer. For example, a “hot partition” can be defined on a fact table that is pinned in physical memory. Aggregations and indexes are deliberately not built on this partition. Other DBMSs or OLAP cubes may support deferred updating that allows existing queries to run to completion but then perform the updates.

## Error Event Schemas
Managing data quality in a data warehouse requires a comprehensive system of data quality screens or filters that test the data as it flows from the source systems to the BI platform. When a data quality screen detects an error, this event is recorded in a special dimensional schema that is available only in the ETL back room. `This schema consists of an error event fact table whose grain is the individual error event and an associated error event detail fact table whose grain is each column in each table that participates in an error event`.
