import array as arr 

# creating an array

test_array = arr.array('i',[1,2,3,4,5,7,8,9])

print(test_array) # output array('i', [1, 2, 3, 4, 5, 7, 8, 9])

# checking the buffer information

print(test_array.buffer_info()) # output (4344951056, 8)

# inserting into an array

test_array.insert(2,22)

print(test_array) # output array('i', [1, 2, 22, 3, 4, 5, 7, 8, 9])

# appending to an array

test_array.append(55)

print(test_array) # output array('i', [1, 2, 22, 3, 4, 5, 7, 8, 9, 55])

#index of a value in a array

print(test_array.index(55)) # output 9

#accessing values of an array
print(test_array[1]) # output 2

# deleteing an element from an array

test_array.remove(1) # note here 1 is the value and not the index
print(test_array) # output array('i', [2, 22, 3, 4, 5, 7, 8, 9, 55])

# reversing an array

test_array.reverse()

print(test_array) # output array('i', [55, 9, 8, 7, 5, 4, 3, 22, 2])

#remove the last element of an array

test_array.pop()
print(test_array) # output array('i', [55, 9, 8, 7, 5, 4, 3, 22])

# Array to bytes/ String

print(test_array.tobytes()) # output b'7\x00\x00\x00\t\x00\x00\x00\x08\x00\x00\x00\x07\x00\x00\x00\x05\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00\x16\x00\x00\x00'

# Count of array
 
print(test_array.count(55)) # output 1, note that 55 is a element in the array
