# Exchange money accounts

## Project Information 
Contain all information about the project from business view.

### Fictitious context :information_source:

You're working in startup project related about exchange and transaction money called **Kambiazo**. In this system, a new user create account based in predeterminated plans to make operations (withdraw and deposit) in his money. All transaction is based in exchange in this moment, because it's part of business model to be the financial institute with the lowest interest in country.

This institute get all exchange using [Free forex API](https://freeforexapi.com/Home/Api) and its  own system to managemente financial transactionals. They ask you that build a system to analyze all done operations in interval of 5 minutes and generate metrics based in this.


### Goals of project :dart:

1. Build a infraestructure to store and queries data.
2. Request and implement metrics from data analytics to business.
3. Generate documents to navigate in data to make queries.

### Technical and functional considerations :eyes:

1. The metrics need to be update in interval of 5 minutes. it can be re-assigned between 1 hour to 3 minutes.
2. You need to integrate API to get exchange. It need to be queries each 30 seconds.
3. You need to manage historical data. Data will be considerate historical with 1 week of age in system but it can be re-assigned dynamically between 1 month to 3 days.
4. All users need to document to understand models.


## Development project
Contain general topics of project from technical view. If you need more specificated topics you need to go "navigation" section to check what part you need to come in.

### Skills i need to :mechanic:
* Design, Build and document a dimensiona model to soport ad-hoc queries by end users.
* Design, Build and document a infraestructure to support data ingestion and storage.
* Show domain in several cloud tools of GCP.
* Document and implement metrics based in business alignment.
* Design and implement data entry to management documents and configurations.

### Topic skills i will show
* Documentation of project.
* Using tools: Infraestructure as Code, Python 3, HTTP, etc.
* Data architecture.
* Data modeling.
* Data ingestation.
* Cloud Services In GCP.
* Best practice in programming.

### Diagram of project
This is diagram of infraestructure in project.
![Diagram of infraestructure](https://github.com/CarlosChicata/data_world_portfolio/blob/main/Projects/exchange_money_accounts/Diagram%20of%20arquitecture.png?raw=true)

### Version of project
| Number of versión | New feature |
| ------------------|-------------|
| 0.0.1             | Definition of projects | 
