# Merge Sort
# Merge sort is a divide-and-conquer algorithm that splits the input into two halves, recursively sorts each half, and then merges the two sorted halves.

# How it Works
# If the input array has only one element, return it (since it is already sorted).
# Split the input array into two halves, left and right.
# Recursively call the merge sort function on left and right.
# Merge the two sorted halves, left and right, into a single sorted array.
# Merging
# Create an empty array, result, to store the merged elements.
# Compare the smallest unmerged elements in left and right.
# Add the smaller element to result.
# Remove the smaller element from its respective array (left or right).
# Repeat steps 2-4 until one of the arrays is empty.
# Append the remaining elements from the non-empty array to result.
# Example
# Suppose we have the following list of numbers: [5, 2, 8, 3, 1, 6, 4]

# Step 1

# Split the input array into two halves: [5, 2, 8] and [3, 1, 6, 4]
# Step 2

# Recursively call the merge sort function on [5, 2, 8] and [3, 1, 6, 4]
# Split [5, 2, 8] into [5] and [2, 8]
# Split [3, 1, 6, 4] into [3, 1] and [6, 4]
# Step 3

# Recursively call the merge sort function on [5], [2, 8], [3, 1], and [6, 4]
# Since [5] has only one element, return it
# Merge [2, 8] into [2, 8]
# Merge [3, 1] into [1, 3]
# Merge [6, 4] into [4, 6]
# Step 4

# Merge [2, 8] and [5] into [2, 5, 8]
# Merge [1, 3] and [4, 6] into [1, 3, 4, 6]
# Step 5

# Merge [2, 5, 8] and [1, 3, 4, 6] into [1, 2, 3, 4, 5, 6, 8]
# The list is now sorted.

# Code Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

arr = [5, 2, 8, 3, 1, 6, 4]
print(merge_sort(arr))  # [1, 2, 3, 4, 5, 6, 8]
