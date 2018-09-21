
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import urllib.request
import http.client
import re
from collections import Counter


# In[3]:


File = "C:\\Users\\briana.dalce\\Documents\\all_publications_sample_new.xlsx"


# In[4]:


df = pd.read_excel(File, usecols = 'A,F:F') #shows only two columns (Record Number and AGID)


# In[5]:


df = df.dropna() #drops the rows that do not have an AGID


# In[6]:


counter = Counter() #calls the Counter functions that tracks how often a string is used
total = 0 #total count initialized to 0 

for index, row in df.iterrows(): #Checks each row in the AGID columnn
    x = row['AGID']
    #adds the AGID to the search query
    y = 'https://api.nal.usda.gov/pubag/rest/search/?query=agid:'+str(x)+'&api_key=B4MvzyvVMUlBvKgTcym9xcD29zIwXgD0B3rzPdQd'
    try:
        z = urllib.request.urlopen(y) #opens the webpage
        text = z.read().decode('utf-8') # reads the contents of each webpage                           
        find = re.findall('Full Text', text) #finds the phrase 'Full Text' on the webpage
        for i in find: #checks for each instance of 'Full Text'
            counter = Counter(find) #counts how many times 'Full Text' appears in a row 
            if counter == Counter({'Full Text': 1}):
                total += 1  #counts how many rows have the phrase 'Full Text'
    except http.client.HTTPException as e: #handles the BadStatusLine error
        continue
print("Full Text publications in PubAg: " + str(total))

