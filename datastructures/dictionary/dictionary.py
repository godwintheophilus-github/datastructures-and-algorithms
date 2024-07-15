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