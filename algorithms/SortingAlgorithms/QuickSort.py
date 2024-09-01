# Quick Sort
# Quick sort is a divide-and-conquer algorithm that selects a pivot element, partitions the input around the pivot, and recursively sorts the subarrays.

# How it Works
# If the input array has only one element, return it (since it is already sorted).
# Select a pivot element from the input array.
# Partition the input array around the pivot:
# Elements less than the pivot go to the left subarray.
# Elements greater than the pivot go to the right subarray.
# Elements equal to the pivot can go to either subarray.
# Recursively call the quick sort function on the left and right subarrays.
# Combine the sorted left subarray, the pivot element, and the sorted right subarray.
# Partitioning
# There are several ways to partition the input array around the pivot. Here's one common approach:

# Choose the pivot element (e.g., the middle element).
# Initialize two pointers, i and j, to the start and end of the input array.
# Iterate through the array, swapping elements as follows:
# If an element is less than the pivot, swap it with the element at index i and increment i.
# If an element is greater than the pivot, swap it with the element at index j and decrement j.
# When the iteration is complete, the pivot element is in its final position, and the input array is partitioned around it.
# Example
# Suppose we have the following list of numbers: [5, 2, 8, 3, 1, 6, 4]

# Step 1

# Select the pivot element (e.g., the middle element): 3
# Step 2

# Partition the input array around the pivot:
# Elements less than 3: [2, 1]
# Elements greater than 3: [5, 8, 6, 4]
# Elements equal to 3: [3]
# Step 3

# Recursively call the quick sort function on the left and right subarrays:
# Sort [2, 1]: [1, 2]
# Sort [5, 8, 6, 4]: [4, 5, 6, 8]
# Step 4

# Combine the sorted left subarray, the pivot element, and the sorted right subarray:
# [1, 2], 3, [4, 5, 6, 8]: [1, 2, 3, 4, 5, 6, 8]
# The list is now sorted.

# Code Implementation

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [5, 2, 8, 3, 1, 6, 4]
print(quick_sort(arr))  # [1, 2, 3, 4, 5, 6, 8]