"""
for-loop: Iterating any collections we can make use of for-loop
"""
print("Iterating string")
print("-"*20)
# --------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

for i in my_string:
    print("Each Char:", i)

print("#"*40, end="\n\n")
################################

print("Iterating list")
print("-"*20)
# --------------

my_list = ["Java", "C", 200, "Python"]

for i in my_list:
    print("Each value in my_list:", i)
    if i == "Python":
        print("2nd char is:", i[1])
        print("2nd char is:", i[::-1])

print("#"*40, end="\n\n")
################################

print("Iterating dictionary keys()")
print("-"*20)
# --------------

my_dictionary = {"duration": 5, "course": "python", "mode": "online"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

# >>> my_dictionary.keys()
# dict_keys(['duration', 'course', 'mode'])
# >>>
for i in my_dictionary.keys():
    print("Key:", i)
    print("Value:", my_dictionary[i]) # my_dictionary["course"]

print("#"*40, end="\n\n")
################################

print("Iterating dictionary values()")
print("-"*20)
# --------------

my_dictionary = {"duration": 5, "course": "python", "mode": "online"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

# >>> my_dictionary.values()
# dict_values([5, 'python', 'online'])
# >>>
for i in my_dictionary.values():
    print("Only Value:", i)

print("#"*40, end="\n\n")
################################

print("Iterating dictionary items()")
print("-"*20)
# --------------

my_dictionary = {"duration": 5, "course": "python", "mode": "online"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

# >>> my_dictionary.items()
# dict_items([('duration', 5), ('course', 'python'), ('mode', 'online')])
# >>>
for i in my_dictionary.items():
    print("Each Tuple:", i)
    print("Key:", i[0])
    print("Value:", i[1])

print("#"*40, end="\n\n")
################################

# 2 Cases
# Case-1: 'break-statement': We can end the for-loop
# Case-2: 'continue-statement': We can skip the current iteration

print("# Case-1: 'break-statement': We can end the for-loop in between")
print("-"*20)
# --------------

my_courses_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_courses_list:", my_courses_list, end="\n\n")

# Requirement: Verify are there any Java course? If one course
# found then no need to check for other courses

for each_course in my_courses_list:
    if each_course.startswith("Java"):
        print("Course 'Java' Found")
        break


print("#"*40, end="\n\n")
################################

print("# Case-2: 'continue-statement': We can skip the current iteration")
print("-"*20)
# --------------

my_courses_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_courses_list:", my_courses_list, end="\n\n")

for each_course in my_courses_list:
    # Below code till end of for-loop, will be applicable for java course
    # So, from this line, other than java course are not required
    if not each_course.startswith("Java"):
        continue
    print("This JAVA course name is:", each_course)
    print("This is one version of java")
    print("This Java course duration is 5 days", end="\n\n")

print("#"*40, end="\n\n")
################################
