"""
Generator:
- It is function only
- It will be able to
    generate object on the fly
    or
    generate object whenever we want
"""

print("Without using generators")
print("-"*20)
# --------------


def my_square_function(my_list):
    result = []
    for i in my_list:
        result.append(i*i)
    return result


L = [10, 20, 30, 40, 50]
squared_list = my_square_function(L)

for i in squared_list:
    print("Square Value:", i)

# In above code, requirement is to print one squared value at a time
# Even though we need one squared value at a time, 1st we are keeping
# all the squared values and we are using one by one

# Requirement: are there way to get values/object whenever we need
# so that we can save memory which all squared values are using

print("#"*40, end="\n\n")
################################

print("Using generators")
print("-"*20)
# --------------


def my_square_generator_function(my_list):
    for i in my_list:
        yield i * i


L = [10, 20, 30, 40, 50]
generator_object = my_square_generator_function(L)

print("generator_object:", generator_object)

for i in generator_object:
    print("Squared Value:", i)


print("#"*40, end="\n\n")
################################
