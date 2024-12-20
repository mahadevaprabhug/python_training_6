"""
2 Cases
Case-1: How to access values outside the function
Case-2: How to pass values to variables present inside the function

Here,
Case-1: How to access values outside the function
"""
print("Function returning single value")
print("-"*20)
# --------------

# 2 Steps to return values
# Step-1: Inside function, use return statement to specify values
# Step-2: Assign function call to variables, so that return value will be stored

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1: Inside function, use return statement to specify values
    return name

# Step-2: Assign function call to variables, so that return value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
################################

print("Function returning multiple values: Tuple")
print("-"*20)
# --------------

# 2 Steps to return values
# Step-1: Inside function, use return statement to specify values
# Step-2: Assign function call to variables, so that return value will be stored

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1: Inside function, use return statement to specify values
    return name, company # default is tuple, it will keep in tuple and return

# Step-2: Assign function call to variables, so that return value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
################################

print("Function returning multiple values: List")
print("-"*20)
# --------------

# 2 Steps to return values
# Step-1: Inside function, use return statement to specify values
# Step-2: Assign function call to variables, so that return value will be stored

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1: Inside function, use return statement to specify values
    return [name, company]

# Step-2: Assign function call to variables, so that return value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
################################

print("Function returning multiple values: Dictionary")
print("-"*20)
# --------------

# 2 Steps to return values
# Step-1: Inside function, use return statement to specify values
# Step-2: Assign function call to variables, so that return value will be stored

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1: Inside function, use return statement to specify values
    return {"name": name, "company": company}

# Step-2: Assign function call to variables, so that return value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
################################
