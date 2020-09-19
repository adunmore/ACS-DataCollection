'''
Test File to see if we can download without iterating over counties.
We can't.
'''
import censusdata

acs_type = 'acs5' # 5-year ACS data
year = 2018 # Ending year, ie 2014-2018
state_code = '12' # Florida
variable_list = ['B01001_002E', 'B02001_002E'] # List of variables to download

acs_key = '8f10147e22b4c6b5fff0ff6956bee34e12a8e48b'

location = censusdata.censusgeo([('state', state_code), ('block group', '*'), ]) 
data = censusdata.download(acs_type, year, location, variable_list, acs_key) 

print(data.shape)

# change to a different directory
data.to_csv('../ACS-csv/test.csv')