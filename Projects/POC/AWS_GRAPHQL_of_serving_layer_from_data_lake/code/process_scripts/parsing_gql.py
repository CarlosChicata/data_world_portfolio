def generate_format_request(level, gql_request, format_obj, name_level ):
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
            if field[1] == level:
                #print(field)
                format_obj["field"].append(field[0])
            else:
                temp_gql_request.append(field)
        
        #print(format_obj)
        #print(temp_gql_request)
        #print("--------------")
        
        # check what is the node field in this level
        for field in temp_gql_request:
            inner_field = field[0].split("/")[0]
                
            if inner_field in format_obj["field"] and inner_field not in node_fields:
                node_fields.append(inner_field)
                format_obj["field"].remove(inner_field)
                format_obj["node"].append([])

        #print(format_obj)
        #print(node_fields)
        #print(temp_gql_request)
        #print("--------------")

        # fill node of level with field need to formatting
        for field in temp_gql_request:
            inner_field = field[0].split("/")[0]
            index_node = node_fields.index(inner_field)
            format_obj["node"][index_node].append(field[0])
        
        # remove field not needed
        
        
        print(format_obj)
        
        return format_obj
    except Exception as e:
        print(e)
        raise e  


# working
def parsing_gql_request_to_obj(fields):
    try:
        # Step 1: get the level of deep by fields
        rich_fields = [ (field, field.count('/')) for field in fields]
        max_level = max([ field[1] for field in rich_fields])

        format_request = {}
        #  Step 2: setup to recorring element
        generate_format_request(0, fields, {}, 'Client')
        #while len(rich_fields) > 0:
        #    True
        
        return format_request
    except Exception as e:
        print(e)
        raise e
    
    
    
#### test

GQL = [
      'address', # -> 1
      'cityID', # -> 1*
      'cityID/id', # -> 2 
      'cityID/countryID', # -> 2*
      'cityID/countryID/currencyISO', # -> 3
      'cityID/countryID/id', # -> 3
      'cityID/countryID/name', # ->  3
      'cityID/name', # -> 2
      'commercialName', # -> 1 
      'enterprise_key' # ->  1
    ]

GQL2 = [
    'cityID/id',
    'cityID/countryID', 
    'cityID/countryID/currencyISO', 
    'cityID/countryID/id', 
    'cityID/countryID/name', 
    'cityID/name'
]

#generate_format_request(0, GQL, {}, "Client")
parsing_gql_request_to_obj(GQL)