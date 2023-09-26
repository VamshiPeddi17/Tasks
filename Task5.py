#!/usr/bin/env python
# coding: utf-8

# **Task1: Append and Modify Elements**
#     
# * Create an empty list called numbers. Append the numbers 1, 2, and 3 to the list.
# * Modify the element at index 1 to be 4.
# * Print the updated list.
# 
# **Task2: Slicing and Concatenation**
# 
# * Create a list called fruits with elements 'apple', 'banana', 'orange', 'mango', and 'kiwi'. 
# * Create a new list  by slicing fruits to include only the citrus fruits ('orange' and 'mango"). * Create a new list called tropical by slicing fruits to include only the tropical fruits ('banana" and "kiwi'). 
# * Concatenate citrus and tropical lists to create a new list called combined. Print combined.
# 
# **Task3: Counting and Removing Elements**
# 
# * Create a list called colors with repeated elements 'red', 'blue', 'red', 'green', 'red'. Print the number of occurrences of 'red' in the list. Remove all occurrences of 'red' from the list. Print the updated list.
# 
# **Task 4: List Manipulation**
# 
# * Add 'cheese' to the end of the list. Remove 'milk' from the list.
# * Create a list called groceries with initial items: 'bread', 'milk', 'eggs', 'butter'. Print the final list of groceries.
# * Insert 'yogurt' at index 1.
# 
# 

# **Task1: Append and Modify Elements**
#     
# * Create an empty list called numbers. Append the numbers 1, 2, and 3 to the list.
# * Modify the element at index 1 to be 4.
# * Print the updated list.

# In[1]:


numbers = []


# In[2]:


type(numbers)


# In[4]:


numbers.append(1)


# In[5]:


numbers.append(2)


# In[6]:


numbers.append(3)


# In[7]:


numbers[1] = 4


# In[8]:


print(numbers)


# **Task2: Slicing and Concatenation**
# 
# * Create a list called fruits with elements 'apple', 'banana', 'orange', 'mango', and 'kiwi'. 
# * Create a new list  by slicing fruits to include only the citrus fruits ('orange' and 'mango"). * Create a new list called tropical by slicing fruits to include only the tropical fruits ('banana" and "kiwi'). 
# * Concatenate citrus and tropical lists to create a new list called combined. Print combined.

# In[10]:


fruits = ['apple','banana','orange','mango','kiwi']


# In[33]:


citrus = fruits[2:4]


# In[34]:


citrus


# In[29]:


tropical = fruits[1:5:3]


# In[30]:


tropical


# In[35]:


combined = citrus+tropical


# In[36]:


combined


# **Task3: Counting and Removing Elements**
# 
# * Create a list called colors with repeated elements 'red', 'blue', 'red', 'green', 'red'. Print the number of occurrences of 'red' in the list. Remove all occurrences of 'red' from the list. Print the updated list.

# In[37]:


colors = ['red','blue','red','green','red']


# In[38]:


colors.count('red')


# In[43]:


colors.remove('red')


# In[44]:


colors


# **Task 4: List Manipulation**
# 
# * Add 'cheese' to the end of the list. Remove 'milk' from the list.
# * Create a list called groceries with initial items: 'bread', 'milk', 'eggs', 'butter'. Print the final list of groceries.
# * Insert 'yogurt' at index 1.

# In[48]:


groceries = ['bread','milk','eggs','butter']


# In[49]:


groceries.append('cheese')


# In[50]:


groceries.remove('milk')


# In[57]:


groceries.insert(1,'yogurt')


# In[58]:


print(groceries)

