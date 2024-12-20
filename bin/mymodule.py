"""
In this file, Keep all
- Variables
- Functions
- Classes
which we are planning to use in other programs

This file is also called as PYTHON-MODULE or PYTHON-LIBRARY
"""

course = "python"


def add(a, b):
    return a + b


class Employee:
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def get_employee_name(self):
        return self.employee_name
