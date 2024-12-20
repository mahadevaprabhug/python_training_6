"""
Get data from database and write to files
db_data.txt
db_data.json
"""

print("Get data from database")
print("-"*20)
# --------------

import sqlite3

print("Creating database 'my_database.sqlite3'")
# my_db_connection = sqlite3.connect(r'C:\python_training\programs\my_database.sqlite3')
my_db_connection = sqlite3.connect('my_database.sqlite3')
print("Done\n")

print("Creating cursor object ")
my_db_cursor = my_db_connection.cursor()
print("Done\n")

print("Execute select query")
my_query = "SELECT * FROM MY_TABLE"
my_db_cursor.execute(my_query)
print("Done\n")

my_db_result = my_db_cursor.fetchall()
print("my_db_result:", my_db_result)

print("#"*40, end="\n\n")
################################

print("Writing to 'db_data.txt'")
print("-"*20)
# --------------

my_text_file_handle = open("db_data.txt", "w")
print("IP", "DATE", "PICS", sep="\t\t", file=my_text_file_handle)
for i,j,k in my_db_result: #i-> ip, j-> date, k-> pics
    print(i, j, k, sep="\t", file=my_text_file_handle)
my_text_file_handle.close()

print('Created "db_data.txt", Please check')

print("#"*40, end="\n\n")
################################


print("Writing to 'db_data.json'")
print("-"*20)
# --------------

my_json_file_handle = open("db_data.json", "w")

import json
json.dump(my_db_result, my_json_file_handle)

my_json_file_handle.close()

print("Created 'db_data.json' file, Please check")

print("#"*40, end="\n\n")
################################
