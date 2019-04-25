Publicly Accessible Research Compliance

Goals: 

    To determine the percentage of publicly accessible ARS publications

    To automate the publication tracking process.


Scripts:
    The following scripts use information in VIVO from ARIS

  Publication Info:

    Uses Crossref to find the publisher and date of publication for a specific DOI.

  PubAg:
  
  The PubAg API allows users with an assigned API key to search through the metadata of articles to gain useful information. This API is   used in this script because users can find either citations or full text of an article by inputting the AGID. Full text under a       particular tell us that the article is publicly accessible on PubAg.

    Searches through articles with AGIDs to see if there is full text in PubAg

    Converts the AGID to a string 

    Uses regex to find the phrase "Full Text"

  PubMedCentral:
  
  The DOI converter API for PubMedCentral converts DOIs to PMIDs or PMCIDs. This API was chosen for this script because an article having a PMCID tells us it is available on PubMedCentral where full text articles are shared with the public. 
    
    Converts article DOIs to PMCIDs 

    Uses regex to find the phrases "true" and "false"

    False: not available

    True: available 

  CHORUS:

    Searches for the DOI on the CHORUS API page to see if the article is available in CHORUS

    Converts DOI to a string to match the format on the CHORUS API page 

   Public Access Journals:

    Reads the prefix of the DOI to determine if a publisher/organization is publicly accessible

    Reads the suffix of the DOI to determine if a specific journal is publicly accessible

    Uses the SpringerNature and Elsevier APIs find publicly accessible articles from those publications



