# Radix Sort
# Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits (or by radix) which share the same significant position and value.

# How it Works
# Find the maximum number to know the number of digits.
# Initialize 10 buckets (0-9) for each digit.
# Iterate through each digit position (from least significant to most significant).
# For each digit position, distribute the numbers into the corresponding buckets.
# Collect the numbers from the buckets and update the original array.
# Repeat steps 3-5 until all digit positions have been processed.
# Example
# Suppose we have the following list of numbers: [170, 45, 75, 90, 802, 24, 2, 66]

# Step 1

# Find the maximum number to know the number of digits: 802 has 3 digits.
# Step 2

# Initialize 10 buckets (0-9) for each digit.
# Step 3

# Iterate through each digit position (from least significant to most significant).
# Step 4

# For each digit position, distribute the numbers into the corresponding buckets.
# Digit Position 1 (Least Significant)

# 170 -> Bucket 0
# 45 -> Bucket 5
# 75 -> Bucket 5
# 90 -> Bucket 0
# 802 -> Bucket 2
# 24 -> Bucket 4
# 2 -> Bucket 2
# 66 -> Bucket 6
# Step 5

# Collect the numbers from the buckets and update the original array: [170, 90, 802, 2, 24, 45, 75, 66]
# Step 6

# Repeat steps 3-5 until all digit positions have been processed.
# Digit Position 2

# 170 -> Bucket 7
# 90 -> Bucket 9
# 802 -> Bucket 0
# 2 -> Bucket 0
# 24 -> Bucket 2
# 45 -> Bucket 4
# 75 -> Bucket 7
# 66 -> Bucket 6
# Digit Position 3 (Most Significant)

# 170 -> Bucket 1
# 90 -> Bucket 0
# 802 -> Bucket 8
# 2 -> Bucket 0
# 24 -> Bucket 0
# 45 -> Bucket 0
# 75 -> Bucket 0
# 66 -> Bucket 0
# Final Sorted Array

# [2, 24, 45, 66, 75, 90, 170, 802]
# Code Implementation

def radix_sort(arr):
    RADIX = 10
    placement = 1

    max_digit = max(arr)
    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        placement *= RADIX
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))  # [2, 24, 45, 66, 75, 90, 170, 802]