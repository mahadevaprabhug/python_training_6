"""
Read and print website data
https://www.jafsoft.com/searchengines/log_sample.html
"""

print("Read and print website data")
print("-"*20)
# --------------
import urllib.request as u
my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")
web_content = my_web_file_handle.read()
my_web_file_handle.close()

web_content = web_content.decode() # convert bytes to string
print(web_content)

print("#"*40, end="\n\n")
################################
