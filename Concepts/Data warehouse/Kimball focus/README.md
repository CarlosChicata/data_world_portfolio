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

