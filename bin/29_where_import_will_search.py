"""
List of directories where import will search for mymodule.py/mypackage
"""

print("List of directories where import will search for mymodule.py/mypackage")
print("-"*20)
# --------------

import sys
print(sys.path)

# 'import' will refer sys.path list to check modules/packages.

print("#"*40, end="\n\n")
################################


print("Adding new location")
print("-"*20)
# --------------

import sys
sys.path.append(r"D:\mylib1")
sys.path.append(r"D:\mylib2")
print(sys.path)
# import statement will come here

print("#"*40, end="\n\n")
################################

