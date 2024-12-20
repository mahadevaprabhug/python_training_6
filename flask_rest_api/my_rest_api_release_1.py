"""
Python for web development

We have many web development frameworks like
flask
django # (MVT-> Model View Template)
fastapi
and many more
"""

"""
We are discussing flask framework
"""

"""
Using flask framework,
1. Using flask framework we can develop REST-API
2. Using flask framework we can develop Websites
3. Using flask framework we can develop Micro Services
"""

"""
We need to discuss on 
how to use flask framework for developing REST-API
"""

"""
Suppose, we need to provide access to our database my_database with others/public
then
how we can provide access with others/public?

OPTION-1: We can create separate credentials like user/password 
    and share.

OPTION-1 will be LIMITED. DIFFICULT to manage
"""

"""
We got 2 solutions.
1. SOAP: Simple Object Access Protocol
2. REST: REpresentational State Transfer

both tells how we can provide access others/public?

both tells to introduce some DOOR/GATE/INTERFACE between our-app with others
it is like
our-app/DB <--INTERFACE--> others/public

This INTERFACE is also called as APPLICATION PROGRAMMING INTERFACE (API)

both tells how to develop such interface

SOAP-API
REST-API
"""

"""
REST came after SOAP
- easy to implement and mange
- popular
"""

"""
flask framework, already implemented REST-ARCHITECTURE,
we just need to know how to create REST-API using flask
"""

"""
We are planning to provide complete-access/full-access to our database table my_table

complete-access/full-access means,

- Create new record in our table my_table
- Read existing record from table my_table
- Update existing record in table my_table
- Delete existing record from table my_table
"""

"""
Http Standards: HTTP Methods

POST        - Create new record in our table my_table
GET         - Read existing record from table my_table
PUT/PATCH   - Update existing record in table my_table
DELETE      - Delete existing record from table my_table
"""

"""
Web server:
flask has builtin web server, we can use it for development purpose
"""

"""
In this release, creating API for providing access to
read existing records from our table my_table
"""

# -----------
# Create APP
#############
import flask
my_rest_api_app = flask.Flask(__name__) # __name__, file name will print
########################

# -----------
# END POINT - 1: http://127.0.0.1:5000/getdbdata Mapped to route("/getdbdata")
#############
@my_rest_api_app.route("/getdbdata", methods=["GET"])
def get_db_data_function():
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    # import json
    # return json.dumps(my_db_result)
    return flask.jsonify(my_db_result)
########################

# -----------
# Run the builtin server
#############
my_rest_api_app.run() # default IP=127.0.0.1 port=5000
# my_rest_api_app.run(host='192.168.1.4', port=5000)
########################