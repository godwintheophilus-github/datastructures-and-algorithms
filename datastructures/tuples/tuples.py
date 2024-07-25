# create a tuple in python

test_tupple = (1,2,3,4,5,6,11,11,11,'11')
print(test_tupple) # output (1, 2, 3, 4, 5, 6, 11, 11, 11, 11)

# identify the index of the tuple
print(test_tupple.index(11)) # output 6

# identify the count of element in the tuple
print(test_tupple.count(11)) # output 4

# retrive data based on index
print(test_tupple[4]) # output 5

# slicing the tupple

print(test_tupple[4:]) # output (5, 6, 11, 11, 11, '11')