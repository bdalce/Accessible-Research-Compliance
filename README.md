# Accessible-Research-Compliance Project
The purpose of this project is to track compliance with the USDA Public Access Implementation Plan. USDA funded research from 2014 and beyond should have publically accessible publications and data. 

PubMed Script

Packages/Classes Used: pandas, biopython, urllib.request, 

Goals:
To determine if an publication is available in PubMedCentral


Methods: 
Used the ID Converter API to read the DOIs in the dataset
Searched for "true" or "false" in the JSON file using regex

PubAg Script

Packages/Classes Used: pandas, urllib.request, http.client, collections, and re 

Goal:
Determine how many publications from the sample have full text in PubAg

Methods:
 Used pandas package to read through the sample of 1000 publications on Excel, 
 Removed any publication that did not have an AGID,
 Ran each AGID through the PubAg API search query using the urllib.request and http.client classes, 
 Counted the amount times “Full Text” appears in each query, and
 Counted how many rows say Full Text



Extracting DOI Dates

Packages/Classes Used: pandas, crossref.restful 

Goals:
 To find the publication dates from the DOI and to 
 Look for publications 2014 and beyond, specifically the 2017 fiscal year 


Methods: 
Used the Crossref API to find publication info based on the DOI, 
Imported pandas package to read through the Excel sheet, and Remove publications that did not have a DOI 



