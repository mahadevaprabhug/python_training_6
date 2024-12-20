"""
Tuple:
        -- To keep multiple values like list of employee names
        -- We can keep duplicate values
        -- Automatically index number will be assigned to each value
"""

print("Tuple PART-1")
print("Store Multiple Values")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", (100, 200))
# It will create object of builtin class 'tuple' and store the values
print("my_tuple:", my_tuple, end="\n\n")

print("#"*40, end="\n\n")
################################

print("Tuple PART-2")
print("Indexes are similar to strings")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", (100, 200, "Java"))
print("my_tuple:", my_tuple, end="\n\n")

print("Course Name:", my_tuple[2]) # "python"
print("2nd char in Course Name:", my_tuple[2][1], end="\n\n") # "y"

print("Inner Tuple:", my_tuple[3]) # (100, 200, "Java")
print("Course name in Inner Tuple:", my_tuple[3][2]) # "Java"
print("2nd char in Course name in Inner Tuple:", my_tuple[3][2][1]) # "a"

print("#"*40, end="\n\n")
################################

print("Tuple PART-3")
print("Methods inside tuple class")
print("-"*20)
# --------------

print(dir(my_tuple))
# OR
# print(dir(tuple))

print("#"*40, end="\n\n")
################################

print("Tuple PART-4")
print("'count' and 'index' method")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", "python", "python", (100, 200, "Java", "Java", "Java"))
print("my_tuple:", my_tuple, end="\n\n")

count_of_python = my_tuple.count("python")
index_of_python = my_tuple.index("python")
print("count_of_python:", count_of_python)
print("index_of_python:", index_of_python)


# my_tuple[-1] = (100, 200, "Java", "Java", "Java")
count_of_java = my_tuple[-1].count("Java")
index_of_java = my_tuple[-1].index("Java")
print("count_of_java:", count_of_java)
print("index_of_java:", index_of_java)

print("#"*40, end="\n\n")
################################
