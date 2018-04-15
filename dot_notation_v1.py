# Just for pretty prints
import json

# Update dict in smart way
def upsert_dict(item_value, item_result):
    if isinstance(item_value, dict):
        for subkey, subvalue in item_value.items():
            if subkey in item_result:
                item_result[subkey] = upsert_dict(subvalue, item_result[subkey])
            else:
                item_result[subkey] = subvalue
    return item_result

# Update list in smart way
def upsert_list(list_value, list_result):
    result = []
    for item_value, item_result  in zip(list_value, list_result):
        result.append(upsert_dict(item_value, item_result))
    return result

# Cheapass validation for avoiding index references in queries
def validate(query):
    if isdigit(query) == True:
        return True
    else:
        return False

# Recursive return of nested levels
def go_one_level_down(data, sublevels):
    if len(sublevels) > 0:
        if isinstance(data, list):
            result = []
            for element in data:
                result.append(go_one_level_down(element, sublevels))
            return result

        elif isinstance(data, dict):
            if sublevels[0] in data:
                if len(sublevels) == 1:
                    return {sublevels[0]: data[sublevels[0]]}
                else:
                    return {sublevels[0]: go_one_level_down(data[sublevels[0]], sublevels[1:])}
            else:
                return {}
        else:
            return {}
    else:
        return data

# Dot notation "filters"
queries = [
    "children.friends",
    "name",
    "children.name",
    #"children"
]

# Cleaning from duplicates + sorting for clarity
if len(queries) > 1:
    queries = list(set(queries))
    queries.sort()

# Sample input data
test_json = {
    "name": "Alex",
    "children": [
        {
            "name":"Adam",
            "friends": [
                "Lisa"
            ]
        },
        {
            "name":"Selena",
            "friends": []
        }
    ]
}

# Building result based off queries
result = {}
if len(queries) > 0:
    for query in queries:
        levels = query.split(".")
        if len(levels) > 0:
            get_result = go_one_level_down(test_json, levels)
            if len(get_result) > 0:
                for key, value in get_result.items():
                    if key in result:
                        if isinstance(value, list):
                            result[key] = upsert_list(value, result[key])
                        else:
                            result[key] = upsert_dict(value, result[key])
                    else:
                        result[key] = value
        elif query > 0:
            if validate(query):
                result.update(test_json[query])
            else:
                print("Invalid query")
        else:
            print("Invalid query")
else:
    result = test_json

# Print result
print(json.dumps(result, indent=4))
