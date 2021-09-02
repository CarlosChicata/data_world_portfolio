# Data warehouse
======================================

## Purpose
Contain all concepts, best practices, patterns, architectures and concepts about data warehouse i learned.


## Index of readme
This is a index to best navigation inside document.

- [The problems of external data sources: unified storage of data](#the-problems-of-external-data-sources)
- [References](#references)



# The problems of external data sources
You wanna extract data of external sources to analyze them to get insight/knowledge. The extract process is good for 2 reason:
* don't degrade the performance of the source system when you need to analyze in mass.
* control this data because you move this data into your system.

But you will have a problem if you don't structure a unified infraestructure to store this data:
![alt text](ExtractDataFromExternalProblem.png?raw=true)

Based in above image, we have 3 problems in this bad infraestructure:
* Lack of credibility: if 2 departments generate a report same focus, it's possibly both are difference in results, because both use difference data source in their report. there are some reason associated:
  * Change data continually in all sources.
  * Sources can have difference type of data.
  * Don't share sources in all department.
  * When you extract data of external, i need to capture of identity source to accredit those data.
* Productivity low: it's so hard to access and processing several sources in diference locations inside organization.
* From data to information: it's so hard to reconciliate and normalize structure of data from several different sources to generate a column in report.


# References
1.   build of data warehouse, fourth edition. W. H. Inmon. 2005. page: 5-14
