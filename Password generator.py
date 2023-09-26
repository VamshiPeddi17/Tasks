#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('No of passwords to generate: ')
number = int(number)

length = int(input('Length of password to generate: '))

print('\nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range (length):
        passwords += random.choice(chars)
    print(passwords)


# In[ ]:




