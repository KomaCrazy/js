
from flask import Flask ,request , send_from_directory
from flask_cors import CORS 
app = Flask(__name__,)
CORS(app) 
host ='0.0.0.0'
port = 5000

@app.route('/')
def page_0():
    return '0'

@app.route('/1')
def page_1():
    data = request.args
    user = data["user"]
    password = data["password"]
    print(user,password)
    if user == "kaw" and password == "1234":
        return '1'
    else :
        return '0'

if __name__ == '__main__':
    app.run(host,port)