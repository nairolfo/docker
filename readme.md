The code in this solution does the following:
 - Takes the input.csv file and uses a sequence matching algorithm from difflib along with a fuzzywuzzy string matching method 
	to identify if a menu row contains a brand name from the terms.csv file.
 - Populates an SQL database with input.csv, terms.csv and matches found.

The database can be created with the mrmDbCreationScript.sql script 

Processing of the input.csv file takes 96s or about 1.5 mins on my machine.

the result of the code can be viewd in output.csv file which is an export of the following statement.
SELECT menuId, ProductName, ProductDescription, term.term FROM mrm.menu as menu
	JOIN mrm.match as matched ON matched.rowId=menu.rowId    
	JOIN mrm.term as term ON matched.termId=term.termId;

The results seem satisfying at first glance but didn't have time to investigate more.

The project entry file is MRMDataTest.py and the matching business logic is in content_matching_service.py file.

Created some unit test files but didn't yet implement them.