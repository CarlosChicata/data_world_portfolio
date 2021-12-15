# Data warehouse based in Kimball focus.

======================================

## Purpose
Contain all concepts, best practices, patterns, architectures and concepts about data warehouse i learned based in kimball focus


## Index of readme
This is a index to best navigation inside document.

- [Dimensional modeling introduction](#dimensional-modeling-introduction)
  - [General issues in dimensional modeling](#general-issues-in-dimensional-modeling)
  - [Star schema vs OLAP cube](#star-schema-vs-olap-cube)

# Dimensional modeling introduction
## General issues in dimensional modeling
This technique to analyze data because it addresses two simultaneous requirements: deliver data fast and understandable to the business users by make simple database from complex data base.

The dimensional modeling and 3NF models (or called ERD model) are compared in query performance issues, but the main diferent is in the degree of normalization: the RDMS can't efficiently query a efficient normalized data model, so you need to some degree of unnormalize into those queries.

## Star schema vs OLAP cube

The dimensional models implemented in RDMS are referred to as Star schema while the dimensional models implemented in Multidimensional Database are referred to as OLAP Cubes.

![Start schema and OLAP Cube](Images/StarSchemaVsOLAPCube.png?raw=true)

The OLAP cube is stored and indexed using techniques for dimensional data, performance aggregations or precalculated summary tables are created and managed by the OLAP cube engine and this deliver super query performances, flexibility to analyze and robust functions that exceed those available with SQL. The downside is that you pay a load performance price in generate this cube, especially with large data sets.
