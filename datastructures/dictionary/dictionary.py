# creating an dictionary

test_dict = {"a":1,"b":2}

print(test_dict) # output {'a': 1, 'b': 2}

# get the value from a dict
print(test_dict.get("a")) # output 1

# add a value to the dict
test_dict.popitem()
print(test_dict) # remove the last item output {'a': 1}

# add a value to the dict
test_dict = {"a":1,"b":2}
test_dict.pop("a")
print(test_dict) # remove the specific item output {'b': 2}

# loop through a dict
test_dict = {"a":1,"b":2}
for key in test_dict:
    print(test_dict.get(key))

# update a value to the dict
test_dict = {"a":1,"b":2}
test_dict["a"]=3
print(test_dict) # output {'a': 3, 'b': 2}

# get method
test_dict = {"a":1,"b":2}
print(test_dict.get("a")) # output 1

# items method
print(test_dict.items()) # output dict_items([('a', 1), ('b', 2)])

# keys method
print(test_dict.keys()) #output dict_keys(['a', 'b'])

# values method
print(test_dict.values()) #output dict_values([1, 2])

# len function
print(len(test_dict.values())) #output 2

