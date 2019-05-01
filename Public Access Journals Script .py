
# coding: utf-8

# In[ ]:


import pandas as pd
from crossref.restful import Works
import urllib.request
import urllib.error
import re
from collections import Counter


# In[ ]:


Type = input("Enter file type: ")
if Type == 'xlsx':
    File = input("Enter complete file path: ") 
    df = pd.read_excel(File)
else:
    print("Not valid")
 
for index, row in df.iterrows(): #Checks each row in the DOI columnn
    x = row['DOI']
    y = str(x)
  
    #DOIs of Open Access Journals 
    if "10.1371/" in y or "10.3389/" in y or "10.3390/" in y or "10.1155/" in y or "10.3201/" in y:
        print(index, 'YES')
    elif "10.4236/" in y or "10.4172/" in y or "10.9734/" in y or "10.1186/" in y or "10.1534/" in y:
        print(index, 'YES')
    elif "10.1099/" in y or "10.2489/" in y or "10.1210/" in y or "10.1590/" in y or "10.5194/" in y:
        print(index, 'YES')
    elif "10.3835/plantgenome" in y or "10.7717/peerj" in y:
        print(index, 'YES')
    elif "10.1139/" in y or "10.1101/" in y or "10.3923/" in y or "10.5539/" in y or "10.5344/" in y: 
        print(index, 'YES')
    #DOIs of articles that are available immediately or 6-12 months after the publication date
    elif "10.1073/" in y:
        print(index, 'YES (hybrid)')
    #DOIs of publishers that have both available and unavailable articles 
    elif "10.1177" in y:
        if "/1040" in y: 
            print(index, 'YES')
        else:
            print(index, 'NO')
    elif "10.1094/" in y:
        if "PHYTO" in y or "PHP" in y or "pbiomes" in y or "PDIS" in y or "MPMI" in y:
            print(index, 'YES')
        else:
            print(index, 'NO')
    elif "10.1128/" in y:
        if "genomeA" in y or "mSystems" in y  or "mSphere" in y or "mBio" in y or "CVI" in y:
            print(index, 'YES')
        else:
            print(index, 'NO') 
    elif "10.1093/" in y or "10.3495/" in y or "10.2527/" in y:
        if "gigascience" in y or "gbe" in y or "aobpla" in y or "fqsafe" in y or "database" in y or "cdn" in y:
            print(index, 'YES')
        else:
            print(index, 'NO')
    elif "10.1002/" in y or "10.1111/" in y or "10.3732/" in y :
        if "fsn3" in y or "gcbb" in y or "pbi" in y or "tpj" in y or "ajb" in y  or "rse" in y or "mbo" in y:
            print(index, 'YES')
        else:
            print(index, 'NO')
    elif "10.2134/" in y or "10.3198/" in y:
        if "ael" in y or "agronj" in y:
            print(index, 'YES')
        else:
            print(index, 'NO')
    elif "10.1038/" in y:
        if "hortres" in y or "nplants" in y or "ncomms" in y or "s" in y or "gim" in y:
            print(index, 'YES')
        else:
            print(index, 'NO')
    #DOIs of publications that are unavailable
    elif "10.1017/" in y or "10.4039/" in y or "10.1080/" in y or "10.21273/" in y or "10.2113/" in y:
        print(index, 'NO')
    elif "10.17660/" in y or "10.1079/" in y or "10.3791/" in y or "10.1637/" in y: 
        print(index, 'NO')
    elif "10.3958/" in y or "10.1039/" in y or "10.5334/" in y or "10.2460/" in y:
        print(index, 'NO')
    #DOIs associated with Elsevier
    elif "10.1016/" in y or "10.3168/" in y or "10.5232/" in y:
        try:
            url = 'https://api.elsevier.com/content/article/doi/' + str(x)
            a = urllib.request.urlopen(url).read().decode('utf-8')
            find = re.findall('<openaccessArticle>true', a)
            find2 = re.findall('<openaccessArticle>false', a)
            for i in find:
                counter = Counter(find)
                if counter == Counter({'<openaccessArticle>true': 1}):
                    print(index,'YES')
          
            for j in find2:
                counter = Counter(find2)
                if counter == Counter({'<openaccessArticle>false': 1}):
                    print(index,'NO')
        except urllib.error.HTTPError as e:
            if e.code >= 400:
                print (index, 'NO')
          
        
    #DOIs associated with SpringerNature
    elif "10.1007/" in y or "10.4996/" in y: 
        try:
            url2 = 'http://api.springernature.com/metadata/json/doi/'+ str(x) +'?api_key=94e5956dc09e116bc249d60506e4e51b'
            b = urllib.request.urlopen(url2).read().decode('utf-8')
            find3 = re.findall('"openaccess":"true"', b)
            find4 = re.findall('"openaccess":"false"', b)
            for i in find3:
                counter = Counter(find3)
                if counter == Counter({'"openaccess":"true"': 1}):
                    print(index,'YES')
          
            for j in find4:
                counter = Counter(find4)
                if counter == Counter({'"openaccess":"false"': 1}):
                    print(index,'NO')
        except urllib.error.HTTPError as e:
            if e.code >= 400:
                print (index, 'NO')
   
                
    else:
        print(index, '')





        

