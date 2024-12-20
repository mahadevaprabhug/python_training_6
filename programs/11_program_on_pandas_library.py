"""
Get data from
1) database
2) db_data.json
3) log_report.txt

and produce one single report
and write to below files

pandas_report.csv
pandas_report.xlsx
pandas_report.json
pandas_report.xml
"""

print("Get data from database")
print("-"*20)
# --------------

import sqlite3
my_db_connection = sqlite3.connect('my_database.sqlite3')

import pandas as pd
my_db_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)

print(my_db_df)

print("#"*40, end="\n\n")
################################

print("Get data from json")
print("-"*20)
# --------------

my_json_df = pd.read_json("db_data.json")
print(my_json_df)

print("#"*40, end="\n\n")
################################

print("Get data from text file")
print("-"*20)
# --------------

my_text_df = pd.read_csv("log_report.txt", sep="\t")
print(my_text_df)

print("#"*40, end="\n\n")
################################

print("Merge all 3 data")
print("-"*20)
# --------------

merged_df = pd.concat([my_db_df, my_json_df, my_text_df], axis=0)
print(merged_df)

merged_df.to_csv("temp1.csv")
print("""
Created temp1.csv, please check
""")

print("#"*40, end="\n\n")
################################

print("Get column names from json data")
print("-"*20)
# --------------

print(my_json_df.columns)

print("#"*40, end="\n\n")
################################

print("For my_json_df, Providing names to column ")
print("-"*20)
# --------------
my_json_df.columns = ["IP", "DATE", "PICS"]
print(my_json_df)

print("#"*40, end="\n\n")
################################

print("my_text_df columns")
print("-"*20)
# --------------

print(my_text_df.columns)
# ['IP', 'Unnamed: 1', 'PICS']

print("#"*40, end="\n\n")
################################

print("Remove 'Unnamed: 1' column")
print("-"*20)
# --------------

my_text_df = my_text_df.drop(['Unnamed: 1'], axis=1)
print(my_text_df)

print("#"*40, end="\n\n")
################################

print("Merging all 3")
print("-"*20)
# --------------

merged_df = pd.concat([my_db_df, my_json_df, my_text_df], axis=0)
print(merged_df)

merged_df.to_csv("temp2.csv", index=False)

print("#"*40, end="\n\n")
################################

print("Finding Empty cells")
print("-"*20)
# --------------

print(merged_df.isnull())

print("#"*40, end="\n\n")
################################

print("Count Empty cells")
print("-"*20)
# --------------

print(merged_df.isnull().sum())

# 26/Apr/2000

print("#"*40, end="\n\n")
################################

print("fill empty cells with '26/Apr/2000'")
print("-"*20)
# --------------

merged_df["DATE"] = merged_df["DATE"].fillna("26/Apr/2000")
print(merged_df.isnull().sum())

print("#"*40, end="\n\n")
################################

print("Final merged_df")
print("-"*20)
# --------------

print(merged_df)

print("#"*40, end="\n\n")
################################

print('Write to files')
print("-"*20)
# --------------

# pandas_report.csv
merged_df.to_csv("pandas_report.csv", index=False)

# pandas_report.xlsx
merged_df.to_excel("pandas_report.xlsx", index=False)

# pandas_report.xml
merged_df.to_xml("pandas_report.xml")

print("""
Created below reports 

pandas_report.csv
pandas_report.xlsx
pandas_report.xml

please check""")

print("#"*40, end="\n\n")
################################

print("resting index column")
print("-"*20)
# --------------

merged_df = merged_df.reset_index(drop=True)
print(merged_df)

print("#"*40, end="\n\n")
################################

print("Write to json file")
print("-"*20)
# --------------

merged_df.to_json("pandas_report_1.json")

merged_df = merged_df.T # Rotate
merged_df.to_json("pandas_report_2.json")

print("""
Created 
pandas_report_1.json
pandas_report_2.json
please check
""")

print("#"*40, end="\n\n")
################################

