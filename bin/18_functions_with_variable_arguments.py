"""
Variable Arguments
1. Variable POSITIONAL Arguments
2. Variable KEYWORD Arguments
"""

print("1. Variable POSITIONAL Arguments")
print("-"*20)
# --------------


def add(*a):
    print("Received Values In Tuple:", a)


add()
add(10)
add(10, 20, 30, 40)

print("#"*40, end="\n\n")
################################

print("2. Variable KEYWORD Arguments")
print("-"*20)
# --------------

def employee_profile(**a):
    print("Received Values In Dictionary:", a)

employee_profile()
employee_profile(name="emp-1")
employee_profile(name="emp-1", company="XYZ Company")

print("#"*40, end="\n\n")
################################

# We can combine all type of arguments in one function
# BUT
# we need to follow below order
# --------------
# 1st put all positional arguments IF ANY
#
# then
#
# put Variable positional arguments IF ANY
#
# then
#
# put all Keyword argument IF any
#
#
# then
#
# put variable keyword argument IF ANY
################################
