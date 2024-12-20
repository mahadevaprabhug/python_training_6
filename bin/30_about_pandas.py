"""
About Pandas:
- It is a library
- It has many functions and classes in it
- Few function names are read_csv, read_excel etc.
- Few class names are DataFrame, Series etc.

About 'DataFrame' class
- it is MAIN class
- it has methods related to tabular data
"""

print("Inside pandas library")
print("-"*20)
# --------------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
################################

print("Inside DataFrame class")
print("-"*20)
# --------------

print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
################################


print("DataFrame Example-1")
print("-"*20)
# --------------

my_df = pd.DataFrame([[10, 20, 30], [40, 50, 60]])
print(my_df)

print("#"*40, end="\n\n")
################################

print("DataFrame Example-2")
print("-"*20)
# --------------

my_df = pd.DataFrame([[10, 20, 30], [40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df)

print("#"*40, end="\n\n")
################################
