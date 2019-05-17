
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


Type = input("Enter file type: ")

if Type == 'xlsx':
    File = input("Enter complete file path: ") 
    df = pd.read_excel(File)
else:
    print("Not valid")
 


# In[3]:


df = df.dropna(subset = ['Accession'])


# In[7]:


total_count = 0 #count for total number of unique accession numbers 
proj_count = 0 #count for total number of unique accession numbers with a dataset

unique_num_list = [] #list for all unique accession numbers
proj_list = [] #list of accession numbers that have dataset

#goes through each cell in the 'Accession' and 'delta' column
for index, row in df.iterrows(): 
    x = row['Accession']
    y = row['delta']
#if an accession number is not in the list, it will be added,
#and the total number of accession numbers increases.

#if the accession number is already in the list, it does not
#get added. The list and total count remain the same.
    if x not in unique_num_list:
        unique_num_list.append(x)
        total_count += 1
#if an accession number is not in the list, it will be added,
#and the number  of accession numbers increases.

#if the accession number is already in the list, it does not
#get added. The list and total count remain the same.
    if x not in proj_list and y == 0:
        proj_list.append(x)
        proj_count += 1
#dividing the accession number with datasets with the overall total 
#to determine the % of all the ARS 2017 accession numbers have 
#at least one associated dataset in Ag Data Commons.
proj_percent = (proj_count/total_count) * 100
print('{0:.2f}%'.format(proj_percent))

