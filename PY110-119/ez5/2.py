# given dictionary and list of keys
# return new dict that only contains the key/value pairs for the specified keys

def keep_keys(dic, keys):
    return {key: dic[key] for key in dic if key in keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True