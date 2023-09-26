#!/usr/bin/env python
# coding: utf-8

# 1. Ask user to  enter a  website name and check whether it is valid or not(True/False)
# 
# 
# 2. name = "Innomatics", course = "Data Science"
#    write python code in `different ways` to show output as :
#    `"Hello World I am learning Data Science in Innomatics"`
#    
#    
# 3. Replace `Science` with `Analysis` in the above output.
# 
# 
# 4. `string = '     Hello World I am learning Python in Innomatics   '`
#     a. How many characters are there in the string.
#     b. Slice only 'Python' from above string
#     c. Remove white spaces on both sides then find no.of characters in the string.
#     d. Convert the string in Upper case
#     
#     
# 5. What is the index number of 'World' in above string.
# 
# 
# 6. Split the string with respect to `whitespace`.after that `store` that splitted into a variable and find the `data type`of that variable.
# 
# 
# 7. How many times 'a' is `repeated` in above string.
# 
# 8. 

# In[68]:


website = input('Enter the name of wesite: ')
(website.startswith('https')) and (website.endswith(".com/"))


# In[69]:


name = "Innomatics"
course = "Data Science"


# In[74]:


name = input('Enter the name:')
course = input('Enter the course name: ')


# In[76]:


print("Hello World I am learning " + course+ ' in ' + name)


# In[78]:


print("Hello World I am learning {} in {}".format(course,name))


# In[79]:


print(f"Hello World I am learning {course} in {name}")


# In[80]:


Str = "Hello World I am learning Data science in Innomatics"


# In[81]:


Str.replace('science','Analysis')


# In[85]:


string = '     Hello World I am learning Python in Innomatics   '


# In[86]:


len(string)


# In[88]:


string[31:37]


# In[89]:


string.strip()


# In[90]:


string.upper()


# In[92]:


string.index('World')


# In[95]:


S = string.split('     ')


# In[96]:


S


# In[97]:


type(S)


# In[99]:


string.count('a')

