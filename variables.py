# Print "Hello, World!"
# Take your name as input and print a greeting.
# Take two numbers and print their sum.
# Swap two numbers (using a temporary variable).
# Swap two numbers (without a temporary variable).
# Find the area of a rectangle.
# Find the area of a circle.
# Convert Celsius to Fahrenheit.
# Convert kilometers to miles.
# Find the simple interest.


# print("hello world!")

# name = "Lucky Ray"
# print("Welcome Back" , name)

# num1 = 5
# num2 = 6
# sum = num1 + num2
# print(sum)

# a = 5
# b = 6
# temp = a
# a = b
# b = temp

# print("a" , a)
# print("b" , b)


# c = 8
# d = 10
# c,d = d,c
# print("c" , c)
# print("d",d)

# arr = [1,2,5,6,2]

# greater = arr[0]

# for i in range(len(arr)):
#     if arr[i] > greater:
#      greater = arr[i]
    
# print("greater", greater)


# arr1 = [2,5,6,1,3,2,6,4,1]
# new_arr = []

# for i in range(len(arr1)):
#     for j in range(i+1 , len(arr1)):
#         if arr1[i] == arr1[j]:


# for i in range(1,11):
#     print(i)


# str = "lucky"
# reverse = ""
# for char in str:
#     reverse = char + reverse
# print(reverse)



# arr = [1,2,3]
# min = arr[0]
# max = arr[0]

# for i in range(1,len(arr)):
#     if arr[i] > max:
#         max = arr[i]
#     if arr[i] < min:
#         min = arr[i]

# print(max, min)





# n = 123

# r = n % 10 
# q = n // 10

# num1 = n % 10
# num2 = q % 10


# num3 = q // 10


# n = "123"
# reverse = ""

# i = len(n) - 1

# while i >= 0:
#     reverse = reverse + n[i]
#     i -= 1

# print(reverse)


    


  # Moves the cursor to the next line


 
# d
# n = 7
# first = 0
# second = 1
# print(first)
# print(second)
# next = (first+second)
# print(next)


# first = second
# second = next
# next = (second+ next)
# print(next)
# print(second + next)




# n = int(input("Enter a number:"))
# if n <= 1:
#     print("Not a prime number")
# elif n !=  2 and n % 2 == 0:
#     print("Not a prime number")
# else:
#     print("prime number")

# num = -10
# if num > 0:
#   for i in range(1 , num + 1 ):
#       if num % i == 0:
#         print(i)

# if num < 0:
#   num = -num
#   for i in range(1 , num + 1 ):
#       if num % i == 0:
#         print(-i)


# A = int(input("Enter A: "))
# B = int(input("Enter B: "))

# if B % A == 0:
#     print("Yes, A is a factor of B")
# else:
#     print("A is not a factor of B")



# a = int(input("Enter a first side :"))
# b = int(input("Enter a second side :"))
# c = int(input("Enter a third side :"))


# if a == b:
#   if b == c:
#       print("It is a Equilateral Triangle")
#   else:
#      print("It is a  Isosceles Triangle")
# elif b == c:
#    print("Isosceles Triangle")
# elif c == a:
#    print("Isosceles Triangle")
# else:
#    print("scalene Triangle")



# a = int(input("Enter a first side :"))
# b = int(input("Enter a second side :"))
# c = int(input("Enter a third side :"))


# if a*a + b*b == c*c:
#     print("It is a Right Angled Triangle")
# elif b*b + c*c == a*a:
#     print("It is a Right Angled Triangle")
# elif a*a + c*c == b*b:
#     print("It is a Right Angled Triangle")
# else:
#     print("Not a Right Angled Triangle")



# a = int(input("Enter a Number: "))

# if a % 5 == 0:
#     if a % 11 == 0:
#         print("Divisible by both")
#     else:
#         print("Divisible by 5")
# elif a % 11 == 0:
#     print("Divisible by 11")
# else:
#     print("Not divisible by both")


# a = int(input("Enter side1: "))
# b = int(input("Enter side2: "))
# c = int(input("Enter side3: "))
# d = int(input("Enter side4: "))
# ang = int(input("Enter angle: "))

# if a == b == c == d:
#     if ang == 90:
#         print("It is a Square")
#     else:
#         print("It is a Rhombus")

# elif a == c:
#     if b == d:
#         if ang == 90:
#             print("It is a Rectangle")
#         else:
#             print("It is a Parallelogram")
#     else:
#         print("It is an Irregular Quadrilateral")

# else:
#     print("It is an Irregular Quadrilateral")




# a = int(input("Enter Rockwell Hardness: "))
# b = float(input("Enter Carbon Content: "))
# c = int(input("Enter Tensile Strength: "))

# if a > 50:
#     if b > 0.7:
#         if c > 5600:
#             print("Grade 10")
#         else:
#             print("Grade 9")
#     else:
#         if c > 5600:
#             print("Grade 7")
#         else:
#             print("Grade 6")

# else:
#     if b > 0.7:
#         if c > 5600:
#             print("Grade 8")
#         else:
#             print("Grade 6")
#     else:
#         if c > 5600:
#             print("Grade 6")
#         else:
#             print("Grade 5")




# **Today's question**
# A company has N employees. Each employee has completed a certain number of tasks.
# An employee is eligible for a bonus if:
# Tasks completed ≥ 50
# AND tasks completed is an even number.
# Print the number of eligible employees.


# Now store the task counts of only the eligible employees in a new array.
# Print the new array.


# The company wants to reward the top performer among the eligible employees.
# Find:
# Highest task count
# Second highest task count


# Employees are promoted if:
# They are eligible for a bonus (Problem 2)
# AND their task count is at least 90% of the highest task count (Problem 3).
# Print the promoted employees.


# def count_eligible_employees(tasks):
#   count = 0
#   for t in tasks:
#     if t >= 50 and t % 2 == 0:
#       count += 1
#       print(count)



# N = int(input("Enter total No. of employee :"))
# count= 0
# for i in N:
#   if i >= 50 and i % 2==0:
#     count += 1
#     print(count)



# arr = [20, 30, 40, 50, 60, 70, 72, 85]
# new_arr = []

# for i in range(len(arr)):
    
#     if arr[i] >= 50 and arr[i] % 2 == 0:
#         new_arr.append(arr[i])
    

# print(new_arr)
# print(len(new_arr))
# print(max(new_arr, "is the highest employee task"))


# arr = [6,3,4,5,8]
# max = 0

# for i in range(len(arr)):
#     if arr[i] >= max:
#         max = arr[i]

# print(max)


# players = [22,40,55,90,72,22,35]
# max_num = players[0]
# max2_num = players[1]


# for i in range(len(players)):
    
#     if players[i] > max_num:
#               max2_num = max_num
#               max_num = players[i]

# for i in range(len(players)):
#       if players[i] > max2_num and players[i] != max_num:
#             max2_num = players[i]


# new_players = [0] * len(players)
# count = 0
# qp = 0

# for i in range(len(players)):
#         if players[i] >= 40:
#              new_players[qp] = players[i]
#              qp += 1
#              count += 1

# star_players = [0] * len(players)
# sp = 0

# for i in range(len(players)):
#         if players[i] >= (80 / 100) * max_num:
#           star_players[sp] = players[i]
#           sp += 1
  
        
        

# print("Total qualified players:", count)
# print("Qualified players:", new_players[:qp])
# print("Maximum highest score is ", max_num)
# print("second maximum highest score is", max2_num)
# print("star players", star_players[:sp])




# 1. Find the Largest Element in an Array ⭐ (Classic Beginner)

# Problem:
# Given an array of integers, find the largest element.

# Input
# arr = [12, 45, 7, 89, 23]
# Output
# 89
# Example 2

# Input

# arr = [-5, -2, -10, -1]

# Output

# -1
# Constraints
# 1 <= n <= 10^5
# -10^9 <= arr[i] <= 10^9
# Approach
# Assume the first element is the largest.
# Traverse the array.
# If the current element is greater than the largest, update it.
# Print the largest element.
# Time Complexity
# O(n)
# Space Complexity
# O(1)
# Other Classic Array Problems (Solve in this order)


# arr = [12, 45, 7, 89, 23]
# largest = arr[0]

# for i in range(len(arr)):
#   if largest < arr[i]:
#     largest = arr[i]


# print(largest)


# arr = [-5, -2, -10, -1]
# max = arr[0]
# for i in range(len(arr)):
#     if max < arr[i]:
#         max = arr[i]
# print(max)


# Problem 1: Decode the Message
# Each number represents an ASCII code.
# Convert all numbers into characters and print the hidden message.
# Input: 72 69 76 76 79
# Output: HELLO

# input_numbers = [72, 69, 76, 76, 79]
# hidden_message =  ''.join(chr(n) for n in input_numbers)
# print(hidden_message)

# Problem 2: Hide the Vowels
# Replace every vowel (A, E, I, O, U) with .
# Input: HELLO
# Output: HLL*

# input_str = "HELLO"
# output_str = ""

# for char in input_str:
#     if char in "AEIOU":
#         output_str += "*"
#     else:
#         output_str += char

# print(output_str)

# Problem 3: Longest Word
# Words are separated by a space character (ASCII 32).
# Find the longest word in the decoded message.
# Input: HELLO WORLD CHATGPT
# Output: CHATGPT

# input_str = "HELLO WORLD CHATGPT"
# words = input_str.split() 

# longest_word = ""
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word

# print(longest_word)

# Problem 4: Frequency Analysis
# Find the most frequently occurring alphabet in the decoded message.
# Ignore spaces.
# If two letters have the same frequency, print the alphabet that appears first.




# Problem 1: Find the First Empty Parking Slot
# A parking lot has N parking slots.
# Each slot contains:
# 0 → Empty
# 1 → Occupied
# Find the index of the first empty parking slot.
# If all slots are occupied, print "Parking Full".
# Input: 1 1 1 0 1 0
# Output: 3

# arr = [1, 1, 1, 0, 1, 0]

# empty_arr = 0
# for i in range(len(arr)):
#     if arr[i] == 0:
#         empty_arr = i
#         print(i)
#         break
    
# else:
#     print("parking full")


    
# Problem 2: Largest Continuous Empty Area
# Find the longest continuous sequence of empty parking slots.
# Input: 1 0 0 0 1 0 0
# Output: Length = 3

# arr = [1,0,0,0,1,0,0]
# current_zero = 0
# longest_zero = 0

# for i in range(0,len(arr)):
#     if arr[i] == 1:
#         current_zero = 0
#     elif arr[i] == 0:
#         current_zero = current_zero + 1

#         if current_zero > longest_zero:
#             longest_zero = current_zero

# print("longest zero :" ,longest_zero)
       

# Problem 3: Bus Parking
# A bus requires K consecutive empty slots.
# Determine whether the bus can be parked.
# Input: Slots:1 0 0 0 1 0 0
#            K = 3
# Output: YES

# arr = [1,0,0,0,1,0,0]
# current_zero = 0
# longest_zero = 0
# K = 3

# for i in range(0,len(arr)):
#     if arr[i] == 1:
#         current_zero = 0
#     elif arr[i] == 0:
#         current_zero = current_zero + 1

#         if current_zero > longest_zero and current_zero == K:
#             longest_zero = current_zero
            
# print("yes")


# Problem 4: Best Parking Location
# If there are multiple locations where the bus can park, choose the parking block that lies in the middle among all the valid parking locations.
# If the number of valid parking locations is odd, choose the exact middle one.
# If the number of valid parking locations is even, choose the left-middle parking location.
# Print the starting index of the selected parking block.
# Input: Parking Slots: 0 0 0 1 0 0 0 1 0 0 0
# Output: 4 

# arr = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
# parking_location = 0
# even = 0
# odd = 0
# for i in range(len(arr)):
#     if arr[i] == 0:
#         parking_location = parking_location + 1
#         parking_location % 2 != 0
        
# print(parking_location)


        
# remove all the duplicate without using inbuilt function

# output = 3 4 6 2 8 1

# arr = [3, 4, 6, 2, 8, 4, 3, 4, 3, 2, 1]   
# new_arr = []

# for i in range(len(arr)):
#     if arr[i] not in new_arr:
#         new_arr.append(arr[i])

# print(new_arr)  

# arr = [1 ,1, 2, 2, 3 ,3 ,4, 5 ,5]
# new_arr = []
# for i in range(len(arr)):
#     if arr[i] not in new_arr:
#         new_arr.append(arr[i])
    
    
        
    
    




  

   
      






    

    
    













