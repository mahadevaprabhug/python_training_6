"""
- Strings:
    -- We have option to store text data like name, email-id, word, sentence etc
    -- Automatically index number will be assigned to each character
"""

print("Strings PART-1")
print("How to store values")
print("-"*20)
# --------------

a = 'PERSON'
b = "PERSON'S"
c = 'PERSON\'S'
d = """PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCHES)"""
e = '''PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCHES)'''
f = """a"""

# In all the above cases, it will create object of builtin class 'str'
# and store the values

print(a, b, c, d, e, f, sep="\n")

print("#"*40, end="\n\n")
################################

print("Strings PART-2")
print("How to store values")
print("-"*20)
# --------------

my_file_path_1 = "C:\newfolder\test.py"
# By default: \n\t etc are having special meaning, \n will get replace witn newline
print("my_file_path_1 in non-raw format=", my_file_path_1, sep="\n", end="\n\n")


my_file_path_2 = r"C:\newfolder\test.py"
# r -> raw string -> No special meaning for \n\t etc
print("my_file_path_2 in raw format=", my_file_path_2, sep="\n", end="\n\n")

my_file_path_3 = repr(my_file_path_1) # convert to raw format
print("my_file_path_3: convert to raw format=", my_file_path_3, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
################################

print("Strings PART-3")
print("How to store values")
print("-"*20)
# --------------

x = 100
y = 200
z = x + y

my_string = f"add of {x} and {y} is {z}"
# f - > format
# f -> it will replace {variable name} with value
print("my_string:", my_string)

print("#"*40, end="\n\n")
################################


print("Strings PART-4")
print("Indexes: We can access each character using index number")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer: Example-1 in 5_strings.xlsx

print("3rd character using +ve index number:", my_string[2])
print("3rd character using -ve index number:", my_string[-6])

# print("100th character using +ve index number:", my_string[100]) # ERROR

print("#"*40, end="\n\n")
################################

print("Strings PART-5")
print("Slicing: We can get sub string")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")


print("Substring from index 1 to 6 using +ve index number:", my_string[1:6])
print("Substring from index 1 to 6 using -ve index number:", my_string[-7:-2], end="\n\n")
# always in slicing character at last index will not come
# Here, char at index-6 will not come
# If we want index-6 also then end index we need provide one extra i.e 7

print("Substring from index 1 to END using +ve index number:", my_string[1:])
print("Substring from index 1 to END using -ve index number:", my_string[-7:], end="\n\n")

print("Substring from BEGINNING to 6 using +ve index number:", my_string[:6])
print("Substring from BEGINNING to 6 using -ve index number:", my_string[:-2], end="\n\n")


print("#"*40, end="\n\n")
################################

print("Strings PART-6")
print("Step Value: We can skip characters")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer Example-2 in 5_strings.xlsx

print("Substring from index 1 to 6 using +ve index number, default step by 1:", my_string[1:6])
print("Substring from index 1 to 6 using -ve index number, default step by 1:", my_string[-7:-2], end="\n\n")
# default step=1, which means from index-1 to 6, give me every character

print("Substring from index 1 to 6 using +ve index number, step by 1:", my_string[1:6:1])
print("Substring from index 1 to 6 using -ve index number, step by 1:", my_string[-7:-2:1], end="\n\n")
# step=1, which means from index-1 to 6, give me every character

print("Substring from index 1 to 6 using +ve index number, step by 2:", my_string[1:6:2])
print("Substring from index 1 to 6 using -ve index number, step by 2:", my_string[-7:-2:2], end="\n\n")
# step=2, which means from index-1 to 6, give me every 2nd character
# by default character at start index-1 will be included
# by default character at end index-6 will be excluded

print("#"*40, end="\n\n")
################################

print("Strings PART-7")
print("-ve Step Value: We can traverse in reverse direction")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Example: 6 to 1 in reverse direction
# Mandatory Steps:
# Condition-1: start index should be 6
# Condition-2: end index should be 1
# Condition-3: step value should be present and it should be negative step value
# If we miss any condition then we will not get OUTPUT

# Refer Example-3 in 5_strings.xlsx
print("sub string from index-6 to 1 using +ve index number, step by -1:", my_string[6:1:-1])
print("sub string from index-6 to 1 using -ve index number, step by -1:", my_string[-2:-7:-1], end="\n\n")
# Character at start index 6 will be included
# Character at end index 1 will be excluded

print("#"*40, end="\n\n")
################################

print("Methods/Variables present inside 'str' class")
print("-"*20)
# --------------

print(dir(my_string))

# OR
# print(dir(str))

print("#"*40, end="\n\n")
################################

# Why __ names
# --------------
# - these are system defined names
# - these are internally called/used by some operators/functions
# - Example: + internally calls __add__
# - Example: * internally calls __mul__
# - Example: [] internally calls __getitem__
################################


print("About 'startswith()' method")
print("-"*20)
# --------------

print(help(my_string.startswith))

print("#"*40, end="\n\n")
################################

print("'startswith()' method")
print("-"*20)
# --------------

my_string = "WEL COME smf;ksads asdsad  ad sa d sadsa d sa d"
print("my_string:", my_string, end="\n\n")

startswith_result_1 = my_string.startswith("WEL")
startswith_result_2 = my_string.startswith("COM", 4)
startswith_result_3 = my_string.startswith("COM", 4, 8)

print("startswith_result_1:", startswith_result_1)
print("startswith_result_2:", startswith_result_2)
print("startswith_result_3:", startswith_result_3)

print("#"*40, end="\n\n")
################################
