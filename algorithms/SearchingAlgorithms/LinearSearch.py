# Linear Search
# Linear search is a simple searching algorithm that works by iterating through each element in a list or array until it finds a match for the target value.

# How it Works
# Start at the beginning of the list or array.
# Compare the target value with the current element.
# If the target value matches the current element, return the index of the current element.
# If the target value does not match the current element, move to the next element in the list or array.
# Repeat steps 2-4 until the end of the list or array is reached.
# If the target value is not found, return a special value (e.g. -1) to indicate that the value is not in the list or array.
# Example
# Suppose we have the following list of numbers: [3, 6, 1, 8, 2, 4]

# Target value: 8
# Start at the beginning of the list: 3
# Compare 8 with 3: no match
# Move to the next element: 6
# Compare 8 with 6: no match
# Move to the next element: 1
# Compare 8 with 1: no match
# Move to the next element: 8
# Compare 8 with 8: match!
# Return the index of the current element: 3
# Code Implementation

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [3, 6, 1, 8, 2, 4]
target = 8
print(linear_search(arr, target))  # 3