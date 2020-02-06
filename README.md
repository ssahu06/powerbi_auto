# powerbi_auto
PowerBI Automation script to update connection string using Python

## Pre Requisites :-
 1. PowerBI desktop installed with singed in using any email account.
 2. Finance Visualisation and finance database in local.
 3. Python installed with required packages used in script.
  
## How to Run :
 1. Clone the repository into your Local and Update the path for pbix and connection at line number 18 & 58.
 2. Run the powerbi_auto.py through command prompt (C:\path>powerbi_auto.py) or any python IDE.
 
## Import Finance Data :
 1. Clone the repository and open Vector/Ingres CLI.
 2. cd "path to Finance folder from repo"
 3. createdb financedb
 3. sql financedb < copy.in
