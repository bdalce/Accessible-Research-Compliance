
# coding: utf-8

# In[ ]:


import pandas as pd
import urllib.request
import urllib.error
import re
from collections import Counter
from Bio import Entrez


# In[ ]:


Type = input("xlsx or csv: ")

if Type == 'xlsx':
    File = input("Enter complete file path: ") 
    df = pd.read_excel(File)
elif Type == 'csv':
    File = input("Enter complete file path: ") 
    df = pd.read_csv(File)
else:
    print("Not valid")
 


# In[ ]:


Entrez.email = 'bdalce@terpmail.umd.edu'


# In[ ]:


for index, row in df.iterrows(): #Checks each row in the DOI columnn
    x = row['DOI']
    y = str(x)
    #url link for DOIs that are available PubMedCentral (JSON format)
    url = 'https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids='+str(x)+'&format=json&versions=yes&tool=biopython&email=bdalce@terpmail.umd.edu'
    a = urllib.request.urlopen(url).read().decode('utf-8')
    #link for DOIs under embargo or unavailable in PubMedCentral (JSON format)
    url = 'https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids='+str(x)+'&format=json&versions=no&tool=biopython&email=bdalce@terpmail.umd.edu'
    b = urllib.request.urlopen(url).read().decode('utf-8')
    #search through the json files for 'true' or 'false'
    finderr = re.findall('false', b)
    find = re.findall('true', a)
    #counts how many time 'true' or 'false' appears on the page
    for i in find:
        count = Counter(find)
        if count == Counter({'true': 1}):
            print(index,'YES') #prints 'YES' if true is found once
      
    for i in finderr:
        count = Counter(finderr)
        if count == Counter({'false': 1}):
            print(index, 'NO') #prints 'NO' if false is found once

         


# In[ ]:


#find = re.findall('true',a)
#find2 = re.findall('error',a)
#find3 = re.findall('release-date',a)
#for i in find:
    #count = Counter(find)
    #if count == Counter({'true': 1}):
        #print(index,'YES')  
#for i in find2:
    #count = Counter(find2)
    #if count == Counter({'error': 1}):
        #print(index,'NO') 
#for i in find2:
    #count = Counter(find3)
    #if count == Counter({'error': 1}):
        #print(index,'NO')     
    #else:
        #print(index, 'NO (not released yet)'

