import numpy as np 

# create a two dimentional array
test_array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(test_array) 
# output
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# inserting an array
test_array = np.insert(test_array,0,axis=0,values=[12,13,14,15]) # axis 0 is row and 1 means columns. 0 here is index
print(test_array)

#output
# [[12 13 14 15]
#  [ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

test_array = np.insert(test_array,0,axis=1,values=[12,13,14,15])
print(test_array)
# output
# [[12 12 13 14 15]
#  [13  1  2  3  4]
#  [14  5  6  7  8]
#  [15  9 10 11 12]]

# remove a column or a row for an array

test_array = np.delete(test_array,0,axis=1)
print(test_array)

# output
# [[12 13 14 15]
#  [ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

#appending values to existing array
test_array = np.append(test_array,[[77,88,99,22]],axis=0)
print(test_array)

# output
# [[12 13 14 15]
#  [ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [77 88 99 22]]

# accessing an element
print(test_array[1][1]) #output 2
