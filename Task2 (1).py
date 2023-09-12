#!/usr/bin/env python
# coding: utf-8

# * Write a program that calculates the `sum, difference, product, and quotient` of two numbers: 10 and 5.
# 
# * Create a program that calculates the `area of a circle` with a radius of 4.5 units.

# In[ ]:


a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a//b)


# In[ ]:


r = 4.5
area_of_circle = 3.14 * (r * r);
print(area_of_circle)


# *  Write a program that `swaps` the values of two variables:
# 
# 1.   List item
# 2.   List item
# 
# x with a value of 5 and "y" with a value of 10.
# * Create a program that calculates `compound interest` for a principal amount of $1000, an interest rate of 5%, and a time period of 3 years.

# In[ ]:


x,y = 5,10
x,y = y,x
print(x,y)


# In[ ]:


import math
p = 1000
r = 5
T = 3
A = p*(math.pow((1+(5/100)),3))
Compound_interest = A-p
print(A)
print(Compound_interest)


# * Write a program that `compares` two numbers: 7 and 12, and determines whether the first number is greater than, less than, or equal to the second number.
# * Create a program that `checks` if a person of age 18 is eligible to vote based on the voting age requirement.(True/False)

# In[ ]:


a ,b = 7,12
if(a>b):
    print("greater")
elif(a<b):
  print("less than")
elif(a==b):
  print('a is equal to b')


# In[ ]:


Age = int(input('Enter the age: '))
if Age >=18:
  print('Person is eligible to vote')
else:
  print('Person is not eligible to vote')


# In[ ]:





# * Create a program that `swaps` the values of two integers: `a` with a value of 10 and `b` with a value of 20 using
#  *  bitwise XOR (^) operator.
#  * Logical AND
#  * Logical OR
#  * Logical NOT

# In[ ]:


x ,y = 10,20 #1010,10100
x^=y #11110, 10100
y^=x #01010, 11110
x^=y
print(x,y)


# In[ ]:


x ,y = 10,20
x and y


# In[ ]:


x or y


# *  Create a Python program that calculates the `area of a rectangle`. Prompt the `user to enter` the length and width of the rectangle, `store them` in variables, and compute the area using the formula:area length width.Finally, `print the calculated area.
# 
# * Create a Python program that calculates the `average` of three exam scores. Prompt the user to enter the scores, `store them` in variables, calculate the average, and print the result.
# 
# * Write a Python program that `converts` temperature from Celsius to Fahrenheit. Prompt the user to enter a temperature in Celsius, store it in a variable, and convert it to Fahrenheit using the formula: `Fahrenheit = (Celsius* 9/5)+32`, and print the converted temperature.
# 
# * What are the `logical operators` in Python? Explain `each one` with an example.
# 
# * What are the `membership` operators in Python? Explain their usage with examples
# 
# * List and briefly explain the `basic data types` available in Python.
# 
# * Write a Python code snippet that `assigns a value to a variable `and determines its `data type` using the type() function.

# In[ ]:


l = int(input('enter the length: '))
w = int(input('enter the width: '))
a = l*w
print(a)


# In[ ]:


s1 = int(input('enter score one: '))
s2 = int(input('enter score two: '))
s3 = int(input('enter score three:'))
total = s1+s2+s3
print(total)
a = total/3
print(a)


# Write a Python program that converts temperature from Celsius to Fahrenheit. Prompt the user to enter a temperature in Celsius, store it in a variable, and convert it to Fahrenheit using the formula: Fahrenheit = (Celsius* 9/5)+32, and print the converted temperature.

# In[ ]:


Celsius = float(input())
Fahrenheit = (Celsius* (9/5))+32
print(Fahrenheit)


# Write a Python code snippet that assigns a value to a variableand determines its data type using the type() function.
# 
# 

# In[ ]:


A = 'Hello'
print(type(A))


# In[ ]:


B = 1.1
print(type(B))


# In[ ]:


C = 11
print(type(C))
D = [1,2,3,4]
E = {1,2,3,3}
F = (1,1,2,2,3,3)
G = {'a':'10','b':'20'}
print(type(C))
print(type(D))
print(type(E))
print(type(F))
print(type(G))
print(E)


# In[ ]:





# Assignment: Basic Python Operators
# 
# **Task 1: Arithmetic Operators**
# 1. Write a Python program that takes two user-input numbers and displays their sum using the addition operator.
# 2. Create a program to calculate the area of a rectangle. Prompt the user for the length and width, then use multiplication to find the area.
# 3. Implement a program that converts temperature from Celsius to Fahrenheit using the formula: Fahrenheit = (Celsius * 9/5) + 32.
# 
# **Task 2: Comparison Operators**
# 1. Write a program that compares two user-input numbers and prints whether the first number is greater than the second number or not.
# 2. Create a program that determines whether a user-input year is a leap year or not. A leap year is divisible by 4 and not divisible by 100, unless it is also divisible by 400.
# 3. Implement a simple guessing game. Generate a random number between 1 and 100 and have the user guess the number. Provide feedback if their guess is too high or too low, and let them know when they've guessed correctly.
# 
# **Task 3: Logical Operators**
# 1. Write a program that checks whether a user-input number is positive and even using logical AND (`and`) operator.
# 2. Create a login system where you define a correct username and password. Ask the user for their input and compare it with the correct credentials using logical OR (`or`) operator. Provide access if either the username or password is correct.
# 3. Implement a program that determines whether a given year is a leap year and divisible by 7 using logical NOT (`not`) operator.
# 
# **Task 4: Assignment Operators**
# 1. Write a program to calculate the square of a number using the exponentiation operator (`**`) and assign it back to the same variable.
# 2. Create a program that keeps track of the total score in a game. Prompt the user for their latest score and update the total score using the addition assignment operator (`+=`).
# 3. Implement a program to convert seconds into hours, minutes, and remaining seconds using both division and modulo operators, and then assign each value using assignment operators.
# 
# **Task 5: Bitwise Operators**
# 1. Write a program that performs a bitwise AND operation between two user-input numbers and displays the result.
# 2. Create a program to toggle the nth bit of a given number. Ask the user for the number and the value of n, then use bitwise XOR (^) operator to toggle the bit.
# 3. Implement a program to swap the values of two variables without using a temporary variable, only using bitwise XOR (^) operator.
# 
# 

# 1. Write a Python program that takes two user-input numbers and displays their sum using the addition operator.
# 

# In[ ]:


a = int(input())
b = int(input())
c = a+b
print('c is', c)


# 2. Create a program to calculate the area of a rectangle. Prompt the user for the length and width, then use multiplication to find the area.
# 

# In[ ]:


L = int(input('Enter the length:'))
W = int(input('Enter the width:'))
A = L*W
print(A)


# comparison operator

# 1. Write a program that compares two user-input numbers and prints whether the first number is greater than the second number or not.
# 

# In[ ]:


S = int(input('Enter the value:'))
F = int(input('Enter the value:'))
print(S>F)


# 2. Create a program that determines whether a user-input year is a leap year or not. A leap year is divisible by 4 and not divisible by 100, unless it is also divisible by 400.
# 

# In[ ]:


Year = int(input('Enter the Year:'))
if Year%4 == 0 and Year % 100 != 0:
  print('Leap year')
else:
  print('not a leap year')


# 

# In[ ]:




