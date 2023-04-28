import pandas as pd
from collections import defaultdict


QUERY_DATA_FILE = '../fake_parquet/generated-data_query.csv'
SQL= [
        'comercial_name', 
        'business_name', 
        'enterpris_key', 
        'city_id/name', 
        'city_id/timezone', 
        'city_id/country_id/currencyiso', 
        'city_id/country_id/region', 
        'city_id/country_id/name', 
        'city_id/country_id/prefixphone'
    ]

RPTA_SQL = {
    'comercial_name': 'Client/comercial_name', 
    'business_name': 'Client/business_name', 
    'enterpris_key': 'Client/enterpris_key', 
    'city_id': {
        'name': 'Client/city_id/name', 
        'timezone': 'Client/city_id/timezone', 
        'country_id': {
            'currencyiso': 'Client/city_id/country_id/currencyiso', 
            'region': 'Client/city_id/country_id/region', 
            'name': 'Client/city_id/country_id/name', 
            'prefixphone': 'Client/city_id/country_id/prefixphone'
        }
    }
}

# OK
def generate_node_fields(fields, parents):
    '''
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
    

# OK
def generate_graphq_response_structure(node, base_name):
    '''

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


# OK
def get_rpta_from_file(filename, basename):
    
    headers = pd.read_csv(filename, index_col=0, nrows=0).columns.tolist()
    headers = [ col[len(basename)+1:] for col in headers]

    rpta = generate_graphq_response_structure(headers, [basename])
    return rpta






## test
base_cap = "Client"

print(get_rpta_from_file(QUERY_DATA_FILE, base_cap))