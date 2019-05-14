
# coding: utf-8

# In[ ]:


from crossref.restful import Works
import pandas as pd


# In[ ]:


File = input("Enter file type: ")
if File == 'xlsx':
    FileLoc = input("Enter complete file path: ")
    df = pd.read_excel(FileLoc)
else:
    print("Not valid")


# In[ ]:

#Works is a function in Crossref that allows access to a variety of metadata for publications
pub = Works()


# In[ ]:


for index, row in df.iterrows():
    #.doi() is a function under Works() that delivers information
    #based on the publications' DOI.
    x = pub.doi(row['DOI']) #finds DOI info for each cell of the DOI column
    if x is None: #handles cells that do not have DOIs or incorrect DOIs
        print(index, '')
    else:
        a = x["created"]["date-parts"]
        b = str(a).strip("[[]]")
        print (index, b, end ='\n') 


# In[ ]:


for index, row in df.iterrows():
    x = pub.doi(row['DOI']) #finds DOI info for each cell of the DOI column
    if x is None: #handles cells that do not have DOIs or incorrect DOIs
        print(index, '')
    else:
         print (index, x['publisher'] , end ='\n')

