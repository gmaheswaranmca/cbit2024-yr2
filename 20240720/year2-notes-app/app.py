from flask import Flask, render_template, request, redirect ###2
from db import noteTablesCreate, readAllNotes #
from db import createNote, readNoteById, updateNote  ###3
from db import search, deleteNote, Note  ###2+1
noteTablesCreate() # db is created if not exist, tbl is created if not exist.
app = Flask(__name__)
@app.route("/list",methods=['GET'])
def notes_list():
    notes = readAllNotes() #list of notes objects #
    for I in range(len(notes)):
        notes[I].sno = I + 1
    return render_template('list.html',notes=notes, menu='list')#
@app.route("/create",methods=['GET','POST'])
def notes_create(): ###all
    note = Note()
    if request.method == 'GET':
        return render_template('create.html',note=note, menu='create')
    elif request.method == 'POST':
        note.title = request.form['title']
        note.notes = request.form['notes']
        createNote(note)
        return redirect('/list')
@app.route("/view/<id>")
def notes_view(id,methods=['GET']):
    note = readNoteById(id)
    return render_template('view.html', note=note, menu='view')
@app.route("/edit/<id>",methods=['GET','POST'])
def notes_edit(id):
    note = readNoteById(id)
    if request.method == 'GET':
        return render_template('edit.html',note=note, menu='edit')
    elif request.method == 'POST':
        note.title = request.form['title']
        note.notes = request.form['notes']
        updateNote(note)
        return redirect('/list')

@app.route("/",methods=['GET','POST'])
def notes_index():
    if request.method == 'GET':
        return render_template('index.html', menu='search')
    elif request.method == 'POST':
        title = request.form['title']
        notes_text = request.form['notes']
        notes = search(title,notes_text)
        for I in range(len(notes)):
            notes[I].sno = I + 1
        return render_template('list.html',notes=notes, menu='list')

@app.route("/delete",methods=['POST'])
def notes_delete():
    if request.method == 'POST':
        id = request.form['id']
        deleteNote(id)
        return redirect('/list')

