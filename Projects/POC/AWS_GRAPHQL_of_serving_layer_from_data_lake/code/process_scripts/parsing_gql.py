def generate_format_request(level, gql_request, format_obj, name_level ):
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
        print(level, gql_request, format_obj, name_level)
        print("\n")
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
                format_obj["field"].append(field[0].split("/")[0])
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
        print("----------------------")
        
        return format_obj
    except Exception as e:
        print(e)
        raise e  


# working
def parsing_gql_request_to_obj(fields, level, name_level, format):
    try:


        #  Step 2: setup to recorring element
        new_object = generate_format_request(level, fields, format, name_level)

        for  index in range(len(new_object["node"])):
            node_fields = new_object["node"][index]
            name_node = node_fields[0].split("/")[0]
            
            node_fields = [ field[len(name_node)+1:] for field in node_fields]
            
            new_node = parsing_gql_request_to_obj(
                node_fields,
                0,
                name_node,
                {}
            )
            
            new_object["node"][index] = new_node
        
        return new_object
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
rpta = parsing_gql_request_to_obj(GQL, 0, 'Client', {})
print("rpta")
print(rpta)