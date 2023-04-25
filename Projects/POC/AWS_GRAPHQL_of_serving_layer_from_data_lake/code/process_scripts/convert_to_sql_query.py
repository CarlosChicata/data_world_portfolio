from collections import defaultdict

mapper = {
   "Client": {
       "table": "client_table",
       "short_table": "cli",
       "database": "db-poc-case-1",
       "join": {
           # primero es del tabla externa, el siguiente de la tabla actual
        }
   },
   "cityID": {
       "table": "city_table",
       "short_table": "ci",
       "database": "db-poc-case-1",
       "join": {
           "Client": {"container_table": "city_id", "current_table": "id" }
       }
   },
   "countryID":  {
       "table": "country_table",
       "short_table": "co",
       "database": "db-poc-case-1",
       "join": {
           "cityID": {"container_table": "country_id", "current_table": "id" }
       }
   }
}

mapper_2 = {
   "Client": {
       "table": "client_table",
       "short_table": "cli",
       "database": "db-poc-case-1",
       "join": {
           # primero es del tabla externa, el siguiente de la tabla actual
        }
   },
   "city_id": {
       "table": "city_table",
       "short_table": "ci",
       "database": "db-poc-case-1",
       "join": {
           "Client": {"container_table": "city_id", "current_table": "id" }
       }
   },
   "country_id":  {
       "table": "country_table",
       "short_table": "co",
       "database": "db-poc-case-1",
       "join": {
           "city_id": {"container_table": "country_id", "current_table": "id" }
       }
   }
}


gql_formatter_2 = {
    'field': ['address', 'comercial_name', 'business_name', 'enterpris_key'], 
    'name': 'Client', 
    'node': [
            {
                'field': ['name', 'timezone'], 
                'name': 'city_id', 
                'node': [
                        {
                            'field': ['currencyiso', 'region', 'name', 'prefixphone'], 
                            'name': 'country_id', 
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

# prototype
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

# OK
def extract_data_from_formatter(node, level, mapper, used_table, parents_node, \
        short_previous_table_name):
    '''
        Extract data from GraphQL requesto to structure the SQL Query.
        
        Args
        Node(object): node of table to process.
        level(int): current level in formatter object of GraphQL request.
        Mapper(object): Auxilitary object to map the conection of node from 
            data sources view.
        used_table (object): utility object to store used table name in 
            formatter object.
        parents_node(list of string): name of previos parents node of 
            current node.
        short_previous_table_name (string): short name of father node of
            current node.
            
        Return a fields and name of node to use.
    '''
    try:

        #  Step 1: generate fields and table name for SQL query
        table_name, short_table_name = generate_table_name(
                node["name"], 
                mapper, 
                used_table
            )
        fields_table = generate_field_of_table_name(
                short_table_name, 
                node["field"],
                parents_node + [node["name"]]
            )

        # Step 2: specify table name of this node for SQL query
        if level == 0:
            table_name = '''FROM %s''' % (table_name)
        else:
            joining_tables = mapper[node["name"]]["join"][parents_node[-1]]
            
            table_name = '''JOIN %s on  %s = %s''' % (
                table_name,
                ".".join([
                            '''"%s"''' % (short_previous_table_name,), 
                            '''"%s"''' % (joining_tables["container_table"],)
                        ]),
                ".".join([
                            '''"%s"''' % (short_table_name,), 
                            '''"%s"''' %  (joining_tables["current_table"],)
                        ])
            )

        table_name = [table_name]

        # Step 3: generate the fields and tables name of  the subnode of base node
        for  index in range(len(node["node"])):
            deep_fields, deep_table = extract_data_from_formatter(
                node["node"][index],
                level + 1,
                mapper,
                used_table,
                parents_node + [node["name"]],
                short_table_name
            )
            
            fields_table = fields_table + deep_fields
            table_name = table_name + deep_table

        # Step 3: return a base node
        return fields_table, table_name
    except Exception as e:
        print(e)
        raise e


# OK
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
        rpta = ''' "%s" as "%s"''' % (
                mapper[table_name]["table"],
                mapper[table_name]["short_table"]
            )
        short_rpta = mapper[table_name]["short_table"]
        used_table[table_name] += 1
        
    else:
        ite = used_table[table_name]
        rpta = '''"%s" as "%s"''' % (
                mapper[table_name]["table"],
                mapper[table_name]["short_table"] + "_" + str( ite + 1)
            )
        short_rpta = mapper[table_name]["short_table"] + "_" + str( ite + 1)
        used_table[table_name] += 1

    return rpta, short_rpta


# OK
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
        value_field = '''%s as "%s"''' % (
            ".".join(['''"%s"''' % (table_name,), '''"%s"''' % (field,)]),
            "/".join([base_field, field])
        )
        rpta.append(value_field)
    
    return rpta
    

# ok
def gql_formatter_to_sql(mapper, gql):
    '''
        Generate a SQL query from fomatter object of GraphQL request.
        
        Args:
        mapper(object): utility object to map conection of table from tables.
        gql (object): fomatter  object of GraphQL request.
        
        return a SQL query to execute
    '''
    try:
        used_table = defaultdict(lambda: -1)

        fields, tables = extract_data_from_formatter(
            gql,
            0,
            mapper,
            used_table,
            [],
            None
        )
        select = "SELECT " + ",\n".join(fields)
        tables = "\n".join(tables)
        return select + "\n" + tables
    except Exception as e:
        print(str(e))
        raise e
        
        
        
    return None
        

# test
print(gql_formatter_to_sql(mapper_2, gql_formatter_2))


'''
used_table = defaultdict(lambda: -1)

rpta = extract_data_from_formatter(
    gql_formatter_1,
    0,
    mapper,
    used_table,
    [],
    None
)
print(rpta)


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
'''