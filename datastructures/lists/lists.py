#creating a list
test_list = [1,2,3,4,5,6,"a"]
print(test_list) #output [1, 2, 3, 4, 5, 6, 'a']

# accessing the list
print(test_list[1]) # output 2

# nexted list 
test_list = [test_list,1,2,3,4,5]
print(test_list) # output [[1, 2, 3, 4, 5, 6, 'a'], 1, 2, 3, 4, 5]

# remove the last element
test_list.pop()

print(test_list) # output [[1, 2, 3, 4, 5, 6, 'a'], 1, 2, 3, 4]

# update a value of list

test_list[0] = 'G' 
print(test_list) # output ['G', 1, 2, 3, 4]

# add a value to the index
test_list.insert(2,[11,12,13])
print(test_list) # ['G', 1, [11, 12, 13], 2, 3, 4]

# find a element's index in a list
print(test_list.index(2)) # output 3

# count of numbers in a list 
print(test_list.count(2)) # output 1

# slice of a list
print(test_list[3:]) # output [2, 3, 4]
print(test_list[-2:]) # output [3, 4]

# String

test_string = "Godwin"
test_list = list(test_string)
print(test_list) # output ['G', 'o', 'd', 'w', 'i', 'n']