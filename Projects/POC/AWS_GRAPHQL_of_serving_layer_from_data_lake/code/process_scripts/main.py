import json
import io
import os

import pandas as pd
from collections import defaultdict
from boto3 import Session
import boto3


s3_cli = boto3.client('s3')
athena_cli = boto3.client('athena')

ATHENA_S3_OUTPUT = "s3://pruebas-generales-para/"
ATHENA_S3_BUCKET_OUTPUT = "pruebas-generales-para"


### MACRO STEP #1 : convert graphql fields list to json graph (AKA formatter)

def generate_format_request( gql_request, format_obj, name_level ):
    '''
        Generate the level based in list of field
        
        Parmas:
        Level (int): current level of work.
        gql_request (list of string): list of field of graphql request.
        format_obj (object): node will store data associate this level.
        name_level (string): name of this node.
        
        return a node 
    '''
    try:
        rich_fields = [ (field, field.count('/')) for field in gql_request]
        
        # setting format obj
        format_obj["field"] = []
        format_obj["name"] = name_level
        format_obj["node"] = []
        
        # set up variables for process
        temp_gql_request = []
        node_fields = []

        # add only field of level
        for field in rich_fields:
            if field[1] == 0:
                #print(field)
                format_obj["field"].append(field[0].split("/")[0])
            else:
                temp_gql_request.append(field)
        
        # check what is the node field in this level
        for field in temp_gql_request:
            inner_field = field[0].split("/")[0]
                
            if inner_field in format_obj["field"] and inner_field not in node_fields:
                node_fields.append(inner_field)
                format_obj["field"].remove(inner_field)
                format_obj["node"].append([])

        # fill node of level with field need to formatting
        for field in temp_gql_request:
            inner_field = field[0].split("/")[0]
            index_node = node_fields.index(inner_field)
            format_obj["node"][index_node].append(field[0])
        
        # remove field not needed
        
        return format_obj
    except Exception as e:
        print(e)
        raise e  


def parsing_gql_request_to_obj(fields, name_level, format):
    '''
        Generate the format object to generate SQL query. Recursive focus working.
    
        Params
        field (list of string): list of fields in graphql request to process.
        name_level (string): name of base node.
        format (object): Node will store the data of graphql request.
    
        return format with data of graphql request to work
    '''
    try:

        #  Step 1: generate the base node
        new_object = generate_format_request(fields, format, name_level)

        # Step 2: generate the subnode of base node
        for  index in range(len(new_object["node"])):
            node_fields = new_object["node"][index]
            name_node = node_fields[0].split("/")[0]
            
            node_fields = [ field[len(name_node)+1:] for field in node_fields]
            
            new_node = parsing_gql_request_to_obj(
                node_fields,
                name_node,
                {}
            )
            
            new_object["node"][index] = new_node
        
        # Step 3: return a base node
        return new_object
    except Exception as e:
        print(e)
        raise e
    
### MACRO STEP #2 : convert formatter to  SQL query

def extract_data_from_formatter(node, level, mapper, used_table, parents_node, short_previous_table_name):
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
     
### MACRO STEP #3 : get data from AWS ATHENA

def get_data_from_sql_engine(query):
    '''
        Execute a SQL sentences in AWS AThena and return data.
        
        Params
        query (string): sql query to extract data
        
        return a location of generated file: key of file and bucket
    '''
    try:
        # setting params to control de Athena
        STATE = "RUNNING"

        ## STEP 1 : go the SQL sentence to athena
        
        query_id = athena_cli.start_query_execution(
            QueryString = query,
            QueryExecutionContext = {
                "Database": "db-poc-case-1"
            },
            ResultConfiguration= {"OutputLocation": ATHENA_S3_OUTPUT}
        )

        ## STEP 2 : waiting the finish operation: asynchronic ops

        while STATE in ["RUNNING", "QUEUED"]:
            #MAX_EXECUTION -= 1
            response = athena_cli.get_query_execution(
                    QueryExecutionId=query_id["QueryExecutionId"]
                )

            if "QueryExecution" in response and \
                "Status" in response["QueryExecution"] and \
                "State" in response["QueryExecution"]["Status"]:

                STATE = response["QueryExecution"]["Status"]["State"]

                if STATE == 'FAILED' or STATE == 'CANCELLED':
                    print(STATE)
                    raise Exception("error: not allow to get data; maybe it was failed or cancelled.")
                if STATE == "SUCCEEDED":
                    break

        ## STEP 3 : get data of query
        file_query_solved = query_id["QueryExecutionId"] + ".csv"
        
        return  ATHENA_S3_BUCKET_OUTPUT, file_query_solved
    except Exception as e:
        print("error")
        print(e)
        raise e


### MACRO STEP #4 : convert csv file to json

## STEP 4.1 : generate structure of response from formatter

def generate_node_fields(fields, parents):
    '''
        Generate the node estructure for the mapper of graphql and SQL data.
        This is a recursive method.
        
        Args
        fields (List of string): list of field to process.
        parents (list of string): list of previous nodes contain it.
        
        Return the ready node to work.
    '''
    try:
        rich_fields = [ (field, field.count('/')) for field in fields]
        format_obj = {}
        group_fields = defaultdict(lambda: -1)
        
        # add associated field to group of fields
        for field in rich_fields:
            if field[1] == 0:
                format_obj[field[0]] = "/".join(parents + [field[0]])
            else:
                inner_field = field[0].split("/")

                if group_fields[inner_field[0]] == -1:
                    group_fields[inner_field[0]] = ["/".join(inner_field[1:])]
                else:
                    group_fields[inner_field[0]].append("/".join(inner_field[1:]))
    
        for key, value  in group_fields.items():
            format_obj[key] = value

        return format_obj
    except Exception as e:
        print(str(e))
        raise(e)
    

def generate_graphq_response_structure(node, base_name):
    '''
        Generate the structure of graphql response.
        This is a recursive method.
        
        Args:
        node (list of string): list of field to generate the node.
        base_name (list of string): list of previous container node.
        
        return a structure to work like mapper graphql-SQL data
    '''
    try:
        #  Step 1: generate fields and table name for SQL query
        node = generate_node_fields(node, base_name)

        # Step 2: specify table name of this node for SQL query
        for key, value  in node.items():
            if type(value) is list:
                node[key] = generate_graphq_response_structure(
                        value,
                        base_name + [key]
                    )

        # Step 3: return a base node
        return node
    except Exception as e:
        print(e)
        raise e


def get_rpta_from_file(bucket, key, basename):
    '''
        Generate estructure of graphql response base in header of data file 
        from aws athena
        
        Args:
        bucket (String): name of bucket contain the data file.
        key (String): name of object contain the data file
        basename (string): name of first node in query method of data schema.
        
        return a structure of mapper to SQL data to graphql request
    '''
    s3_object = s3_cli.get_object(
        Bucket=bucket,
        Key=key
    )
    headers = pd.read_csv(
            io.BytesIO(s3_object['Body'].read()), 
            encoding='utf8',
            nrows=0
    ).columns.tolist()
    
    clean_headers = [ col[len(basename)+1:] for col in headers]

    rpta = generate_graphq_response_structure(clean_headers, [basename])
    return rpta, headers


## STEP 4.2 : generate data of response in graphql request

def generate_node_response(structure, row):
    '''
        Map the field of graphql response to column in row of data file; but
        in node level. This is a recursive method.
        
        Args
        structure (object): mapper of graphl request and SQL data.
        row (row of dataframe): row of data file.
        
        return a partial graphql data item related with SQL data
    '''
    try:
        node = {}
        
        # add associated field to group of fields
        for key, value in structure.items():
            if type(value) is not dict:
                node[key] = row[value]
            else:
                node[key] = value

        return node
    except Exception as e:
        print(str(e))
        raise(e)


def generate_graphql_response(structure, row):
    '''
        Generate the structure of graphql response for row of data file
        This is a recursive method..
        
        Args:
        structure (object): mapper of graphl request and SQL data.
        row (row of dataframe): row of data file.
        
        return a completed graphql data item related with SQL data
    '''
    try:
        #  Step 1: generate fields and table name for SQL query
        node = generate_node_response(structure, row)

        # Step 2: specify table name of this node for SQL query
        for key, value  in node.items():
            if type(value) is dict:
                node[key] = generate_graphql_response(
                        value,
                        row
                    )

        # Step 3: return a base node
        return node
    except Exception as e:
        print(e)
        raise e


def generate_rpta_graphql(bucket, key, basename):
    '''
        Generate the graphql response from data file.
        
        Args:
        bucket (String): name of bucket contain the data file.
        key (String): name of object contain the data file
        basename (string): name of first node in query method of data schema.
        
        return graphql data items
    '''
    structure, headers = get_rpta_from_file(bucket, key, basename)
    
    s3_object = s3_cli.get_object(
        Bucket=bucket,
        Key=key
    )
    data_body = pd.read_csv(
            io.BytesIO(s3_object['Body'].read()), 
            encoding='utf8',
    )
    rpta = []

    for _, row in data_body.iterrows():
        rpta_node = generate_graphql_response(structure, row.to_dict())
        rpta.append(rpta_node)
    
    if len(rpta) == 0: rpta = [{}]
    
    return rpta


### MAIN PROCESS: 

def get_sql_query_from_graphql(gql_fields, name, mapper_relationships):
    '''
        Response the graphql request with data file from Athena.
        
        Args
        gql_fields (list of string): list of required fields from graphql request.
        name (string): name of main container node in data schema.
        mapper_relationships (object) mapper of table relationships.
        
        return a required graphql data items
    '''
    # step 1: get formatter from graphql request
    formatter_gql = parsing_gql_request_to_obj(gql_fields, name, {})
    
    # step 2: get SQL query from formatter
    query = gql_formatter_to_sql(mapper_relationships, formatter_gql)

    # step 3: generate the data of graphql request in aws athena    
    bucket_data, key_data = get_data_from_sql_engine(query)
    
    # step 4: generate response structure mapper from formatter
    rpta = generate_rpta_graphql( bucket_data, key_data, name)
    print(rpta)
    return rpta



def lambda_handler(event, context):
    print(event)
    print(event['info']["selectionSetList"])
    NAME_CLIENT = "Client"
    MAPPER_RELATIONSHIPS = {
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
    return get_sql_query_from_graphql(
            event['info']["selectionSetList"],
            NAME_CLIENT,
            MAPPER_RELATIONSHIPS
        )
