"""
Get data from log file
then
extract using regular expression
then
send extracted data to database
"""

"""
How to communicate with database in python?

python-program    <-Communicate Using Library->  Any databases(SQL/No-SQL)

Example:
python-program    <-Communicate Using Library(cx-oracle)->  Oracle database
python-program    <-Communicate Using Library(mysql.connector)->  Mysql database
python-program    <-Communicate Using Library(Sqlite3)->  SQLite database
"""

"""
We need one database
- We can use SQLite database
- lightweight
- SQLite database is serverless
    means like other databases, sqlite will not be having server
- SQlite will just create one database file.
"""

"""
How to create/communicate with SQLite database?
2 ways
1-way: Using SQLite database software
2-way: WITHOUT Using SQLite database software, Using
        python-library sqlite3, we can create/communicate with SQLite database
"""

print("Creating database 'my_database.sqlite3' and table 'my_table'")
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

print("Create table if not present")
my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)
print("Done\n")


print("#"*40, end="\n\n")
################################

print("Getting data from web_server.log")
print("-"*20)
# --------------

my_log_file_handle = open(r"../log/web_server.log", "rb")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content, end="\n\n")

print("#"*40, end="\n\n")
################################

print("Extract IP, DATE, PICS")
print("-"*20)
# --------------

import re

for each_line in log_file_content:
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST|PUT|PATCH|DELETE)\s/(pics/(\w+\.(gif|jpg)))?.*', each_line)

    if match_result is not None:

        ip = match_result.group(1)
        ip = ip.decode() # Convert to string

        dt = match_result.group(2)
        dt = dt.decode()

        img = match_result.group(5)
        if img is None:
            img = "No Image"
        else:
            img = img.decode()
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{dt}', '{img}')"
        print("Executing Query:", my_query)
        my_db_cursor.execute(my_query)
        print("One record inserted\n")

my_db_connection.commit()
print("All records are inserted")

print("#"*40, end="\n\n")
################################
