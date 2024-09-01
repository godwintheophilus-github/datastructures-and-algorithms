
# creating a set
myset = {"apple", "banana", "cherry"}

# true and 1 are considered same value, False and 0 are considered same value
thisset = {"apple", "banana", "cherry", True, 1, 2} # output {True, 2, 'apple', 'cherry', 'banana'}

thisset = {"apple", "banana", "cherry", False, True, 0} # output {False, True, 'apple', 'cherry', 'banana'}

# ordering of the set
set1 = {"abc", 34, True, 40, "male"} # output {True, 34, 40, 'abc', 'male'}

# set Constructor
thisset = set(("apple", "banana", "cherry")) # output {'apple', 'banana', 'cherry'}


# accessing set items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x) # output apple, banana, cherry

# check if an item is in the set
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) # output True

# adding an item to the set
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) # output {'apple', 'banana', 'cherry', 'orange'}

# add multiple items to the set
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset) # output {'apple', 'banana', 'cherry', 'orange', 'mango', 'grapes'}

# remove an item from the set
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) # output {'apple', 'cherry'}

# discard an item from the set
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) # output {'apple', 'cherry'}

# pop an item from the set
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) # output banana
print(thisset) # output {'apple', 'cherry'}

# clear the set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset) # output set()

# delete the set
thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset) # NameError: name 'thisset' is not defined

# union of two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) # output {'a', 'b', 'c', 1, 2, 3}
