"""
How to store data inside object

Here,
1. CLASS VARIABLES
2. INSTANCE VARIABLES
"""

print("Writing Class")
print("-"*20)
# --------------


class Employee:
    pass

# pass: it is dummy keyword, it does nothing
# pass: Use this to keep any block empty
# Above class empty class, but it is valid class.
#   valid class means, we can create object using this empty class
print("#"*40, end="\n\n")
################################

print("Creating Objects")
print("-"*20)
# --------------

e1 = Employee()
e2 = Employee()

# Total 3 objects
# CLASS OBJECT: 'Employee', In the name of class one object is getting created
#           automatically
# INSTANCE OBJECT: 'e1' & 'e2', which we created

print("#"*40, end="\n\n")
################################

print("Store the data in all 3 objects")
print("-"*20)
# --------------

Employee.company_name = "XYZ Company"
# Inside object 'Employee', It will create new variable 'company_name' and store the value
e1.name = "emp-1"
# Inside object 'e1', It will create new variable 'name' and store the value
e2.name = "emp-2"
# Inside object 'e2', It will create new variable 'name' and store the value

print("#"*40, end="\n\n")
################################

print("DATA inside each objects:")
print("-"*20)
# --------------

print("DATA present inside class object 'Employee':", Employee.company_name)
print("DATA present inside instance object 'e1':", e1.name)
print("DATA present inside instance object 'e2':", e2.name)

print("#"*40, end="\n\n")
################################

print("METHODS/VARIABLES inside each objects:")
print("-"*20)
# --------------

print("METHODS/VARIABLES present inside class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
################################

# CLASS OBJECT 'Employee' is common space for all INSTANCE OBJECTS
# So, we can use class object to  keep the data which is common for all instance object
