'''
Utility file to examine first 10 rows of a csv
'''
from constants import Constants
import csv

filename = Constants.csv_path + Constants.file_name

content = []
with open(filename) as csvfile:
	reader_obj = csv.reader(csvfile)
	for row in reader_obj:
		content.append(row)
print(content[:10])