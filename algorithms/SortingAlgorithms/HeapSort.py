# Heap Sort
# Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. It is similar to selection sort, but instead of searching for the maximum or minimum element in the unsorted portion of the array, heap sort uses a heap to find the maximum or minimum element.

# How it Works
# Build a max heap from the unsorted array.
# Swap the root node (maximum element) with the last node in the heap.
# Reduce the size of the heap by one and heapify the root node.
# Repeat steps 2-3 until the heap is empty.
# Building a Max Heap
# A max heap is a complete binary tree where each parent node is greater than or equal to its children. To build a max heap, we start at the last non-leaf node and work our way up to the root node, heapifying each node as we go.

# Heapify
# Heapify is the process of rearranging the nodes of a heap to maintain the heap property. To heapify a node, we compare it with its children and swap it with the larger child if necessary.

# Example
# Suppose we have the following list of numbers: [5, 2, 8, 3, 1, 6, 4]

# Step 1

# Build a max heap from the unsorted array:
# Code
# CopyInsert
#      8
#    /   \
#   5     6
#  / \   / \
# 2   3 1   4
# Step 2

# Swap the root node (maximum element) with the last node in the heap:
# Code
# CopyInsert
#      4
#    /   \
#   5     6
#  / \   / \
# 2   3 1   8
# Step 3

# Reduce the size of the heap by one and heapify the root node:
# Code
# CopyInsert
#      6
#    /   \
#   5     4
#  / \   / \
# 2   3 1
# Step 4

# Repeat steps 2-3 until the heap is empty:
# Code
# CopyInsert
#      5
#    /   \
#   4     3
#  / \   / \
# 2   1
# The list is now sorted.

# Code Implementation

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr = [5, 2, 8, 3, 1, 6, 4]
heap_sort(arr)
print(arr)  # [1, 2, 3, 4, 5, 6, 8]