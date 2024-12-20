"""
Get data from web_server.log
then
extract using regular expression
"""

print("Getting data from web_server.log")
print("-"*20)
# --------------

my_log_file_handle = open(r"../log/web_server.log", "rb")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content, end="\n\n")

print("#"*40, end="\n\n")
################################

print("Check whether it is IP address line or not")
print("-"*20)
# --------------

import re

for each_line in log_file_content:
    # match_result = re.match('\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]', each_line)
    # OR
    match_result = re.match(br'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    # br : b -> bytes r -> raw string
    print("Each Line:", each_line)
    print("match_result:", match_result, end="\n\n")

# COMMENT
# r-> raw string
r"""
Regular Expression

IDENTIFIERS
------------
\d -> to tell it is any ONE digit b/n 0 to 9
\D -> to tell it is any ONE non-digit. any character except 0 to 9
. -> to tell any ONE any character
\. -> to tell strictly DOT
------------

QUANTIFIERS
------------
\d{3} -> it will make \d\d\d
\d{1,3} -> \d or \d\d or \d\d\d
------------

MODIFIERS
------------
* -> to make 0 or more times
+ -> to make 1 or more times
? -> to make 0 or 1 time
------------

"""

print("#"*40, end="\n\n")
################################

print("Extract IP")
print("-"*20)
# --------------

import re

for each_line in log_file_content:
    # match_result = re.match('\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]', each_line)
    # OR
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3})(.*)', each_line)
    # br : b -> bytes r -> raw string
    if match_result is not None:

        ip = match_result.group(1)
        ip = ip.decode() # Convert to string

        remaining = match_result.group(2)

        print("IP:", ip)
        print("remaining:", remaining, end="\n\n")

# COMMENT
# r-> raw string
r"""
put () to IP address pattern to capture
this is called grouping
each group has index number starting from 1
"""

print("#"*40, end="\n\n")
################################

print("Extract IP, DATE")
print("-"*20)
# --------------

import re

for each_line in log_file_content:
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*', each_line)

    if match_result is not None:

        ip = match_result.group(1)
        ip = ip.decode() # Convert to string

        dt = match_result.group(2)
        dt = dt.decode()

        print(ip, dt)

# COMMENT
# r-> raw string
r"""

26/Apr/2000

26
---
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
\d[0-9] # Strictly 2 digits
[0-9]\d # Strictly 2 digits

\d{1,2} # minimum 1, maximum 2
[0-9]{1,2} # minimum 1, maximum 2
\d?\d # minimum 1, maximum 2
[0-9]?[0-9] # minimum 1, maximum 2
[0-9]?\d # minimum 1, maximum 2
\d?[0-9] # minimum 1, maximum 2
---

Apr
---
[a-zA-Z][a-zA-Z][a-zA-Z]
[a-zA-Z]{3}
[A-Z][a-z][a-z]
[A-Z][a-z]{2}
(Jan|Feb|Mar|Apr)
---

"""

print("#"*40, end="\n\n")
################################


print("Extract IP, DATE, PICS")
print("-"*20)
# --------------

import re

for each_line in log_file_content:
    # Provided less information here, so NOT WORKING
    # match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(\w+\.[a-z]{3}).*', each_line)

    # Below pattern not matching lines which is not having image names
    # match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST|PUT|PATCH|DELETE)\s/pics/(\w+\.(gif|jpg)).*',each_line)

    # Making (pics/wpaper.gif) portion optional so that
    # lines which are not having image name also matched
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST|PUT|PATCH|DELETE)\s/(pics/(\w+\.(gif|jpg)))?.*', each_line)

    if match_result is not None:

        ip = match_result.group(1)
        ip = ip.decode() # Convert to string

        dt = match_result.group(2)
        dt = dt.decode()

        img = match_result.group(5)
        if img is None:
            img = "No Image"
        else:
            img = img.decode()
        print(ip, dt, img)

# COMMENT
# r-> raw string
r"""

\w -> [a-zA-Z_0-9]
\W -> [^a-zA-Z_0-9] # ^ -> excluding

\s -> One SPACE
\S -> any character except SPACE

"""

print("#"*40, end="\n\n")
################################
