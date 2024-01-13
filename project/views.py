from flask import Blueprint , render_template, request, flash, jsonify
from flask_login import  login_required, current_user
from .models import Note
from . import db
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        age = request.form.get('age')
        city = request.form.get('city')

        if len(note) < 1:
            flash('add patients!', category='error')
        if len(age) < 1:
            flash('Age should be greater then 0', category='error')
        if len(city) < 1:
            flash('City not allowed!', category='error')
        else:
            new_note = Note(data=f"Name:{note}, Age:{age}, City:{city}", user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Patient added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods =['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
             db.session.delete(note)
             db.session.commit()

    return jsonify({})
