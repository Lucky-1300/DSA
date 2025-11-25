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




#17. Five easy conditional questions.

#1. Check if a number is positive ,negative, or zero.
num = int(input("Enter a Number:"))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")



#2. Check if a number is even or odd.
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")



#3. Find the largest of two numbers.
num1 =  int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
if num1 > num2:
    print(num1, "is greater" )
else: 
    print(num2, "is greater")



#4.Check if a person is eligible to vote(age >= 18).
age = int(input("Enter age:"))
if age >= 18:
    print("Person is eligible to vote")
else:
    print("Person is not eligible to vote")



#5. Check if a number is divisible by 5 and 11.
num = int(input("Enter a number:"))
if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")




#6.Check if a year is a leap year.
#7.Check if a character is a vowel or consonant.
#8.Check if a character is an alphabet, digit, or special symbol.
#9.Find the smallest of three numbers.
#10.Check if a number is multiple of both 3 and 7.




    