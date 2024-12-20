"""
How to add methods

Here,
1. CLASS METHODS
2. INSTANCE METHODS
"""

print("Writing Class")
print("-"*20)
# --------------


class Employee:
    """
    Requirement:
    # 1. add method to store company name
    # 2. add method to get company name
    # 3. add method to store employee name
    # 4. add method to get employee name
    """

    # 1. add method to store company name
    @classmethod # Decorator: It is function. It has functionality to pass class object to below method
    def store_company_name(cls, company_name):
        cls.company_name = company_name

    # 2. add method to get company name
    @classmethod
    def get_company_name(cls):
        return cls.company_name

    # 3. add method to store employee name
    def store_employee_name(self, employee_name):
        self.employee_name = employee_name

    # 4. add method to get employee name
    def get_employee_name(self):
        return self.employee_name

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

Employee.store_company_name("XYZ Company")
# Internally class object 'Employee' will be passed to 'cls'
# "XYZ Company" will be passed to company_name

e1.store_employee_name("emp-1")
# Internally instance object 'e1' will be passed to 'self'
# "emp-1" will be passed to employee_name

e2.store_employee_name("emp-2")
# Internally instance object 'e2' will be passed to 'self'
# "emp-2" will be passed to employee_name

print("#"*40, end="\n\n")
################################

# about '@classmethod'
# --------------
# - When we call any method using e1, e2 then e1/e2 will goto self
# - If we call any method using class object 'Employee' by default
#   object 'Employee' will not be PASSED.
#
# - Example-1
#   Employee.store_employee_name("emp-3") # THIS WAY IT WILL NOT WORK
#
# - Example-2
#   Employee.store_employee_name(e1, "emp-1") # THIS WILL WORK
#   Employee.store_employee_name(e2, "emp-2") # THIS WILL WORK
#
# @classmethod # Decorator: It is function.
# It has functionality to pass class object to below method
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
