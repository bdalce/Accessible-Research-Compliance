
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import urllib.request
import http.client
import re
from collections import Counter


# In[3]:


Type = input("xlsx or csv: ")

if Type == 'xlsx':
    File = input("Enter complete file path: ") 
    df = pd.read_excel(File)
elif Type == 'csv':
    File = input("Enter complete file path: ") 
    df = pd.read_csv(File)
else:
    print("Not valid")
 





# In[5]:


df = df.dropna(subset = ['AGID']) #drops the rows that do not have an AGID


# In[6]:


counter = Counter() #calls the Counter functions that tracks how often a string is used
total = 0 #total count initialized to 0 
Key = input("Enter API key: ")
for index, row in df.iterrows(): #Checks each row in the AGID columnn
    x = row['AGID']
    xx = math.floor(x)
    #adds the AGID to the search query
    y = 'https://api.nal.usda.gov/pubag/rest/search/?query=agid:'+str(xx)+'&api_key='+str(Key)
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

