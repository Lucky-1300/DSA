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


players = [22,40,55,90,72,22,35]
max_num = players[0]
max2_num = players[1]


for i in range(len(players)):
    
    if players[i] > max_num:
              max2_num = max_num
              max_num = players[i]

for i in range(len(players)):
      if players[i] > max2_num and players[i] != max_num:
            max2_num = players[i]


new_players = [0] * len(players)
count = 0
qp = 0

for i in range(len(players)):
        if players[i] >= 40:
             new_players[qp] = players[i]
             qp += 1
             count += 1

star_players = [0] * len(players)
sp = 0

for i in range(len(players)):
        if players[i] >= (80 / 100) * max_num:
          star_players[sp] = players[i]
          sp += 1
  
        
        

print("Total qualified players:", count)
print("Qualified players:", new_players[:qp])
print("Maximum highest score is ", max_num)
print("second maximum highest score is", max2_num)
print("star players", star_players[:sp])









  

        
        
    
    




  

   
      






    

    
    













