"""
Decorators:
- It is a function
"""

print("Without using Decorators")
print("-"*20)
# --------------


def add(a, b):
    print("Result is:")
    print(a+b)
    print("End of the result")


def sub(a, b):
    print("Result is:")
    print(a-b)
    print("End of the result")


add(10, 20)
sub(10, 20)

print("#"*40, end="\n\n")
################################

print("Using Decorators: PARTIAL IMPLEMENTATION")
print("-"*20)
# --------------


# Function written as per STEPS given in decorator design pattern
def my_decorator(my_func): # my_func=add
    def decorated_function(x, y): # x=10, y=20
        print("Result is:")
        my_func(x, y)  # sub(10,20)
        print("End of the result", end="\n\n")
    return decorated_function


def add(a, b):
    print(a+b)

inner_function_reference = my_decorator(add)
# inner_function_reference will be having reference to decorated_function
inner_function_reference(10, 20)

def sub(a, b):
    print(a-b)

inner_function_reference = my_decorator(sub)
# inner_function_reference will be having reference to decorated_function
inner_function_reference(10, 20)



print("#"*40, end="\n\n")
################################

print("Using Decorators: FINAL IMPLEMENTATION")
print("-"*20)
# --------------


# Function written as per STEPS given in decorator design pattern
def my_decorator(my_func): # my_func=add
    def decorated_function(x, y): # x=10, y=20
        print("Result is:")
        my_func(x, y)  # sub(10,20)
        print("End of the result", end="\n\n")
    return decorated_function

@my_decorator
def add(a, b):
    print(a+b)

add(10, 20)
# @my_decorator will take care executing below 2 lines
# inner_function_reference = my_decorator(add)
# inner_function_reference(10, 20)
@my_decorator
def sub(a, b):
    print(a-b)

sub(10, 20)
# @my_decorator will take care executing below 2 lines
# inner_function_reference = my_decorator(sub)
# inner_function_reference(10, 20)

print("#"*40, end="\n\n")
################################
