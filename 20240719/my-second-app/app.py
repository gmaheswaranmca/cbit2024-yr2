from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/sum", methods=["GET","POST"])
def calc_sum():
    if request.method == "GET":
        first = 0
        second = 0
        s = 0 
    elif request.method == "POST":
        first = int(request.form['first'])
        second = int(request.form['second'])
        s = first + second 
    return render_template('sum.html', 
            first = first, second = second, sum = s)
@app.route("/square", methods=["GET","POST"])
def calc_square():
    if request.method == "GET":
        num = 0
        square = 0 
    elif request.method == "POST":
        num = int(request.form['num'])
        square = num ** 2
    return render_template('square.html', 
            num = num, square = square)

'''
@app.route("/sum/<a>/<b>")
def calc_sum(a,b):
    c = int(a) + int(b)
    return f"<p>sum of {a} and {b} is {c}.</p>"
'''