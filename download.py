'''
Downloads the specified list of variables from ACS data for all block groups in a given state.

Parameters:
	acs_type : 'acs5' / 'acs3' / 'acs1' / ...
	year : year of data to download (ending year)
	state_code : state to download
	variable_list : list of variables to download
'''
from constants import Constants

import censusdata
import os

acs_type = Constants.acs_type
year = Constants.year
state_code = Constants.state_code
variable_list = Constants.variable_list

acs_key = Constants.acs_key

location_state = censusdata.censusgeo([('state', state_code), ('county', '*'), ]) 
dummy_var_list = ['B01001_001E'] # dummy variable to get list of counties
data_state = censusdata.download(acs_type, year, location_state, dummy_var_list, acs_key) 

county_verbose_list = data_state.index.values
county_list = [elem.params() for elem in county_verbose_list] # contains the tuple of state code and county

data = None
for idx, county in enumerate(county_list):
	location_county = censusdata.censusgeo([county[0], county[1], ('block group', '*')]) 
	data_county = censusdata.download(acs_type, year, location_county, variable_list, acs_key) 
	if idx == 0:
		data = data_county
	else:
		data = data.append(data_county)

path_name = Constants.csv_path
if not os.path.exists(path_name):
	os.makedirs(path_name)
file_name = Constants.file_name

data.to_csv(path_name + file_name, index_label='Block Group Identifier')