


def parsing_gql_request_to_obj(fields):
    try:
        # Step 1: get the level of deep by fields
        rich_fields = [ (field, field.count('/')) for field in fields]
        max_level = max([ field[1] for field in rich_fields])

        format_request = {}
        #  Step 2: setup to recorring element
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

parsing_gql_request_to_obj(GQL)