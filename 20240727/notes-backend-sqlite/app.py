from flask import Flask, request, jsonify
from db import Note, noteTablesCreate, createNote, readNoteById
from db import readAllNotes, updateNote, deleteNote, search
from flask_cors import CORS, cross_origin ####
noteTablesCreate()          
app = Flask(__name__)
front_end = 'https://y5k7i9-3000.ocws.app' #### #### #### frontend server
CORS(app,origins=[front_end]) #### #### ####

@app.route("/notes",methods=['POST'])
@cross_origin() #### apply for all functions
def notes_create():
    body = request.get_json()
    new_note = Note(title = body['title'], notes = body['notes'])
    id = createNote(new_note)
    note = readNoteById(id)
    note_dict = {'id': note.id, 'title': note.title, 'notes':note.notes}
    return jsonify(note_dict)

@app.route("/notes/<id>",methods=['GET'])
@cross_origin()
def notes_read_byid(id):
    note = readNoteById(id)
    note_dict = {'id': note.id, 'title': note.title, 'notes':note.notes}
    return jsonify(note_dict)

@app.route("/notes",methods=['GET'])
@cross_origin()
def notes_read_all():
    notes = readAllNotes()
    notes_dict = []
    for note in notes:
        notes_dict.append({'id': note.id, 'title': note.title, 'notes':note.notes})
    return jsonify(notes_dict)

@app.route("/notes/<id>",methods=['PUT'])
@cross_origin()
def notes_update(id):
    old_note = readNoteById(id)
    if not old_note:
        return jsonify({'message': 'note is not found'})
    body = request.get_json()
    old_note.title = body['title']
    old_note.notes = body['notes']
    updateNote(old_note)
    note = readNoteById(id)
    note_dict = {'id': note.id, 'title': note.title, 'notes':note.notes}
    return jsonify(note_dict)

@app.route("/notes/<id>",methods=['DELETE'])
@cross_origin()
def notes_delete(id):
    old_note = readNoteById(id)
    if not old_note:
        return jsonify({'message': 'note is not found', 'is_error':1})
    deleteNote(id)
    return jsonify({'message': 'note is deleted successfully', 'is_error':0})

@app.route("/notes_search",methods=['POST'])
@cross_origin()
def notes_search():
    body = request.get_json()
    notes = search(body['title'],body['notes_text'])
    notes_dict = []
    for note in notes:
        notes_dict.append({'id': note.id, 'title': note.title, 'notes':note.notes})
    return jsonify(notes_dict)