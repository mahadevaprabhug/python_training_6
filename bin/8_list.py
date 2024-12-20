"""
MUTABLE
list:
        -- To keep multiple values like list of employee names
        -- We can keep duplicate values
        -- Automatically index number will be assigned to each value
"""

print("list PART-1")
print("Store Multiple Values")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", (100, 200)]
# It will create object of builtin class 'list' and store the values
print("my_list:", my_list, end="\n\n")

print("#"*40, end="\n\n")
################################

print("list PART-2")
print("Indexes are similar to strings")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", (100, 200, "Java")]
print("my_list:", my_list, end="\n\n")

print("Course Name:", my_list[2]) # "python"
print("2nd char in Course Name:", my_list[2][1], end="\n\n") # "y"

print("Inner list:", my_list[3]) # (100, 200, "Java")
print("Course name in Inner list:", my_list[3][2]) # "Java"
print("2nd char in Course name in Inner list:", my_list[3][2][1]) # "a"

print("#"*40, end="\n\n")
################################

print("list PART-3")
print("Methods inside list class")
print("-"*20)
# --------------

print(dir(my_list))
# OR
# print(dir(list))

print("#"*40, end="\n\n")
################################

print("list PART-4")
print("'count' and 'index' method")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", "python", "python", (100, 200, "Java", "Java", "Java")]
print("my_list:", my_list, end="\n\n")

count_of_python = my_list.count("python")
index_of_python = my_list.index("python")
print("count_of_python:", count_of_python)
print("index_of_python:", index_of_python)


# my_list[-1] = (100, 200, "Java", "Java", "Java")
count_of_java = my_list[-1].count("Java")
index_of_java = my_list[-1].index("Java")
print("count_of_java:", count_of_java)
print("index_of_java:", index_of_java)

print("#"*40, end="\n\n")
################################

print("List PART-5")
print("Add/Remove/Update")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", "Java"]
print("my_list:", my_list, end="\n\n")

# Add
my_list.append("C++")
print("my_list after appending c++:", my_list, end="\n\n")

# Update
my_list[1] = "C"
print("my_list after updating c:", my_list, end="\n\n")
# [10, 'C', 'python', 'Java', 'C++']

# Remove
my_list.pop() # Remove last value else specify index in pop()
my_list.remove("python")
print("my_list after removing 'python' & c++:", my_list, end="\n\n")

print("#"*40, end="\n\n")
################################
