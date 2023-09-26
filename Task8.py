#!/usr/bin/env python
# coding: utf-8

# 
# **Task 1: Basic If-Else Statements**
# Write a Python program that takes an `integer as input` from the user and prints whether it is `multiple of 3 or not` using if-else statements.
# 
# **Task 2: Nested If Statements**
# Create a program that `asks the user` for their `age` and `nationality`. Depending on their age and nationality, display a different message using nested if statements. For example, if they are under 18 and from the USA, display `"You are a minor from the USA."`
# 
# **Task 3: Grade Calculator**
# Write a program that takes a student's score as input and converts it to a letter grade (A, B, C, D, or F) using if-elif-else statements. Use the following grading scale:
# - A: 90-100
# - B: 80-89
# - C: 70-79
# - D: 60-69
# - F: Below 60
# 
# **Task 4: Leap Year Checker**
# Create a Python program that checks if a given year is a leap year or not. Use conditional statements to determine whether the year is divisible by 4, 100, and 400 to decide if it's a leap year.
# 
# **Task 5: BMI Calculator**
# Write a program that calculates a person's Body Mass Index (BMI) based on their height and weight. Then, use conditional statements to categorize the BMI as Underweight, Normal, Overweight, or Obese. Provide guidance on the healthy range for BMI.(use BMI Formula)
# 
# **Task 6: Calculator with Menu**
# Build a simple calculator program that provides a menu with options for addition, subtraction, multiplication, and division. `Take user input for two numbers`and an `operation choice`. Use conditional statements to perform the selected operation and display the result.
# 
# **Task 7: Temperature Converter**
# Write a program that `converts temperatures between Celsius and Fahrenhei`t. Allow the user to `choose` the conversion direction and input the temperature value. Use conditional statements to perform the conversion based on the `user's choice`.(Do with conversion formula)
# 

# Task 1: Basic If-Else Statements Write a Python program that takes an integer as input from the user and prints whether it is multiple of 3 or not using if-else statements

# In[1]:


Number = int(input('Enter a Number: '))

if Number%3 == 0:
    print('Multiple of three')
else:
    print('Not a multiple of three')


# Task 2: Nested If Statements Create a program that asks the user for their age and nationality. Depending on their age and nationality, display a different message using nested if statements. For example, if they are under 18 and from the USA, display "You are a minor from the USA."

# In[4]:


Nationality = input('Enter the nationality:')
Age = int(input('Enter the age: '))

if Nationality == "Indian":
    if Age < 18 and Age > 0:
        print('Minor from India')
    if Age <  0:
        print('Enter correct age')
    else:
        print('Major from India')
else:
        print('Not a resident of india')


# Task 3: Grade Calculator Write a program that takes a student's score as input and converts it to a letter grade (A, B, C, D, or F) using if-elif-else statements. Use the following grading scale:
# 
# A: 90-100
# 
# B: 80-89
# 
# C: 70-79
# 
# D: 60-69
# 
# F: Below 60

# In[16]:


score = int(input('Enter the score: '))

if (score >=90) and (score <=100):
    print('Grade A')
elif (score >=80) and (score <=89):
    print('Grade B')
elif (score >=70) and (score <=79):
    print('Grade C')
elif (score >=60) and (score <=69):
    print('Grade D')
if (score >100) or (score <0):
    print('Enter a valid score')
else:
    print('Fail')


# Task 4: Leap Year Checker Create a Python program that checks if a given year is a leap year or not. Use conditional statements to determine whether the year is divisible by 4, 100, and 400 to decide if it's a leap year.

# In[19]:


Year = int(input('Enter the year: '))

if Year%4 == 0 and Year%100 == 0 and Year%400 ==0:
    print('Leap year by all 3')
if Year%4 == 0 and Year%100 == 0:
    print('Leap year by all 2')
if Year%4 == 0:
    print('Leap year')
else:
    print('Not a leap year')


# Task 5: BMI Calculator Write a program that calculates a person's Body Mass Index (BMI) based on their height and weight. Then, use conditional statements to categorize the BMI as Underweight, Normal, Overweight, or Obese. Provide guidance on the healthy range for BMI.(use BMI Formula)

# In[28]:


height = float(input("Enter your height in meters: "))
weight =float(input("Enter your Weight in Kg: "))
 
BMI=weight/(height*height)
print("BMI Calculated is:  ",BMI)
 
if(BMI>0):
    if(BMI<=16):
        print("You are very underweight")
    elif(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("Congrats! You are Healthy")
    elif(BMI<=30):
        print("You are overweight")
    else: 
        print("You are very overweight")
else:
    print("enter valid details") 


# In[ ]:


# Sir I Didn't understood 6 & 7 th questions

