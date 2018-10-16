
# coding: utf-8

# In[1]:


from crossref.restful import Works


# In[2]:


import pandas as pd


# In[3]:

File = input("xlsx or csv: ")
if File == 'xlsx':
    FileLoc = input("Enter complete file path: ")
    data = pd.read_excel(FileLoc)
elif File == 'csv':
    FileLoc = input("Enter complete file path: ")
    data = pd.read_csv(FileLoc)
else:
    print("Not valid")


# In[4]:

data = data.dropna(subset=['DOI'])
pub = Works()

# In[5]:

for i,j in data.iterrows():
    x = pub.doi(j['DOI']) #finds DOI info for each cell of the DOI column
    if x is None: #handles cells that do not have DOIs or incorrect DOIs
        print('')
    else:
        print(i, x['created'], end = '\n') #prints only the timestamp for cells stored in x 
  
   



