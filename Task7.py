#!/usr/bin/env python
# coding: utf-8

# 
# **Task 1: Dictionary Basics**
# Create a Python program that defines a dictionary to store information about your `favorite book`. Include the title, author, publication year, and genre as key-value pairs. Print out the dictionary.and do atleast 5 dictionary methods on it.
# 
# **Task 2: Dictionary Lookup**
# Write a Python program that simulates a simple dictionary for translating `English words to Spanish`. Define a dictionary containing a few English words as `keys` and their corresponding Spanish translations as `values`. Allow `users to enter` an English word, and then display its Spanish translation `if it exists` in the dictionary.(use google for English to Spanish translator)
# 
# **Task 3: Student Grades**
# Create a Python program that stores the `grades of five students` in a dictionary. Allow users to input the names of the students and their respective grades. Calculate and display the `average grade` of the students.
# 
# **Task 4: Contact List**
# Build a basic contact list using a dictionary. Initially, the dictionary can be `empty`. Allow users to `add new contacts` with `names and phone numbers`. Users should also be able to search for contacts by name and display their phone numbers(use in operator).
# 
# **Task 5: Dictionary Iteration**
# Write a Python program that defines a dictionary containing the names of `fruits as keys` and their corresponding `colors as values` (e.g., 'apple': 'red').Do atleast 5 dictionary methods on it.
# 

# ** Task 1: Dictionary Basics Create a Python program that defines a dictionary to store information about your favorite book. Include the title, author, publication year, and genre as key-value pairs. Print out the dictionary.and do atleast 5 dictionary methods on it.

# In[20]:


Favbook = {'Author':'Robert T Kiyosaki','Book':'RICH DAD POOR DAD','Publication year':2000,'genre':'Parables'} #1 method
print(Favbook)


# In[22]:


Favbook.items()


# In[25]:


Favbook.update({'Best seller':'20years'})
print(Favbook)


# In[26]:


Favbook.popitem()


# In[27]:


Favbook.keys()


# In[28]:


Favbook.values()


# In[ ]:





# **Task 2: Dictionary Lookup**
# Write a Python program that simulates a simple dictionary for translating `English words to Spanish`. Define a dictionary containing a few English words as `keys` and their corresponding Spanish translations as `values`. Allow `users to enter` an English word, and then display its Spanish translation `if it exists` in the dictionary.(use google for English to Spanish translator)

# In[29]:


EtS = {'Dinner':'Cena','minister':'ministra','Teacher':'Maestro','Data analyst':'Analista de datos'}


# In[32]:


EtS.keys()


# In[34]:


EtS.values()


# In[35]:


EtS['Data analyst']


# **Task 3: Student Grades**
# Create a Python program that stores the `grades of five students` in a dictionary. Allow users to input the names of the students and their respective grades. Calculate and display the `average grade` of the students.

# In[36]:


G = int(input('Enter the G: '))
G1 = int(input('Enter the G1: '))
G2 = int(input('Enter the G2: '))
G3 = int(input('Enter the G3: '))
G4 = int(input('Enter the G4: '))
student = input('Enter the name of S: ')
student1 = input('Enter the name of S1: ')
student2 = input('Enter the name of S2: ')
student3 = input('Enter the name of S3: ')
student4 = input('Enter the name of S4: ')



# In[41]:


Sum of Grade = (G+G1+G2+G3+G4)/5
no of students = (student+student1+student2+student3+student4)
avg = Sum of Grade/no of students


# In[ ]:




