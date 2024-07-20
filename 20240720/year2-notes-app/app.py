from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def notes_index():
    return render_template('index.html')
@app.route("/list")
def notes_list():
    notes = [
        {'id':1,'title':'HTML 5','notes':'...'},
        {'id':2,'title':'CSS 3','notes':'...'},
        {'id':3,'title':'Bootstrap','notes':'...'},
        {'id':4,'title':'Javascript','notes':'...'},
    ]
    return render_template('list.html',notes=notes)
@app.route("/create")
def notes_create():
    return render_template('create.html')
@app.route("/view/<id>")
def notes_view(id):
    return render_template('view.html')
@app.route("/edit/<id>")
def notes_edit(id):
    return render_template('edit.html')