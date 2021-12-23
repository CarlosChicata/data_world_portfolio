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


# Dimensional modeling introduction
## General issues in dimensional modeling
This technique to analyze data because it addresses two simultaneous requirements: deliver data fast and understandable to the business users by make simple database from complex data base.

The dimensional modeling and 3NF models (or called ERD model) are compared in query performance issues, but the main diferent is in the degree of normalization: the RDMS can't efficiently query a efficient normalized data model, so you need to some degree of unnormalize into those queries.

## Star schema vs OLAP cube

The dimensional models implemented in RDMS are referred to as Star schema while the dimensional models implemented in Multidimensional Database are referred to as OLAP Cubes.

![Start schema and OLAP Cube](Images/StarSchemaVsOLAPCube.png?raw=true)

The OLAP cube is stored and indexed using techniques for dimensional data, performance aggregations or precalculated summary tables are created and managed by the OLAP cube engine and this deliver super query performances, flexibility to analyze and robust functions that exceed those available with SQL. The downside is that you pay a load performance price in generate this cube, especially with large data sets.


# Star schema modeling

## Fact tables

The fact table in a dimensional model stores the performance measurements resulting from an organization’s business process events. `remember; the fact tables represents a business measure. You store the low-level measurement data resulting from a business process in a single dimensional model`. The volumen of data is overwhelmingly and represent the 90% of data in dimensional modeling, so then i don't duplicate in multiple places, then the all users access a central and consistent data  throughout the enterprise.

Like recommendation for the most usefull facts are numeric and additive; it can be aggregate in all dimensions, Like example sales units price are added to get a total price while you buying a product in market. Likely, the fact tables can be semi-additive; such as account balance, can't be summed across the time dimension or some dimensions; or Non-additive: such as unit price, can neve be added in all dimensions.

The textual measure are possible in theorical focus but in the practice, in general it is constraints into discrete list of values and the recomendation is to put it in dimension table. `you shouldn't store redundant textual information in fact table. Unless the text is unique for every row in the fact table, it belongs in the dimension table`. 

All fact tables have 2 or more foreign keys that connect to the dimension table' primary key. When all the keys in the fact table correctly match their respective primary keys in the corresponding dimension tables, the tables satisfy referential integrity. `The fact table generally has its own primary key composed of a subset of the foreign keys. This key is often called acomposite key. Every table that has a composite key is a fact table. This compositive key is unique for each row in fact tables`.

## Dimensional tables



