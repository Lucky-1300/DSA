# 1. Count Vowels in a String
# Write a program that takes a string and returns the number of vowels (a, e, i, o, u) in it.
# Example:
# Input: "hello"
# Output: 2


# str = "hello"
# vowels = "aeiou"
# count = 0
# for char in str:
#     if char in vowels:
#         count += 1
# print(count)



# 2. Reverse a String
# Write a program that takes a string and returns it reversed.
# Example:
# Input: "apple"
# Output: "elppa"

# str = "apple"
# reversed_str = ""
# for char in str:
#     reversed_str = char + reversed_str
# print(reversed_str)




# def naive_pattern_matching(text, pattern):
#     n = len(text)
#     m = len(pattern)
#     occurrences = []

#     for i in range(n - m + 1):
#         j = 0
#         while j < m and text[i + j] == pattern[j]:
#             j += 1
#         if j == m:
#             occurrences.append(i)

#     return occurrences


# text = "ABABABC"
# pattern = "ABA"
# result = naive_pattern_matching(text, pattern)
# print("Pattern found at indices:", result)



# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True


# print(is_palindrome("racecar")) 
# print(is_palindrome("hello"))    


# binary search
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1




children = int(input("Enter number of children: "))

if children >= 10:
    print(1000)
else:
    print(children * 200)


