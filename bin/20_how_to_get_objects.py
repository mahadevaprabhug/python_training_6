"""
How to get objects
- Using class

Here,
1. CLASS OBJECT
2. INSTANCE OBJECTS
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

print("DATA inside each objects:")
print("-"*20)
# --------------

print("DATA present inside class object 'Employee':", Employee)
print("DATA present inside instance object 'e1':", e1)
print("DATA present inside instance object 'e2':", e2)

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


# About 'object' class
# ---------
# - 'object' class is master class
# - this has basic methods like creating the object, initializing the object etc
# - When we create new class, automatically whatever there in 'object' class
#   will come to our class
# - This linking is called INHERITANCE, Then all classes
#   are by default linked/INHERITED from 'object' class
################################
