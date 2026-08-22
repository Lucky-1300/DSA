# Q1. Maximum sum of K consecutive elements
# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# Find the maximum sum of any k consecutive elements.

# Expected: 9

# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# window_sum = sum(arr[:3])
# max_sum = 0
# for i in range(k,len(arr)):
#     window_sum = window_sum - arr[i-k] + arr[i]
#     if window_sum > max_sum:
#       max_sum = window_sum

   


# 3. Reverse an Array

# Given:

# arr = [10, 20, 30, 40, 50]

# Output:

# [50, 40, 30, 20, 10]

# arr = [10, 20, 30, 40, 50]
# reverse_arr = arr[0]
# for i in range(len(arr)):
#     print(i - 1)
    





# Condition: Don't use reverse() or slicing [::-1].

# Hint: Use a loop.

# 4. Find the Sum of All Elements

# Given:

# arr = [10, 20, 30, 40, 50]

# Output: 150