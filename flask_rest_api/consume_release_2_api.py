"""
requests library for accessing API
"""

print("GET: Getting all records")
print("-"*20)
# --------------

try:
    import requests

    api_response = requests.get("http://127.0.0.1:5000/getdbdata")
    api_data = api_response.json()

    print("api_data:", api_data, end="\n\n")
    print("type of api_data:", type(api_data), end="\n\n")

except Exception as e:
    print("Error Details:", e, sep="\n", end="\n\n")
    print("""
    Not able to access API. 
    Please make sure my_rest_api_release_2.py is running
    """)
    exit()


print("#"*40, end="\n\n")
################################

print("POST: Adding new records")
print("-"*20)
# --------------

try:
    import requests

    api_response = requests.post("http://127.0.0.1:5000/postdbdata",
                                 json={
                                     "IP":"124.124.124.124",
                                     "DATE":"20/Dec/2024",
                                     "PICS": "abc.jpg"
                                 }
                                 )
    api_data = api_response.json()

    print("api_data:", api_data, end="\n\n")
    print("type of api_data:", type(api_data), end="\n\n")

except Exception as e:
    print("Error Details:", e, sep="\n", end="\n\n")
    print("""
    Not able to access API. 
    Please make sure my_rest_api_release_2.py is running
    """)
    exit()

print("#"*40, end="\n\n")
################################
