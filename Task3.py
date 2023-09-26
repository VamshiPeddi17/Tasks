#!/usr/bin/env python
# coding: utf-8

# Assignment Tasks on String Escape Characters, Indexing, and Slicing:
# 
# **String Escape Characters:**
# 
# Task 1:
# 1. Create a string containing a sentence that includes both single and double quotes.
# 2. Use escape characters to include quotes within the string.
# 3. Print the modified string.
# 
# Task 2:
# 1. Declare a string with a backslash \ character in it.
# 2. Demonstrate the use of the escape character to print the backslash itself.
# 3. Print the resulting string.
# 
# Task 3:
# 1. Construct a string containing newline and tab escape sequences.
# 2. Print the string to display the formatted output.
# 
# **Indexing and Slicing:**
# 
# Task 4:
# 1.  sentence = "I want to become Data Scientist".
# 2. Access and print the `first character` of the string using indexing.
# 3. Access and print the `last character` of the string using negative indexing.
# 
# Task 5:
# 1. What are `possible ways` yo extract `Scientist`(use forward and reverse)
# 2. Use slicing to extract and print the `first word` from the string.
# 3. Use slicing to extract and print the `last three` characters of the string.
# 
# Task 6:
# 1. name = "Innomatics Reserach Labs"
# 2. Apply slicing to extract a substring that includes the `second to fifth` characters.
# 3. `Print` the extracted substring.
# 
# Task 7:
# 1. string = "Python@1234"
# 2. Use slicing to extract every second character from the string.
# 3. Print the resulting sliced string.
# 
# Task 8:
# 1.  print last five letters.
# 2. Utilize slicing to reverse the word order in the string.
# 3. Print the string with the words in the reversed order.
# 
# Task 9:
# 1. a = "123123123"
# 2. Apply slicing to extract only the numeric characters at odd positions.
# 3. Print the sliced result.
# 
# Remember to include explanations or comments for each task's code to ensure clarity. Additionally, encourage students to experiment further with different escape characters and slicing techniques beyond the provided tasks to deepen their understanding.

# # Task1

# In[1]:


V = "Game of thrones is the best 'DRAGON' series"


# In[2]:


print(V)


# In[3]:


A = "Iam learning data science from \"Innomatics\" Institute"


# In[4]:


print(A)


# # Task2

# In[9]:


M = "please find the slash at the end \\"


# In[10]:


print(M)


# # Task3

# In[15]:


S = "Hyderabad\tis\tfamous\tfor\tcharminar\nand\tdum\tbiryani"


# In[16]:


print(S)


# # Task4

# In[17]:


H = "I want to become Data Scientist"


# In[18]:


H[0]


# In[26]:


H[-1]


# # Task5

# In[20]:


H = "I want to become Data Scientist"


# In[21]:


len(H)


# In[23]:


H[22:31:1]


# In[25]:


H[-1:-10:-1]


# In[29]:


H[0:1]


# In[32]:


H[-3::]


# # Task6

# In[33]:


name = "Innomatics Reserach Labs"


# In[34]:


name[2:5]


# # Task7

# In[35]:


string = "Python@1234"


# In[36]:


string[::2]


# # Task8

# In[38]:


string[6::]


# In[39]:


string[::-1]


# # Task9

# In[40]:


a = "123123123"


# In[42]:


a[::2]

