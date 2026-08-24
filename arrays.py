#Q1. Maximum and minimum of an array using minimum number of comparisonsa

# arr = [5, 2, 8, 1, 9, 3]

# min_val = arr[0]
# max_val = arr[0]

# for i in range(1, len(arr)):
#     current_element = arr[i]
#     if current_element > max_val:
#        max_val = current_element
#     if current_element < min_val:
#        min_val = current_element


# print("Maximum value:", max_val)
# print("Minimum value:", min_val)




# Q2. Array Reverse

# arr = [10, 20, 30, 40, 50]
# start = 0
# end = len(arr) - 1

# while(end > start):

#    arr[start] , arr[end] = arr[end] , arr[start]

#    start += 1
#    end -= 1

# print(arr)


# Q3. Maximum Subarray

# arr = [2, -3, 4, -1, 5]

# current_max = 0 
# global_max = arr[0]

# for i in range(len(arr)):
#       current_max += arr[i]
#       if current_max > global_max:
#          global_max = current_max
#       if current_max < 0:
#          current_max = 0

# print("Maximum Subarray Sum:", global_max)


# Q4. Contains Duplicate

# arr = [1, 2, 3, 2, 5]

# def contains_duplicate(arr):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] == arr[j]:
#                 return True
#     return False  

# print(contains_duplicate(arr))



# Q5. Print all even numbers in an array

# arr = [1,2,3,4,5,6]

# even_list = []
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         even_list.append(arr[i])

# print(even_list)



# Q6.Print all odd numbers in an array

# arr = [1,2,3,4,5,6,7]

# odd_list = []

# for i in range(len(arr)):
#     if arr[i] % 2 != 0:
#         odd_list.append(arr[i])

# print(odd_list)


# 7.Find the Majority Element

# arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
# def find_majority_element(arr):
#     count = {}
#     majority_count = len(arr) // 2

#     for num in arr:
#         if num in count:
#             count[num] += 1
#         else:
#             count[num] = 1

#         if count[num] > majority_count:
#             return num

#     return None

# print(find_majority_element(arr))



# Q8. Longest Prefix that is also Suffix

# arr = "ababcababc"

# def longest_prefix_suffix(arr):
#     n = len(arr)
#     lps = [0] * n
#     length = 0
#     i = 1

#     while i < n:
#         if arr[i] == arr[length]:
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             if length != 0:
#                 length = lps[length - 1]
#             else:
#                 lps[i] = 0
#                 i += 1

#     return lps[-1]

# print(longest_prefix_suffix(arr))


#9 Check if an Array is Sorted (Non-decreasing)
# arr = [1, 2, 3, 4, ]

# is_sorted = True

# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         is_sorted = False
#         break

# if is_sorted:
#     print("Array is sorted")
# else:
#     print("Array is not sorted")


#10. Move all zeros to the end of the array
# arr = [0, 1, 0, 3, 12]
# non_zero_index = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr[non_zero_index] = arr[i]
#         non_zero_index += 1

# while non_zero_index < len(arr):
#     arr[non_zero_index] = 0
#     non_zero_index += 1

# print(arr)




#11. Find the Second Largest Element in an Array
# arr = [12, 35, 1, 10, 34, 10]
# first = second = float('-inf')
# for number in arr:
#     if number > first:
#         second = first
#         first = number
#     elif number > second and number != first:
#         second = number

# print("Second Largest Element:", second)


#12.Just put the numbers in order from smallest to biggest.

# arr = [5, 2, 3, 1]

# for i in range(len(arr)):
#     for j in range(len(arr) - 1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# print(arr)

     

#Q13. Count the number of elements in an array
# arr = [10,20,30,40]
# count = 0
# for i in range(len(arr)):
#     count = count + 1
    

# print("Count of elements is :", count)


#Q12. Sum of all elemments in array
# arr = [1,2,3,4,5]
# count = 0
# for i in range(len(arr)):
#     count = count + arr[i]
   
# print("sum of total elements", count)


# Q13. Binary Search
# arr = [1,2,3,4,5,6,7,8,9]
# target = 5
# left = 0
# right = len(arr) - 1
# found = False
# while left <= right:
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         found = True
#         break
#     elif arr[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if found:
#     print("Element found in the array")
# else:
#     print("Element not found in the array")



#14.Reverse an array.

# arr =  [1, 2, 3, 4, 5]
# rev_arr = []
# for i in range(len(arr)-1, -1, -1):
#     rev_arr.append(arr[i])

# print("Reversed Array:", rev_arr)



#15. Remove duplicate numbers from list.
# def remove_consecutive_twins(arr):
#     if not arr:
#         return []
#     result = []
#     prev = None
#     for num in arr:
#         if num != prev:
#             result.append(num)
#             prev = num
#     return result


# print(remove_consecutive_twins([1, 1, 2, 2, 3, 3, 2]))

    


#16. Find the intersection of two arrays.
# arr1 = [1, 2, 2, 3, 4]
# arr2 = [2, 2, 4, 6]

# intersection = []

# for i in arr1:
#     for j in arr2:
#         if i == j:
#             intersection.append(i)
#             arr2.remove(j)   

# print("Intersection:", intersection)




# x in arr returns True if x exists in the list arr, otherwise False.
#  Check if an element exists in an array.

# arr = [1,2,3,4]
# x = 3
# if x in arr:
#     print("True")
# else:
#     print("False")





# Find the first non-repeating character in a string.
# Go through each letter one by one.
# Check if it appears only once.
# If yes → print its place and stop.
# If no letter is unique → print -1.

# s = "aabb"

# for i in range(len(s)):
#     if s.count(s[i]) == 1:
#         print(i)
#         break
# else:
#     print(-1)









#Bubble Sort
# arr = [5,2,9,1,5,6]
# n = len(arr)g
# for i in range(len(arr)):
#     for j in range(n - i - 1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
# print(arr)




#  Count occurrences of a character
# Input: string = "banana", char = "a"
# Output: 3
# word = "banana"
# count = 0
# for char in word:
#     if char == "a":
#        count += 1

# print(count)


# 3. Count even numbers in an array
# Input: [2, 5, 6, 7, 8]
# Output: 3
# arr = [2, 5, 6, 7, 8]
# count = 0
# for i in range(len(arr)):
#      if i % 2 == 0:
#         count += 1


# print(count)

     



# Find the smallest element in an array. Input: [4, 2, 9, 1, 7]
# Output: 1



# arr = [4, 2, 9, 1, 7]
# smallest = min(arr)
# print(smallest)



# Check if two strings are anagrams (same letters, different order).Input: "listen", "silent"
# Output: True

# s1 = "listen"
# s2 = "silent"

# def are_anagrams(a, b):
#     return sorted(a) == sorted(b)

# print(are_anagrams(s1, s2))




# Move all zeros to the end of the array while keeping order.Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# arr = [0, 1, 0, 3, 12]

# new_arr = []
# zeros = []

# for num in arr:
#     if num == 0:
#         zeros.append(0)
#     else:
#         new_arr.append(num)

# result = new_arr + zeros

# print(result)


# Find the second smallest number
# arr = [12, 5, 7, 3, 9]
# arr.sort()
# print("Second smallest =", arr[1])


# Use Linear Search to find the number 7 in the array:
# [2, 4, 7, 1, 9]
# At which index is it found?
# arr = [2,4,7,1,9]
# target = 7
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)



# Use Selection Sort to sort the array:
# [29, 10, 14, 37, 13]
# arr = [29, 10, 14, 37, 13]
# for i in range(len(arr)):
#     min_idx = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_idx]:
#             min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]

# print("Sorted array:", arr)





# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high ) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# arr = [2,4,6,8,10,12,14,16]
# target = 10
# index = binary_search(arr,target)
# print(index)


# Question: Sum of Array Elements
# arr = [1,2,3,4,5]
# total = 0
# for i in range(len(arr)):
#     total = total + arr[i]
# print(total)



# arr = [4, 7, 1, 9, 2]

# max = arr[0]

# for i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]

# print(max)


# numbers = [2, 7, 11, 15]
# target = 9

# for i in range(len(numbers)):
#    for j in range(i+1,len(numbers)):
#       print(i,j)
    

# numbers = [2, 7, 11, 15]
# target = 9

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print([i + 1, j + 1]) 



# Ques1 Write a Python program that takes a list of integers and prints the sum of squares of all even numbers in the list.

# Input: [1, 2, 3, 4, 5, 6]
# Output: 56   (2² + 4² + 6² = 4+16+36)

# arr = [1, 2, 3, 4, 5, 6]
# sum_of_squares = 0

# for n in arr:
#     if n % 2 == 0:
#         sum_of_squares += n ** 2

# print(sum_of_squares)

# Ques2 Write a program to find the second largest number in a list without using sort(), sorted(), or max(). Use a loop and conditionals only.



# Input: [10, 5, 20, 8, 20, 15]
# Output: 15

# arr =[10, 5, 20, 8, 20, 15]
# max = 0
# sec_max = 0
# for i in range(len(arr)):
#     if arr[i] > max:
#         sec_max = max
#         max = arr[i]
#     elif arr[i] > sec_max and arr[i] != max:
#         sec_max = arr[i]
    
# print(sec_max)


# Ques3 Given a list of numbers, write a program that removes duplicate elements while preserving the original order of first occurrence. Don't use set().

# Input: [4, 5, 4, 6, 5, 7, 8, 7]
# Output: [4, 5, 6, 7, 8]

# arr = [4, 5, 4, 6, 5, 7, 8, 7]
# new_arr = arr[0]
# for i in range(len(arr)):
#     new_arr ^= arr[i]
   
# print(new_arr)



# Ques4 Given a list of integers and a target value, write a program to find all unique pairs of numbers from the list that add up to the target. Each pair should be printed only once (no repeats, no reversed duplicates like (2,8) and (8,2) both showing).

# Input: nums = [2, 7, 4, 3, 6, 8, 1], target = 9
# Output: (2, 7), (3, 6), (8, 1)

# Hint: Use nested loops to check every combination, but keep a way to track "already used" pairs, so you don't print the same pair twice.



# def longest_consecutive(arr):
#     nums = set(arr)
#     longest = 0

#     for num in nums:
        
#         if num - 1 not in nums:
#             current = num
#             count = 1

#             while current + 1 in nums:
#                 current += 1
#                 count += 1

#             longest = max(longest, count)

#     return longest


# arr = [100, 4, 200, 1, 3, 2]

# print(longest_consecutive(arr))

# arr = ["success", "fail","fail","success","fail","fail","fail"]

# for i in range(len(arr)):
#     if arr[i] == "fail" and arr[i-1] == "fail" and arr[i-2] == "fail":
#        print(i)
       

# arr = ["O","R", "E", "O","E","E","R"]
# for i in range(1,len(arr)):
#     if arr[i] == "E" and arr[i - 1] == "E":
#         print("Alert triggered at", i)
#         break
# else:
#     print("No Escalation pattern")
   

# arr = [100,105,95,130,90,110]
# max = 0

# for i in range(len(arr) - 1 ):
#     diff = arr[i] - arr[i + 1]
#     if diff > max:
#         max = diff
    

#     else:
#         max = max
# print(max,i-1,"to",i)


# arr = [[8,8,0,8,8,0,0],
#        [8,8,8,8,8,8,0],
#        [0,8,8,0,8,0,0]]

# max = 0

# for i in range(len(arr)):
#     total = 0

#     for j in range(len(arr[i])):
#         total = total + arr[i][j]

#     if total > max:
#         max = total
    # else:
    #     max = max

# print(max)

    



# arr = [1, 2, 3, 4, 5]
# total = 0

# for i in range(len(arr)):
#     if arr[i]:
#         total = total + arr[i]
#     else:
#         total = total

# print(total)

# arr = [0,1,0,0,1,1,0,1,0]
# count = 0

# for i in range(1,len(arr)):
#     if arr[i] == 1:
#         if arr[i+1] == 0 and arr[i-1] ==0:
#             count += 1

# print(count)


# arr = [120,160,180,140,155,170,190,130]
# count_veg = 0
# max = 0

# for i in range(len(arr)):
#     if arr[i] > 150:
#         if arr[i] > max:
#             max = arr[i]
#             count += 1
# print(count)

        
# arr = ["Veg", "Veg", "NonVeg", "NonVeg", "NonVeg", "Veg", "NonVeg", "NonVeg"]

# count_veg = 0
# count_nonveg = 0
# max_veg = 0
# max_nonveg = 0

# for i in range(len(arr)):
#     if arr[i] == "Veg":
#         count_veg += 1
#         count_nonveg = 0

#         if count_veg > max_veg:
#             max_veg = count_veg

#     else:
#         count_nonveg += 1
#         count_veg = 0

#         if count_nonveg > max_nonveg:
#             max_nonveg = count_nonveg

# if max_veg > max_nonveg:
#     print("Longest streak:", max_veg, "(Veg)")
# else:
#     print("Longest streak:", max_nonveg, "(NonVeg)")


# Student A: ["A", "B", "C", "C", "D", "A", "B", "D", "C", "A"]
# Student B: ["D", "B", "C", "C", "D", "A", "B", "C", "C", "A"]

# OUTPUT: [(1, 6)]
   
        

# raq and sts 
# stacks and llm 





# arr = [1,2,4,5,6]
# count = 0
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         count += 1
# print(count)







# 🟢 Level 1 — Basic Array Operations
# Print all elements of an array.
# arr = [1,2,3,45]
# print(arr)
# Find the length of an array.
# arr = [1,2,3,45]
# print(len(arr))
# Find the first element of an array.
# print(arr[0])
# Find the last element of an array.
# print(arr[-1])
# Print elements at even indexes.

# Print elements at odd indexes.
# Print the array in reverse order.
# Find the sum of all elements.
# Find the average of all elements.
# Find the largest element in an array.

# 🟢 Level 2 — Min, Max & Counting
# Find the smallest element in an array.
# Count how many even numbers are present.
# Count how many odd numbers are present.
# Count positive numbers.
# Count negative numbers.
# Count zeros in an array.
# Find the sum of even numbers.
# Find the sum of odd numbers.
# Find the largest even number.
# Find the smallest odd number.
# 🟡 Level 3 — Searching
# Search whether a given number exists in an array.
# Find the index of a given number.
# Count how many times a given number occurs.
# Find the first occurrence of a number.
# Find the last occurrence of a number.
# Print all numbers greater than 10.
# Print all numbers smaller than 10.
# Print numbers divisible by 5.
# Find whether all elements are positive.
# Find whether the array contains zero.
# 🟡 Level 4 — Simple Modifications
# Replace all negative numbers with 0.
# Replace all zeros with 1.
# Double every element of an array.
# Square every element of an array.
# Add 5 to every element.
# Remove the first element from an array.
# Remove the last element from an array.
# Insert an element at the beginning.
# Insert an element at the end.
# Reverse an array without using reverse().
# 🟠 Level 5 — Basic Logic
# Find the second largest element.
# Find the second smallest element.
# Check whether an array is sorted in ascending order.
# Check whether an array is sorted in descending order.
# Find duplicate elements.
# Count the number of duplicate elements.
# Remove duplicate elements.
# Find the common elements between two arrays.
# Find the difference between the largest and smallest element.
# Find the element that occurs the maximum number of times.



# Ques1: License Plate Palindrome Checker 🚗 (Using Loops)
# A license plate is called a palindrome if it reads the same forwards and backwards.
# Write a function to check if a given plate number is a palindrome.

# INPUT: "RACECAR"
# OUTPUT: True
# INPUT: "DL8CAF9"
# OUTPUT: False

# text = "RACECAR"

# i = 0
# j = len(text) - 1

# print(len(text))
# while i < j:
#     if text[i] != text[j]:
#         print("no")
#         break

#     i += 1
#     j -= 1
# else:
#     print("yes")

# Ques3: Movie Ticket Price Calculator 🎟️ 
# A cinema calculates ticket price using these rules:
# Age below 5 → Base price ₹0 (free)
# Age 5–11 → Base price ₹150
# Age 60 or above → Base price ₹100
# Everyone else → Base price ₹250
# On top of that:
# If it's a weekend, add ₹50 to the price
# If the person has a student card AND is between 12–59 years old, subtract ₹50
 
# INPUT: age = 25, is_weekend = True, has_student_card = True
# OUTPUT: 250

# age = int(input("Enter your age :"))
# is_weekend = input("Is it weekend? (True/False): ") == "True"
# has_student_card = input("Do you have a student card? (True/False): ") == "True"


# if age < 5:
#     price = 0

# elif age <= 11:
#     price = 150

# elif age >= 60:
#     price = 100

# else:
#     price = 250

# if is_weekend:
#     price += 50

# if has_student_card and age >= 12 and age <= 59:
#     price -= 50

# print(price)


# Ques4: Odd-Even Vehicle Rule Checker 🚗
# Delhi runs an odd-even traffic scheme on certain days:
# On an odd date, only cars with a number plate ending in an odd digit are allowed
# On an even date, only cars with a number plate ending in an even digit are allowed

# Given a vehicle's number plate (a string like "DL8CAF3341") and today's date (a number), determine if the car is "Allowed" or "Not Allowed". If the plate has no digit at all, print "Invalid Plate".

# INPUT: plate = "DL8CAF3341", date = 15
# OUTPUT: Allowed
# (plate ends in 1 → odd digit, date 15 → odd date → match → allowed
# plate = input("Enter your plate number: ").strip()
# date = int(input("Enter today's date: "))

# if int(plate[-1]) % 2 != 0 and date % 2 != 0:
#     print("Allowed")

# elif  int(plate[-1]) % 2 == 0 and date % 2 == 0:
#     print("Allowed")
# else:
#     print( "Invalid Plate")


# Q1. Second Largest Unique Number 
# Given a list of integers, find the second largest unique number in the list.
# If there is no second largest unique number, print -1

# INPUT: [10, 5, 8, 10, 3, 8, 7]
# OUTPUT:  8

# arr = [10, 5, 8, 10, 3, 8, 7]
# max_val = float('-inf')
# sec_max = float('-inf')

# for num in arr:
#     if num > max_val:
#         sec_max = max_val
#         max_val = num
#     elif num > sec_max and num != max_val:
#         sec_max = num

# print(sec_max)  


# Q2. Count Elements Above Average 
# Given a list of integers, calculate the average of all elements and count how many numbers are strictly greater than the average.

# Do not use any built-in function to directly calculate the average.

# INPUT: [10, 20, 30, 40, 50]
# OUTPUT: 2

# Explanation:
# Average = 30
# Numbers greater than 30 are 40 and 50. 


# arr = [10, 20, 30, 40, 50]
# total = 0
# count = 0

# for i in range(len(arr)):
#     total = total + arr[i]
#     average = total / len(arr)
    
# for i in range(len(arr)):
#     if arr[i] > average:
#         count += 1
# print(count)


# Q3 Find the Missing Number 
# You are given a list containing n distinct numbers from 1 to n+1. Exactly one number is missing. Find the missing number.

# INPUT: [1, 2, 4, 5, 6]
# OUTPUT: 3

# arr = [1, 2, 4, 5, 6]

# for i in range(len(arr)):
#     if arr[i] != i + 1:
#         print(i + 1)
#         break

# Q4: Longest Increasing Streak
# Given a list of integers, find the length of the longest continuous increasing streak.
# A streak means every number must be greater than the number immediately before it.

# INPUT: [1, 2, 3, 2, 4, 5, 6, 1, 2]
# OUTPUT: Longest Increasing Streak: 4

# Because the longest streak is: 2, 4, 5, 6

# arr = [1, 2, 3, 2, 4, 5, 6, 1, 2]
# max = 0 
# count = 0

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] < arr[j]:
#             max = arr[i]
#             count += 1
#             break
        
# print(count)


# Q1: Missing Number Detective 🕵️
# An array contains numbers from 1 to n, but one number is missing. 
# Find it — without sorting the array.

# INPUT: [1, 2, 4, 5, 6, 7, 8] , here (n = 8)
# OUTPUT: Missing number: 3

# arr = [1, 2, 4, 5, 6, 7, 8]
# for i in range(len(arr)):
#     if arr[i] != i + 1:
#         print(i + 1)
#         break


# Q2: Matrix Diagonal Difference 
# Given a square matrix, find the absolute difference between the sum of its main diagonal (top-left to bottom-right) and its secondary diagonal (top-right to bottom-left).

# INPUT: 
# [[11, 2, 4],
#  [4, 5, 6],
#  [10, 8, -12]]
# OUTPUT: Absolute difference: 15
# (main diagonal: 11+5-12 = 4 | secondary: 4+5+10 = 19 | |4-19| = 15) 





# Q3: All Pairs Summing to Target 🎯 
# Given a list of numbers and a target value, find all pairs of indices (i, j) where the two numbers add up to the target. Each number can only be used once per pair (don't reuse the same index in two different pairs).

# INPUT: arr = [2, 7, 11, 15, 5, 9] , target = 9
# OUTPUT: [(0, 1)]

# arr = [2, 7, 11, 15, 5, 9]
# target = 9

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print([(i, j)])
#             break


    


# Q4: Matrix Spiral Traversal 🌀
# Given a square (or rectangular) matrix, print all its elements in spiral order — starting from the top-left, moving right, then down, then left, then up, and spiraling inward.

# INPUT:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# OUTPUT: [1, 2, 3, 6, 9, 8, 7, 4, 5]

        

            





    
    


    
   
    
    