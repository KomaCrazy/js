from tools import *
import json

@app.route('/')
def page0():
    try:
        with sqlite3.connect(path) as conn :
            data = []
            sql_cmd = "select * from " + table + ";"
            for row in conn.execute(sql_cmd) :
                rr = {}
                rr["id"] = row[0]
                rr["first"] = row[1]
                rr["last"] = row[2]
                rr["gmail"] = row[3]
                data.append(rr)
        return jsonify(data)
    except Exception as e:
        print("Error")

app.run(host,port)
