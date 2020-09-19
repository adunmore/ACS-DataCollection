'''
File to hold a class with all the constants
'''

class Constants:
	acs_type = 'acs5' # 5-year ACS data
	year = 2018 # Ending year, ie 2014-2018
	state_code = '12' # Florida
	variable_list = ['B01001_001E', 'B01003_001E', 'B02001_003E', 'B08303_001E', 'B19013_001E', 'B19051_001E', 'B28001_002E', 'B25070_001E', 'B25081_001E', 'B29001_001E']

	acs_key = '8f10147e22b4c6b5fff0ff6956bee34e12a8e48b'

	csv_path = '../ACS-csvdata/'
	file_name = 'records.csv'

	schema_name = 'divyansh_acs_schema'
	table_name = 'divyansh_acs_table'