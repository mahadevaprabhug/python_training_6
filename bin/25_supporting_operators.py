"""
Supporting operators

In python for all the operators like +, - etc
there is special name given,
Example: for +, name given is __add__

If we want support for any operator then
we need to write method using the name given to that operator
"""

print("Supporting + Operator")
print("-"*20)
# --------------


class Employee:
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def __add__(self, other): # self=e1, other=e2
        concat_result = self.employee_name + other.employee_name
        return concat_result


e1 = Employee("emp-1")
e2 = Employee("emp-2")

# Requirement: if we add e1 + e2 then it should concat both names
add_result = e1 + e2 # Internally + calls e1.__add__(e2)
print("add_result:", add_result)

print("#"*40, end="\n\n")
################################
