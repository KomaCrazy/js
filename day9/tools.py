from flask import Flask  , jsonify
from flask_cors import CORS
import sqlite3 

app = Flask(__name__)
CORS(app)
host = '0.0.0.0'
port = 5000

path = "data.sqlite"
table = "box1"

id = "" 
first = ""
last = "" 
data = []

def create_table():
    try:
        with sqlite3.connect(path) as conn :
            sql_cmd = "create table "+table+"(id primary key,first text,last text,email text);"
            conn.execute(sql_cmd)
    except Exception as e:
        print("Error : Create Table")
def find_table():  
    try:
        with sqlite3.connect(path) as conn :
            sql_cmd = "select * from " + table + ";"
            
            for row in conn.execute(sql_cmd) :
                rr = {}
                rr["id"] = row[0]
                rr["first"] = row[1]
                rr["last"] = row[2]
                rr["email"] = row[3]
                data.append(rr)
            print(data)    


    except Exception as e:
        print("Error : find_table")