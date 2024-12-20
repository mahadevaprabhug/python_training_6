"""
Inheritance:
1. Multilevel Inheritance
2. Multiple Inheritance
"""

print("1. Multilevel Inheritance")
print("-"*20)
# --------------


# Assume this class is already present
class Salary:
    def add_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

# New requirement: Add below functionality to salary class
# 1. add method to store tax
# 2. add method to get tax
# 3. Change the functionality for get_salary to return (salary-tax)
# 4. provide method to access old_tax_scheme_salary

# Salary -> superclass/parentclass
# Employee -> subclass/childclass
class Employee(Salary):
    # 1. add method to store tax
    def add_tax(self, tax):
        self.tax = tax

    # 2. add method to get tax
    def get_tax(self):
        return self.tax

    # 3. Change the functionality for get_salary to return (salary-tax)
    def get_salary(self):
        return (self.salary - self.tax)

    # 4. provide method to access old_tax_scheme_salary
    def get_old_tax_scheme_salary(self):
        # 1-WAY
        old_salary = super().get_salary()
        # 2-WAY
        old_salary = Salary.get_salary(self)
        return old_salary


print("#"*40, end="\n\n")
################################

print("Creating Object and accessing methods")
print("-"*20)
# --------------

e1 = Employee()
e1.add_salary(20000)
e1.add_tax(2000)

print("Salary:", e1.get_salary())
print("Tax:", e1.get_tax())
print("Old Scheme Salary:", e1.get_old_tax_scheme_salary())

print("#"*40, end="\n\n")
################################

print("Method Resolution Order")
print("-"*20)
# --------------

print(Employee.mro())

# [<class '__main__.Employee'>, <class '__main__.Salary'>, <class 'object'>]
# If we access any method then it will check for method in above order

print("#"*40, end="\n\n")
################################

print("Multiple Inheritance: Method Resolution Order")
print("-"*20)
# --------------


class A:
    pass


class B:
    pass


class C(A,B):
    pass


print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# I we create object 'C' and access any method, then it will look for
# that method in above order

print("#"*40, end="\n\n")
################################

