"""
while-loop: Execute loop based condition
"""

print("While loop example")
print("-"*20)
# --------------

x = 0
while x < 5:
    print("Value of x is:", x)
    x = x + 1 # x += 1

print("#"*40, end="\n\n")
################################

# 2 Cases
# Case-1: 'break-statement': We can end the while-loop
# Case-2: 'continue-statement': We can skip the current iteration

print("# Case-1: 'break-statement': We can end the while-loop in between")
print("-"*20)
# --------------

my_courses_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_courses_list:", my_courses_list, end="\n\n")

# Requirement: Verify are there any Java course? If one course
# found then no need to check for other courses

index_no = 0
# while index_no < 5
while index_no < len(my_courses_list):
    if my_courses_list[index_no].startswith("Java"):
        print("Course 'Java' Found")
        break
    index_no += 1


# for each_course in my_courses_list:
#     if each_course.startswith("Java"):
#         print("Course 'Java' Found")
#         break


print("#"*40, end="\n\n")
################################

print("# Case-2: 'continue-statement': We can skip the current iteration")
print("-"*20)
# --------------

my_courses_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_courses_list:", my_courses_list, end="\n\n")

index_no = 0
while index_no < len(my_courses_list):
    # Below code till end of for-loop, will be applicable for java course
    # So, from this line, other than java course are not required
    if not my_courses_list[index_no].startswith("Java"):
        index_no += 1
        continue
    print("This JAVA course name is:", my_courses_list[index_no])
    print("This is one version of java")
    print("This Java course duration is 5 days", end="\n\n")
    index_no += 1


# for each_course in my_courses_list:
#     # Below code till end of for-loop, will be applicable for java course
#     # So, from this line, other than java course are not required
#     if not each_course.startswith("Java"):
#         continue
#     print("This JAVA course name is:", each_course)
#     print("This is one version of java")
#     print("This Java course duration is 5 days", end="\n\n")

print("#"*40, end="\n\n")
################################
