"""
In this program, we are accessing
variables
functions
classes present in mymodule.py library
"""

print("1-WAY: import")
print("-"*20)
# --------------

import mymodule

print("Course:", mymodule.course)

add_result = mymodule.add(10, 20)
print("add_result:", add_result)

e1 = mymodule.Employee("emp-1")
print("Employee Name:", e1.get_employee_name())

print("#"*40, end="\n\n")
################################

print("2-WAY: from-import")
print("-"*20)
# --------------

from mymodule import course, add, Employee

print("Course:", course)

add_result = add(10, 20)
print("add_result:", add_result)

e1 = Employee("emp-1")
print("Employee Name:", e1.get_employee_name())

print("#"*40, end="\n\n")
################################

print("1-WAY with short name: import")
print("-"*20)
# --------------

import mymodule as mm

print("Course:", mm.course)

add_result = mm.add(10, 20)
print("add_result:", add_result)

e1 = mm.Employee("emp-1")
print("Employee Name:", e1.get_employee_name())

print("#"*40, end="\n\n")
################################

print("2-WAY with shortname: from-import")
print("-"*20)
# --------------

from mymodule import course as c, add as a, Employee as E

print("Course:", c)

add_result = a(10, 20)
print("add_result:", add_result)

e1 = E("emp-1")
print("Employee Name:", e1.get_employee_name())

print("#"*40, end="\n\n")
################################
