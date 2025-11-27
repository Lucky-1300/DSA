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
year = int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")




#7.Check if a character is a vowel or consonant.
char = input("Enter a character:")
if char in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")




#8.Check if a character is an alphabet, digit, or special symbol.
char = input("Enter a character:")
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special Symbol")




#9.Find the smallest of three numbers.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))
if num1 > num2 and num1 > num3:
    print(num1, "is greatest")
elif num2 > num1 and num2 > num3:
    print(num2, "is greatest")
else:
    print(num3, "is greatest")





#10.Check if a number is multiple of both 3 and 7.
num = int(input("Enter a number:"))
if num % 3 == 0 and num % 7 == 0:
    print(num,"number is multiple of both 3 and 7")
else:
    print(num,"number is not multiple of both 3 and 7")





# 11."Find the grade of a student based on marks:
# 90–100 → A, 80–89 → B, 70–79 → C, 60–69 → D, else → F."
marks = int(input("Enter the marks:"))
if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80 and marks <= 89:
    print("B")
elif marks >= 70 and marks <= 79:
    print("C")
elif marks >= 60 and marks <= 69:
    print("D")
else:
    print("F")






# 12.Check whether a character is uppercase, lowercase, or not an alphabet.
char = input("Enter a character: ")
if 'A' <= char <= 'Z':
    print("Uppercase Alphabet")
elif 'a' <= char <= 'z':
    print("Lowercase Alphabet")
else:
    print("Not an Alphabet")


# 13.Determine if a year, month, and day form a valid date.



# 14.Take an integer input and check if its last digit is 3 or not.

num = int(input("Enter a number:"))
if num == 3:
    print("last digit is 3")
elif num % 10 == 3:
    print("last digit is 3")
else:
    print("last digit is  not 3")






# 15.Check if a number is within a range (e.g., 10 ≤ num ≤ 50).
num = int(input("Enter a number:"))
if num >= 10 and num <= 50:
    print("number is within a range of 10 to 50")
else:
    print("number is not in range")


#16. Check if a given time (hours, minutes) is valid or not.


#17. Accept a temperature and print if it’s “Cold”, “Warm”, or “Hot” based on ranges.


# 18.Check if three angles form a valid triangle.
side1 = int(input("Enter side one :"))
side2 = int(input("Enter side two :"))
side3 = int(input("Enter side three :"))
if (side1 + side2 + side3 == 180):
    print("It's a valid triangle")
else:
    print("It's not a valid triangle")



#19. Check if the sum of any two numbers equals the third (like 2 + 3 = 5).
num1 = int(input("Enter a number :"))
num2 = int(input("Enter a number :"))
totalNum = int(input("Enter a number :"))
if (num1 + num2 == totalNum):
    print("Yes , the sum of two numbers are equals to the ", totalNum)
else:
    print("No , the sum of two numbers are equals to the ", totalNum)







 