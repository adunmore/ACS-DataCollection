# ACS-DataCollection
10718 Fall20 Assignment 1 - ACS data collection

To run the entire pipeline, execute the file run.py.

-- The following description has been added after the Sept 18, 23:59 submission deadline --
The file run.py runs three separate python files. 
First, it runs download.py, which downloads the data using CensusData (https://pypi.org/project/CensusData/) library and dumps it to a csv file. The file constants.py contains all the constants in one place, so that they can be easily changed to run the entire pipeline for downloading different variables (or for a different state / different year / etc).
Second, it runs database.py to generate the 'create table' command, and dumps it to create_command.txt. 
Third, it runs database_psycopg2.py to run the psql commands of creating the schema, table and copying the data from the csv into the table. This file uses dbcreds.py for the database credentials (which is not in this repository due to privacy concerns).
