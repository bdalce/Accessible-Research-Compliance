
# coding: utf-8

# In[1]:


from crossref.restful import Works


# In[2]:


import pandas as pd


# In[3]:


FileLoc = "C:\\Users\\briana.dalce\\Documents\\all_publications_sample_new.xlsx"


# In[4]:


data = pd.read_excel(FileLoc, usecols = 3) #using only columns 0-3


# In[5]:


data = data.dropna() #drops the null values within the first four columns of the spreadsheet


# In[6]:


pub = Works()
  
   


# In[7]:


for i,j in data.iterrows():
    x = pub.doi(j['DOI']) #finds DOI info for each cell of the DOI column
    y = j['Record Number']
    if x is None: #handles cells that do not have DOIs or incorrect DOIs
        print('')
    else:
        print(y, x['created'], end = '\n') #prints only the timestamp for cells stored in x 


