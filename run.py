import os

os.system('python3 download.py')
os.system('python3 database.py > create_command.txt')
os.system('python3 database_psycopg2.py')
