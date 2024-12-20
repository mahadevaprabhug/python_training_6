"""
Dictionary:
        -- To keep multiple values like list of employee names
        -- We can keep duplicate values
        -- We can provide our own index to each value called: KEY/VALUE pair
"""

print("Dictionary PART-1")
print("-"*20)
# --------------

my_dictionary_1 = {0: 5, 1: "python", 2: "online"}

# FOR KEYS: We can use any IMMUTABLE values
my_dictionary_2 = {"duration": 5, "course": "python", "mode": "online"}

# FOR VALUES: We can keep any values
my_dictionary_3 = {
    "duration": 5,
    "course": "python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname":"xyz"}
}

# In all the cases, it will create object of builtin class 'dict' and store the values

print("my_dictionary_1:", my_dictionary_1, sep="\n", end="\n\n")
print("my_dictionary_2:", my_dictionary_2, sep="\n", end="\n\n")
print("my_dictionary_3:", my_dictionary_3, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
################################

print("Dictionary PART-2")
print("Access individual values")
print("-"*20)
# --------------

my_dictionary = {
    "duration": 5,
    "course": "python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname":"xyz"}
}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n")

print("Course Name:", my_dictionary["course"]) # "python"
print("Course Name:", type(my_dictionary["course"])) # "python"
print("2nd char in Course Name:", my_dictionary["course"][1], end="\n\n") # "y"

print("mode:", my_dictionary["mode"]) # ["online", "offline"]
print("last mode:", my_dictionary["mode"][-1]) # "offline"
print("4th char in last mode:", my_dictionary["mode"][-1][2:4]) # "fl"
merged_string = my_dictionary["mode"][-1][2:4] + my_dictionary["mode"][-1][-1]
print("merged_string:", merged_string, end="\n\n")

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname":"xyz"}

fname = my_dictionary["trainer"]["fname"] # "abc"
fname_2nd_char = fname[1] # "b"

lname = my_dictionary["trainer"]["lname"] # "xyz"
lname_last_char = lname[-1] # 'z'

final_string = fname_2nd_char + lname_last_char
print("final_string:", final_string, end="\n\n")

print("#"*40, end="\n\n")
################################

print("Dictionary PART-3")
print("Methods present inside 'dict' class")
print("-"*20)
# --------------

# print(dir(my_dictionary))
# OR
print(dir(dict))

print("#"*40, end="\n\n")
################################

print("Dictionary PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# --------------

my_dictionary = {"duration": 5, "course": "python", "mode": "online"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

# ADD or UPDATE: If key present then update else add new
my_dictionary["course"] = "Java" # Key present so update
my_dictionary["location"] = "India" # Key not present so add new
# OR
another_dictionary = {"branch": "branch1"}
my_dictionary.update(another_dictionary) # If key present then update else add new
print("my_dictionary after adding/updating course, location, branch:", my_dictionary, sep="\n", end="\n\n")

# Remove
# {'duration': 5, 'course': 'Java', 'mode': 'online', 'location': 'India', 'branch': 'branch1'}
my_dictionary.pop("mode")
# {'duration': 5, 'course': 'Java','location': 'India', 'branch': 'branch1'}
my_dictionary.popitem() # last value will be removed
# {'duration': 5, 'course': 'Java','location': 'India'}
print("my_dictionary after removing mode & branch:", my_dictionary, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
################################
