from flask import Flask , jsonify
from flask_cors import CORS
from tools import *
import sqlite3

app = Flask(__name__)
CORS(app)
@app.route('/')
def page0():
    return '0'

@app.route('/1')
def page1():
        d = []
        with sqlite3.connect("data.sqlite") as conn :
          sql_cmd = "select * from data;"
          for row in conn.execute(sql_cmd) :
            a = {}
            a["id"] = row[0]
            a["user"] = row[1]
            a["password"] = row[2]
            a["age"] = row[3]
            d.append(a)
        return jsonify(d)
app.run(host,port)