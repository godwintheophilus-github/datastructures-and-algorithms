# Insertion Sort
# Insertion sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.

# How it Works
# Start with the first element as the sorted region.
# Take the next element from the unsorted region.
# Compare the new element with the elements in the sorted region.
# Shift the elements in the sorted region to the right until the correct position for the new element is found.
# Insert the new element into the correct position.
# Repeat steps 2-5 until the entire list is sorted.
# Example
# Suppose we have the following list of numbers: [5, 2, 8, 3, 1, 6, 4]

# Pass 1

# Start with the first element 5 as the sorted region.
# Take the next element 2 from the unsorted region.
# Compare 2 with 5 and shift 5 to the right.
# Insert 2 into the correct position: [2, 5]
# Pass 2

# Take the next element 8 from the unsorted region.
# Compare 8 with 5 and 2, and insert it into the correct position: [2, 5, 8]
# Pass 3

# Take the next element 3 from the unsorted region.
# Compare 3 with 5 and 2, and shift 5 and 8 to the right.
# Insert 3 into the correct position: [2, 3, 5, 8]
# Pass 4

# Take the next element 1 from the unsorted region.
# Compare 1 with 2, 3, 5, and 8, and shift all elements to the right.
# Insert 1 into the correct position: [1, 2, 3, 5, 8]
# Pass 5

# Take the next element 6 from the unsorted region.
# Compare 6 with 5 and 8, and insert it into the correct position: [1, 2, 3, 5, 6, 8]
# Pass 6

# Take the next element 4 from the unsorted region.
# Compare 4 with 5 and 3, and shift 5 and 6 and 8 to the right.
# Insert 4 into the correct position: [1, 2, 3, 4, 5, 6, 8]
# The list is now sorted.

# Code Implementation

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [5, 2, 8, 3, 1, 6, 4]
print(insertion_sort(arr))  # [1, 2, 3, 4, 5, 6, 8]