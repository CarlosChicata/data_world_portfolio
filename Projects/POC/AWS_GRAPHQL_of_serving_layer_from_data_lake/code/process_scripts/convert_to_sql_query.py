from collections import defaultdict

mapper = {
   "Client": {
       "table": "client_table",
       "short_table": "cli",
       "database": "db-poc-case-1",
       "join": {
           "cityID": ["id", "city_id"], 
           # primero es del tabla externa, el siguiente de la tabla base
       }
   },
   "cityID": {
       "table": "city_table",
       "short_table": "ci",
       "database": "db-poc-case-1",
       "join": {
           "countryID": ["id", "country_id"]
       }
   },
   "countryID":  {
       "table": "country_table",
       "short_table": "co",
       "database": "db-poc-case-1",
       "join": {}
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
        Travel all formatter of graphql request to get all field and table.
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


def generate_table_name(table_name, mapper, used_table):
    '''
        Generate the unique name of table will use in SQL query.
        
        Params:
        table_name (string): name of table from graphql request.
        mapper (object/dict): mapper to Graphql to SQL resource.
        used_table (defaultdict): state of concurrence of table.
        
        return a name of table in SQL, en short name references this table.
    '''
    
    if mapper.get(table_name) is None:
        raise Exception("No hay tabla")
    
    rpta = None
    short_rpta = None

    # Step 1: naming the table with unique name in sql
    if used_table[table_name] == -1:
        rpta = '''%s as %s''' % (
                mapper[table_name]["table"],
                mapper[table_name]["short_table"]
            )
        short_rpta = mapper[table_name]["short_table"]
        used_table[table_name] += 1
        
    else:
        ite = used_table[table_name]
        rpta = '''%s as %s''' % (
                mapper[table_name]["table"],
                mapper[table_name]["short_table"] + "_" + str( ite + 1)
            )
        short_rpta = mapper[table_name]["short_table"] + "_" + str( ite + 1)
        used_table[table_name] += 1

    return rpta, short_rpta


def generate_field_of_table_name(table_name, fields, parents):
    '''
        Generate the unique name for all field in table will use in SQL query.
        
        Params:
        table_name (string): name of table from graphql request.
        fields (list of string): list of field of table.
        parents (list of string): list of name of previous node go through to 
            get the field.
        
        return a name of field of table in SQL   
    '''
    base_field = "/".join(parents)
    
    rpta = []
    
    for field in fields:
        value_field = '''%s as %s''' % (
            ".".join([table_name, field]),
            "/".join([base_field, field])
        )
        rpta.append(value_field)
    
    return rpta
    

# working
def gql_formatter_to_sql(mapper, gql):
    '''
    '''
    list_params_sql_query = walk_thourgh_formatter(gql)
        
    if len(list_params_sql_query) <= 0:
        return "",
    elif len(list_params_sql_query) >= 1:
        used_table = defaultdict(lambda: -1)
        
        
        
    return None
        

# test 

used_table = defaultdict(lambda: -1)
#print(walk_thourgh_formatter(gql_formatter_2))
print(generate_table_name(
    'Client',
    mapper, used_table))
print(used_table)
print(generate_table_name(
    'Client', 
    mapper, used_table))
print(used_table)
print(generate_table_name(
    'Client', 
    mapper, used_table))
print(used_table)
print(generate_field_of_table_name("cli", ["name", "currencyISO"], ["Client", "CountryID"]))