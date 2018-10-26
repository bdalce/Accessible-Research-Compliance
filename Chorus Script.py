
# coding: utf-8

# In[ ]:


import pandas as pd
import urllib.request
import re
from collections import Counter


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


a = input("Enter date (yyyy/mm/dd): ")
b = input ("Enter limit: ")
count = 0 #keeps track of how many DOIs are on the page
counter = Counter()
#add inputs into the search query 
y = urllib.request.urlopen('https://api.chorusaccess.org/v1.1/agencies/100000199/histories/'+str(a)+'?category=publicly_accessible&subcategory=yes&limit='+str(b))
z = y.read().decode('utf-8')
for index, row in df.iterrows(): 
    x = row['DOI'] #Checks each row in the DOI column
    doi_string = '"DOI":'+ '"' +str(x)+ '"' #turns DOI into a string
    find = re.findall(doi_string, z) #checks to see if the DOI string is on the page
    for i in find: 
        counter = Counter(find)  
        if counter == Counter({doi_string: 1}): #finds the string on the page
            print(index, 'YES')
            count += 1 #counts how many DOIs are on the page
print("Number of publicly accessible publications in Chorus: " + str(count))
    

