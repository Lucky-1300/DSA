#17. Five easy conditional questions.

#1. Check if a number is positive ,negative, or zero.
# num = int(input("Enter a Number:"))
# if num > 0:
#     print("Number is positive")
# elif num < 0:
#     print("Number is negative")
# else:
#     print("Number is zero")



#2. Check if a number is even or odd.
# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")



#3. Find the largest of two numbers.
# num1 =  int(input("Enter number1:"))
# num2 = int(input("Enter number2:"))
# if num1 > num2:
#     print(num1, "is greater" )
# else: 
#     print(num2, "is greater")



#4.Check if a person is eligible to vote(age >= 18).
# age = int(input("Enter age:"))
# if age >= 18:
#     print("Person is eligible to vote")
# else:
#     print("Person is not eligible to vote")



#5. Check if a number is divisible by 5 and 11.
# num = int(input("Enter a number:"))
# if num % 5 == 0 and num % 11 == 0:
#     print("Number is divisible by 5 and 11")
# else:
#     print("Number is not divisible by 5 and 11")



#6.Check if a year is a leap year.
# year = int(input("Enter a year:"))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")




#7.Check if a character is a vowel or consonant.
# char = input("Enter a character:")
# if char in 'aeiouAEIOU':
#     print("Vowel")
# else:
#     print("Consonant")




#8.Check if a character is an alphabet, digit, or special symbol.
# char = input("Enter a character:")
# if char.isalpha():
#     print("Alphabet")
# elif char.isdigit():
#     print("Digit")
# else:
#     print("Special Symbol")




#9.Find the smallest of three numbers.
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# num3 = int(input("Enter a number:"))
# if num1 > num2 and num1 > num3:
#     print(num1, "is greatest")
# elif num2 > num1 and num2 > num3:
#     print(num2, "is greatest")
# else:
#     print(num3, "is greatest")





#10.Check if a number is multiple of both 3 and 7.
# num = int(input("Enter a number:"))
# if num % 3 == 0 and num % 7 == 0:
#     print(num,"number is multiple of both 3 and 7")
# else:
#     print(num,"number is not multiple of both 3 and 7")





# 11."Find the grade of a student based on marks:
# 90–100 → A, 80–89 → B, 70–79 → C, 60–69 → D, else → F."
# marks = int(input("Enter the marks:"))
# if marks >= 90 and marks <= 100:
#     print("A")
# elif marks >= 80 and marks <= 89:
#     print("B")
# elif marks >= 70 and marks <= 79:
#     print("C")
# elif marks >= 60 and marks <= 69:
#     print("D")
# else:
#     print("F")






# 12.Check whether a character is uppercase, lowercase, or not an alphabet.
# char = input("Enter a character: ")
# if 'A' <= char <= 'Z':
#     print("Uppercase Alphabet")
# elif 'a' <= char <= 'z':
#     print("Lowercase Alphabet")
# else:
#     print("Not an Alphabet")


# 13.Determine if a year, month, and day form a valid date.



# 14.Take an integer input and check if its last digit is 3 or not.

# num = int(input("Enter a number:"))
# if num == 3:
#     print("last digit is 3")
# elif num % 10 == 3:
#     print("last digit is 3")
# else:
#     print("last digit is  not 3")






# 15.Check if a number is within a range (e.g., 10 ≤ num ≤ 50).
# num = int(input("Enter a number:"))
# if num >= 10 and num <= 50:
#     print("number is within a range of 10 to 50")
# else:
#     print("number is not in range")


#16. Check if a given time (hours, minutes) is valid or not.


#17. Accept a temperature and print if it’s “Cold”, “Warm”, or “Hot” based on ranges.


# 18.Check if three angles form a valid triangle.
# side1 = int(input("Enter side one :"))
# side2 = int(input("Enter side two :"))
# side3 = int(input("Enter side three :"))
# if (side1 + side2 + side3 == 180):
#     print("It's a valid triangle")
# else:
#     print("It's not a valid triangle")



#19. Check if the sum of any two numbers equals the third (like 2 + 3 = 5).
# num1 = int(input("Enter a number :"))
# num2 = int(input("Enter a number :"))
# totalNum = int(input("Enter a number :"))
# if (num1 + num2 == totalNum):
#     print("Yes , the sum of two numbers are equals to the ", totalNum)
# else:
#     print("No , the sum of two numbers are equals to the ", totalNum)






# "Grade Assignment With Edge Cases
# Write a program that assigns grades based on marks:
# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → F
# But if marks are exactly 100, print ""Perfect Score!""."
# marks = int(input("Enter a number:"))
# if marks == 100:
#     print("Perfect Score")
# elif marks <= 100 and marks >= 90:
#     print("A")
# elif marks <= 89 and marks >= 80:
#     print("B")
# elif marks <= 79 and marks >= 70:
#     print("C")
# elif marks <= 69 and marks >= 60:
#     print("D")
# elif marks < 60:
#     print("F")







# "2️⃣ Leap Year + Century Check




# Given a year:

# If it's a leap year, print ""Leap Year"".

# If it's divisible by 100 but not 400, print ""Century but not a leap year"".
# Otherwise, print ""Normal Year""."



# "3️⃣ Complex Password Validator

# Check password validity:

# Length ≥ 8

# At least 1 uppercase

# At least 1 lowercase

# At least 1 digit

# At least 1 special symbol
# If any condition fails, print exactly which rule failed."



# "4️⃣ ATM Withdrawal Logic

# Given balance, withdrawal amount, and account type:

# If withdrawal <= balance:

# If account type is ""premium"", allow overdraft up to ₹5000.

# If account type is ""normal"", no overdraft allowed.

# Otherwise, print ""Insufficient Balance""."



# "5️⃣ Movie Ticket Pricing

# Input: age, day of week, and time (matinee or night).

# Children (<13) and seniors (>60) get 50% off.

# Weekend shows cost +₹100 extra.

# Matinee shows cost 30% less.
# Calculate the final ticket price."






# "6️⃣ Triangle Type Validator
# Given 3 sides:
# Check if they form a triangle.
# If yes:
# If all sides equal → Equilateral
# If two sides equal → Isosceles
# If all sides different → Scalene
# If they don’t form a valid triangle, print ""Invalid Triangle""."
# side1 = int(input("Enter a side :"))
# side2 = int(input("Enter a side :"))
# side3 = int(input("Enter a side :"))


# if(side1 + side2 + side3 != 180):
#     print("Invalid Triangle")
# elif (side1 == side2) and (side2 == side3):
#     print("It is a Equilateral Triangle")
# elif(side1 == side2) or (side1 == side3) or (side2 == side3):
#     print("It is a Isosceles Triangle")
# elif(side1 != side2) or (side2 != side3):
#     print("It is a Scalene Triangle")






# "7️⃣ Electricity Bill Calculation

# Based on units:

# 0–100 → ₹5/unit

# 101–200 → ₹7/unit

# 200+ → ₹10/unit
# If the bill exceeds ₹2000, add 5% surcharge."







# "8️⃣ Login System With Lock

# Given username, password, and number of failed attempts:

# If correct → ""Login Successful""

# If wrong but attempts < 3 → ""Try Again""

# If attempts = 3 → ""Account Locked"""




# "9️⃣ Weather Advisory

# Given temperature and humidity:

# Temp > 40 and humidity < 40 → ""Heat Wave Alert""

# Temp < 10 and humidity > 60 → ""Cold & Humid — Wear Layers""

# Temp between 20–30 → ""Comfortable Weather""

# Else → ""Normal Day"""






# "🔟 Advanced Number Check

# Given a number n:

# If n is divisible by both 3 & 5 → ""FizzBuzz""

# If n is prime → ""Prime Number""

# If n is even and > 100 → ""Large Even Number""

# Else → ""Just a Number"""
 