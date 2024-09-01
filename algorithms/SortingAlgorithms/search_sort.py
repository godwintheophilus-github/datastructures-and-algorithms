# Selection Sort
# Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first unsorted element.

# How it Works
# Start at the beginning of the list.
# Find the minimum element in the unsorted part of the list.
# Swap the minimum element with the first unsorted element.
# Move to the next element in the list and repeat steps 2-3 until the end of the list is reached.


# Example
# Suppose we have the following list of numbers: [5, 2, 8, 3, 1, 6, 4]

# Pass 1

# Find the minimum element in the list: 1
# Swap 1 with the first element 5: [1, 2, 8, 3, 5, 6, 4]
# Pass 2

# Find the minimum element in the unsorted part of the list: 2
# Swap 2 with the second element 2: [1, 2, 8, 3, 5, 6, 4] (no change)
# Pass 3

# Find the minimum element in the unsorted part of the list: 3
# Swap 3 with the third element 8: [1, 2, 3, 8, 5, 6, 4]
# Pass 4

# Find the minimum element in the unsorted part of the list: 4
# Swap 4 with the fourth element 8: [1, 2, 3, 4, 5, 6, 8]
# Pass 5

# Find the minimum element in the unsorted part of the list: 5
# Swap 5 with the fifth element 5: [1, 2, 3, 4, 5, 6, 8] (no change)
# Pass 6

# Find the minimum element in the unsorted part of the list: 6
# Swap 6 with the sixth element 6: [1, 2, 3, 4, 5, 6, 8] (no change)


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [5, 2, 8, 3, 1, 6, 4]
print(selection_sort(arr))  # [1, 2, 3, 4, 5, 6, 8]