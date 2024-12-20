"""
Exceptions Handling
"""

# print("Without Handling Exceptions")
# print("-"*20)
# # --------------
#
# a = 10
# b = 0
# c = a/b # Program will terminate abruptly
# print("Value of c:", c)
#
# print("#"*40, end="\n\n")
# ################################

print("Handling Exceptions Using 'try-except'")
print("-"*20)
# --------------

try:
    # Keep the code which we are planning to monitor for error
    # If some error occurs here then it will execute 'except' block
    # If no error then 'except' block will be skipped
    pass
except:
    # Here, write code to solve error occurred in try
    pass


try:
    a = 10
    b = 0
    c = a/b # Program will NOT terminate, Instead it will goto except block
    print("Value of c:", c) # This statement will never execute because control will never comeback here
except:
    print("Reached except block")
    print("Here, we will write logic to solve error occurred in try")

print("#"*40, end="\n\n")
################################

# About exception classes
# --------------
# - If we want to handle using 'try-except' then we need to have
#   exception class for that error
#
# - If we don't have  exception class for that error then we can't
#   handle using 'try-except', so program will terminate with error
#
# - We have few exception classes in builtins, for remaining
#   type of error we need to write our own exception class
#   if we want to handle using 'try-except'
#
# - 'Exception' is super class for all exception class
#
# - We can specify, class name in 'except' block
#
################################

print("Handling Exceptions Using 'try-except' with class names")
print("-"*20)
# --------------

try:
    a = 10
    b = 0
    c = a/xyz
    print("Value of c:", c)
except ZeroDivisionError: # 1-way to specify class name
    print("Reached except block")
    print("This is ZDE")
except NameError as ne: # 2-way to specify class name where we are capturing the object
    print("Reached except block")
    print("This is NE and value of ne is:", ne)
except Exception as e:
    print("Reached except block")
    print("Error occurred is:", e)

print("#"*40, end="\n\n")
################################

print("Using 'try-except-else'")
print("-"*20)
# --------------

try:
    print("Reached try block")
    my_file_handle = open("t.txt", "w")
    # my_file_handle.write("Hello")
    # my_file_handle.close()
except Exception as e:
    print("Reached except block")
    print("Here we are handling only file open() error")
else:
    print("Reached else block")
    my_file_handle.write("Hello")
    my_file_handle.close()

# 'else' block: We can say it is continuation of 'try' block
# if try success then 'else' will execute and skip 'except'
# if try failed then 'except' will execute and skip 'else'

print("#"*40, end="\n\n")
################################

print("Using 'try-except-else-finally'")
print("-"*20)
# --------------

try:
    print("Reached try block")
    my_file_handle = open("t.txt", "w")
    # my_file_handle.write("Hello")
    # my_file_handle.close()
except Exception as e:
    print("Reached except block")
    print("Here we are handling only file open() error")
else:
    print("Reached else block")
    my_file_handle.write("Hello")
finally:
    print('Reached finally')
    my_file_handle.close()

# whether try/except/else success/failed BUT finally block will
# always execute

print("#"*40, end="\n\n")
################################

print("User Defined Exception Class Example-1")
print("-"*20)
# --------------

# Mandatory Step: it should be subclass of 'Exception' class
#   OR if some classes are already subclass of 'Exception' class
#   (like builtin exception classes) then we can extend that class as well


class MyError(Exception):
    pass
# This is valid class, we can handle this error using 'try-except'

try:
    x = 10
    if x == 10:
        raise MyError
    if x > 10:
        raise MyError
    if x < 10:
        raise MyError
except MyError:
    print("It is MyError")


print("#"*40, end="\n\n")
################################

print("User Defined Exception Class Example-2")
print("-"*20)
# --------------

# Requirement: while raising exception, send some message about the error


class MyError(Exception):
    def __init__(self, msg):
        self.error_message = msg

try:
    x = 10
    if x == 10:
        raise MyError("Here value of x is 10, so raising MyError")
    if x > 10:
        raise MyError("Here value of x is gt 10, so raising MyError")
    if x < 10:
        raise MyError("Here value of x is lt 10, so raising MyError")
except MyError as me:
    print("It is MyError, Details:", me.error_message)

print("#"*40, end="\n\n")
################################
