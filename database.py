from constants import Constants
import os

csvfile = Constants.csv_path + Constants.file_name
schema_name = Constants.schema_name
table_name = Constants.table_name

command = 'head -n100 ' + csvfile + ' | '
command += "tr [:upper:] [:lower:] | tr ' ' '_' | sed 's/#/num/' | "
command += 'csvsql -i postgresql --db-schema ' + schema_name + ' --tables ' + table_name

os.system(command)