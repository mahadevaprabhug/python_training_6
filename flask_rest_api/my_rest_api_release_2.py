"""
Supported End Points:
1. Getting all records
    END POINT: http://127.0.0.1:5000/getdbdata
2. Adding new record
    END POINT: http://127.0.0.1:5000/postdbdata
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
# END POINT - 2: http://127.0.0.1:5000/postdbdata Mapped to route("/postdbdata")
#############
@my_rest_api_app.route("/postdbdata", methods=["POST"])
def post_db_data_function():
    """
    Our Plan:
        Task-1: Receive new record sent by end user
        Task-2: Check whether record already present
        Task-3: Add new record to database
    """
    # -----------
    # Task-1: Receive new record sent by end user
    # -----------
    received_record = flask.request.get_json()
    # received_record = {"IP":'', "DATE":"", "PICS":""}
    ip = received_record.get("IP")
    dt = received_record.get("DATE")
    img = received_record.get("PICS")
    #############

    # -----------
    # Task-2: Check whether record already present
    # -----------
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_query = f"SELECT * FROM MY_TABLE WHERE IP = '{ip}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchone()
    if my_db_result is None:
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{dt}', '{img}')"
        my_db_cursor.execute(my_query)
        my_db_connection.commit()
        my_db_connection.close()
        return flask.jsonify("New Record Added")
    else:
        return flask.jsonify("Record Already Present")
    #############

########################

# -----------
# Run the builtin server
#############
my_rest_api_app.run() # default IP=127.0.0.1 port=5000
# my_rest_api_app.run(host='192.168.1.4', port=5000)
########################