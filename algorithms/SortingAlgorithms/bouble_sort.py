# Bubble Sort
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

# How it Works
# Start at the beginning of the list.
# Compare the first two elements. If they are in the wrong order, swap them.
# Move to the next two elements and repeat the comparison and swap if necessary.
# Continue this process until the end of the list is reached.
# Repeat the process until no more swaps are needed, indicating that the list is sorted.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5, 2, 8, 3, 1, 6, 4]
print(bubble_sort(arr))  # [1, 2, 3, 4, 5, 6, 8]