"""
From the string given below,

Extract

IP
DATE
PICS
URL

Expected Output:
----------------
123.123.123.123
26/Apr/2000
wpaper.gif
http://www.jafsoft.com/asctortf/
----------------

"""
print("How input data looks like?")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
################################

print("Type of input data")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(type(input_data))

print("#"*40, end="\n\n")
################################


print("Extract IP - 1 WAY: PARTIAL")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
ip = input_data[0:15]
print(ip)


print("#"*40, end="\n\n")
################################

print("Extract IP - 2 WAY")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
index_of_1st_space = input_data.index(" ")
ip = input_data[0:index_of_1st_space]
print(ip)

# >>> # About 'index' method
# >>> # Feature-1
# >>> s = "WEL COME"
# >>> s.index("E") # Returns index of 1st occurance of 'E'
# 1
# >>>
# >>> # Feature-2
# >>> s = "WEL COME"
# >>> s.index("E", 3) # Start looking from index 3 onwards
# 7
# >>>
# >>> # Feature-3
# >>> s = "WEL COME"
# >>> s.index("COME")
# 4
# >>> # It will return index of 'C'

print("#"*40, end="\n\n")
################################

print("Extract IP - 3 WAY")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("sp:", sp, sep="\n", end="\n\n")

ip = sp[0]
print(ip)

print("#"*40, end="\n\n")
################################
