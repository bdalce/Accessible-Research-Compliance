
# coding: utf-8

# In[1]:


import pandas as pd
#from pandas import ExcelWriter


# In[2]:


File1 = pd.read_excel("C:\\Users\\briana.dalce\\Documents\\pub_doi_agid.xlsx")
File2 = pd.read_excel("C:\\Users\\briana.dalce\\Documents\\ars_projects_pub.xlsx")


# In[3]:


merge = File1.merge(File2, on ="PUBLICATION_ID", how = "outer")
merge


# In[4]:


#newfile = pd.ExcelWriter('pub_proj.xlsx')
merge.to_excel("C:\\Users\\briana.dalce\\Documents\\original_pub_proj.xlsx")

