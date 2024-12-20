"""
Functions With Arguments

Here,
Case-2: How to pass values to variables present inside the function

3 ways to pass values
1-way: We can pass only values OR arg_name=value format
    - Also called POSITIONAL OR KEYWORD ARGUMENTS
2-way: We can pass only values
    - Also called POSITIONAL ONLY Arguments
3-way: We can pass only arg_name=value format
    - Also called KEYWORD ARGUMENTS
"""
print("""
1-way: We can pass only values OR arg_name=value format
    - Also called POSITIONAL OR KEYWORD ARGUMENTS
""")
print("-"*20)
# --------------


def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# POSITIONAL ARGUMENT: We can pass only values
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# KEYWORD ARGUMENT: We can pass values in arg_name=value format
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)


print("#"*40, end="\n\n")
################################

print("""
2-way: We can pass only values
    - Also called POSITIONAL ONLY Arguments
""")
print("-"*20)
# --------------

# / -> It is just syntax to tell it POSITIONAL ONLY ARGUMENTS
# / -> is not counted as argument
# / -> we are not passing any values to /


def employee(name, company, /):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# POSITIONAL ARGUMENT: We can pass only values
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# BELOW CODE WILL NOT WORK

# KEYWORD ARGUMENT: We can pass values in arg_name=value format
# received_value = employee(name="emp-1", company="comp-1")
# print("received_value:", received_value)


print("#"*40, end="\n\n")
################################


print("""
3-way: We can pass only arg_name=value format
    - Also called KEYWORD ARGUMENTS
""")
print("-"*20)
# --------------

# * -> It is just syntax to tell it KEYWORD ONLY ARGUMENTS
# * -> is not counted as argument
# * -> we are not passing any values to *


def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# WE CAN'T CALL LIKE THIS
# POSITIONAL ARGUMENT: We can pass only values
# received_value = employee("emp-1", "comp-1")
# print("received_value:", received_value)

# KEYWORD ARGUMENT: We can pass values in arg_name=value format
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)


print("#"*40, end="\n\n")
################################

