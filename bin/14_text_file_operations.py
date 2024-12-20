"""
Text File Operations.
- Reading from text file
- Writing to text file

Text file extensions like .txt, .log, .mylog, .ownextension
"""

"""
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect
"""

"""
We have functions for all 3 steps
Step-1: Connect to file
    - open() function
Step-2: Read/Write
    - FOR WRITING: 1) write 2) writelines 3) print-function
    - FOR READING: 1) read 2) readlines 3) readline
Step-3: Disconnect
    - close()
"""
print("All write operations")
print("-"*20)
# --------------

# Step-1: Connect to file
# --------------
# my_out_file_handle = open("provide file name or file path here", "provide mode here")
my_out_file_handle = open("my_out_file.txt", "w")
# mode 'w': Write Only, It will create new file, It will erase existing content
# mode 'r': Read Only, It will NOT create new file
# mode "a": Append Only, It will create new file if file is not present
# w+, a+, r+, enable read/write mode
# wb, ab, rb, binary file


# Step-2: Write
# --------------

# Our data
x = 10
y = "Python"

# 1) write: It will take one string
my_out_file_handle.write(str(x)+"\n")
my_out_file_handle.write(y+"\n")

# 2) writelines: It will take any collection values like list/tuple etc
L = [str(x)+"\n", y+"\n"]
my_out_file_handle.writelines(L)

# 3) print-function to write to file
print(x, y, 20, "java", sep="\n", file=my_out_file_handle)
# no need convert x & 20 to string, print will take care

# Step-3: Disconnect
# --------------
my_out_file_handle.close()

print("""
All write operations completed.
please check my_out_file.txt
""")

print("#"*40, end="\n\n")
################################

print("Reading from file using: 1) read")
print("-"*20)
# --------------

# Step-1: Connect to file
# --------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# --------------
file_content = my_out_file_handle.read()
# Returns entire file content in ONE string
print("file_content:", file_content, end="\n\n")
print("file_content in raw format:", repr(file_content), end="\n\n")

# Step-3: Disconnect
# --------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
################################

print("Reading from file using: 2) readlines")
print("-"*20)
# --------------

# Step-1: Connect to file
# --------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# --------------
file_content = my_out_file_handle.readlines()
# Returns entire file content in list
print("file_content:", file_content, end="\n\n")


# Step-3: Disconnect
# --------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
################################

print("Reading from file using: 3) readline")
print("-"*20)
# --------------

# Step-1: Connect to file
# --------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# --------------
file_content = my_out_file_handle.readline() # returns one line
print("1st line:", file_content)

file_content = my_out_file_handle.readline() # returns one line
print("2nd line:", file_content)

file_content = my_out_file_handle.readline() # returns one line
print("3rd line:", file_content)

# Step-3: Disconnect
# --------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
################################

print("Reading from file using: 4) for-loop to read line by line")
print("-"*20)
# --------------

# Step-1: Connect to file
# --------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# --------------
for each_line in my_out_file_handle:
    print("Each Line:", each_line)

# Step-3: Disconnect
# --------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
################################
