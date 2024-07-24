from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calc/sum/<a>/<b>",methods=['GET'])
def calc_sum(a,b):
    a = int(a)
    b = int(b)
    s = a + b 
    res = {'sum' : s}
    return jsonify(res)

@app.route("/calc/square",methods=['POST'])
def calc_square():
    body = request.get_json()
    num = int(body['num'])
    square = num ** 2
    res = {'square' : square}
    return jsonify(res)