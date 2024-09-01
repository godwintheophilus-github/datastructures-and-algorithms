# Binary Search

# Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

# How it works:

# Start with a sorted list: Binary search requires the list to be sorted in ascending or descending order.
# Find the middle element: Calculate the middle index of the list.
# Compare the middle element to the target: If the middle element is equal to the target, return the index.
# Eliminate half of the list: If the middle element is less than the target, repeat the process with the right half of the list. If the middle element is greater than the target, repeat the process with the left half of the list.
# Repeat steps 2-4: Continue dividing the list in half until the target is found or the list is empty.
# Example:

# Suppose we have a sorted list of numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# We want to find the number 5.

# Start with the entire list.
# Find the middle element: 5 (index 4).
# Compare 5 to the target: 5 is equal to the target, so return index 4.
# Time complexity:

# Binary search has a time complexity of O(log n), making it much faster than linear search (O(n)) for large lists.

# Space complexity:

# Binary search has a space complexity of O(1), as it only requires a few variables to store the indices and the target value.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"Low: {low}, High: {high}, Mid: {mid}")

        if arr[mid] == target:
            print(f"Target {target} found at index {mid}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Target {target} not found in the list")
    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

binary_search(arr, target)

# output
# Low: 0, High: 8, Mid: 4
# Target 5 found at index 4