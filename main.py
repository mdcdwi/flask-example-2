from flask import Flask

app = Flask(__name__)

@app.route("/api/cek", methods=['GET'])
def cek():
    return "Backend 2"

@app.route("/", methods=['GET'])
def test():
    return "WEB BACKEND APP"

@app.route("/req", methods=['GET'])
def req():
    return "req brwa"

app.run(host='0.0.0.0', port=8080, threaded=True)
