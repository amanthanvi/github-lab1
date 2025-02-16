import json

def search_json(json_data, search_string):
    results = []
    search_string = search_string.lower() # Convert search string to lowercase

    # 1. Loop through each user's data
    for user in json_data:
        # Loop through each key-value pair in the user's data
        for key, value in user.items():
            # Some items are numbers, so we need to convert them to strings and remove spaces
            str_value = str(value).lower().replace(" ", "")
            str_value_with_spaces = str(value).lower() # Also try with spaces for natural matching
            
            # 2. Check if the search string appears in any field values - case insensitive
            if search_string in str_value or search_string or search_string in str_value_with_spaces:
                # 3. If there's a match, add that user's data to the results
                results.append(user)
                # Break to avoid adding the same user multiple times
                break
    return results