
# coding: utf-8

#Code is similar to Sheet Join.py, but this script allows users to input any spreadsheet, column, or join method. 
# In[ ]:


import pandas


# In[ ]:

file_one = input("Enter first file path: ")
file_two = input("Enter second file path: ")


# In[ ]:


file = pandas.read_excel(file_one)
file1 = pandas.read_excel(file_two)


# In[ ]:


merge_on = input("Enter column name: ")
merge_how = input("Enter (outer/inner/left/right): ")


# In[ ]:


merge = file.merge(file1, on = str(merge_on), how = str(merge_how))
merge


# In[ ]:


new_file = input("Enter new file path: ")


# In[ ]:


merge.to_excel(new_file)

