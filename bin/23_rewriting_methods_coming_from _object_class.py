"""
We can rewrite methods using same name which is coming object class
This rewriting is called OVERRIDING
POLYMORPHISM: We can reuse the name as well. Means we can rewrite method using same name

__new__ is CONSTRUCTOR

We are planning to rewrite/override __init__ which is coming from object
- This we are rewriting to initializing our object with some value

Also, In this class we are adding one more new thing is,
directly declaring variables inside the class
"""

print("Writing Class")
print("-"*20)
# --------------


class Employee:
    """
    Requirement:
    # 1. declare variable inside class to store company name
    # 2. add method to get company name
    # 3. OVERRIDE __init__ to store employee name
    # 4. add method to get employee name
    """

    # 1. declare variable inside class to store company name
    company_name = "XYZ Company"

    # 2. add method to get company name
    @classmethod
    def get_company_name(cls):
        return cls.company_name

    # 3. OVERRIDE __init__ to store employee name
    def __init__(self, employee_name):
        self.employee_name = employee_name

    # 4. add method to get employee name
    def get_employee_name(self):
        return self.employee_name

print("#"*40, end="\n\n")
################################


print("Creating Objects")
print("-"*20)
# --------------

e1 = Employee("emp-1") # it calls __init__
e2 = Employee("emp-2")

# Total 3 objects
# CLASS OBJECT: 'Employee', In the name of class one object is getting created
#           automatically
# INSTANCE OBJECT: 'e1' & 'e2', which we created

print("#"*40, end="\n\n")
################################

print("DATA inside each objects:")
print("-"*20)
# --------------

print("DATA present inside class object 'Employee':", Employee.get_company_name())
print("DATA present inside instance object 'e1':", e1.get_employee_name())
print("DATA present inside instance object 'e2':", e2.get_employee_name())

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

