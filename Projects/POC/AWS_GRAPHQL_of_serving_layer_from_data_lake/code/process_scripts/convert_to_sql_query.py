mapper = {
   "Client": {
       "table": "client_table",
       "database": "db-poc-case-1"
   },
   "cityID": {
       "table": "city_table",
       "database": "db-poc-case-1"
   },
   "countryID":  {
       "table": "country_table",
       "database": "db-poc-case-1"
   }
}

gql_formatter_2 =  {
    'field': ['commercialName', 'enterprise_key'], 
    'name': 'Client', 
    'node': [
        {
            'field': ['id', 'name'], 
            'name': 'cityID', 
            'node': [
                {
                    'field': ['currencyISO', 'id', 'name'], 
                    'name': 'countryID', 
                    'node': []
                }
            ]
        }, 
        {
            'field': ['secondaryDirection'], 
            'name': 'address', 
            'node': [
                {
                    'field': ['name', 'CP'], 
                    'name': 'direction', 
                    'node': []
                }
            ]
        }
    ]
}

gql_formatter_1 = {
    'field': ['address', 'commercialName', 'enterprise_key'], 
    'name': 'Client', 
    'node': [
        {
            'field': ['id', 'name'], 
            'name': 'cityID', 
            'node': [
                {
                    'field': ['currencyISO', 'id', 'name'], 
                    'name': 'countryID', 
                    'node': []
                }
            ]
        }
    ]
}


def walk_thourgh_formatter(gql):
    '''
    '''
    try:

        #  Step 1: generate the base node
        new_object = [{ "table": gql["name"], "fields": gql["field"]}]

        # Step 2: generate the subnode of base node
        for  index in range(len(gql["node"])):
            next_nodes = walk_thourgh_formatter(gql["node"][index])
            new_object.append(next_nodes)
        
        # Step 3: return a base node
        return new_object
    except Exception as e:
        print(e)
        raise e
    
# working
def gql_formatter_to_sql(mapper, gql):
    '''
    '''
    return None
        


print(walk_thourgh_formatter(gql_formatter_2))
