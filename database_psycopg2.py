from dbcreds import Credentials
from constants import Constants
import psycopg2

con = psycopg2.connect(database=Credentials.database, user=Credentials.user, password=Credentials.password, host=Credentials.host)

cmd_list = []
cmd_list.append('SET ROLE ' + Credentials.user + ';')
cmd_list.append('CREATE SCHEMA IF NOT EXISTS ' + Constants.schema_name + ';')
cmd_list.append('DROP TABLE IF EXISTS ' + Constants.schema_name + '.' + Constants.table_name + ';')

with open('create_command.txt') as f:
	cmd_list.append(f.read())

cur = con.cursor()
for cmd in cmd_list:
	cur.execute(cmd)

with open(Constants.csv_path + Constants.file_name) as f:
    sql_command = 'COPY ' + Constants.schema_name + '.' + Constants.table_name + ' from STDIN with CSV HEADER'
    cur.copy_expert(sql_command, f) #, Constants.schema_name + '.' + Constants.table_name, columns=columns, sep=",")
# cur.copy_from('\COPY ' + Constants.schema_name + '.' + Constants.table_name + ' from ' + Constants.csv_path + Constants.file_name + ' WITH CSV HEADER;'

con.commit()
con.close()
