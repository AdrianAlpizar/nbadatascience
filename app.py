from flask import Flask, jsonify, request, redirect
from flask.templating import render_template
from flask_socketio import SocketIO
from matplotlib import pyplot as plt

import numpy as np
import face_recognition
import requests
import io
import random

from imagescan import known_faces
from playerstat import player_stat, players
from draftvisual import draftgraphing


from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 


# from playerstat import graph


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)



player = ''
playername_for_stat = ''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/', methods=['GET', 'POST'])
def search():
    errors = []
    if request.method == "POST":
        # get url that the user has entered
        try:
            search = request.form['search']
            r = requests.get(search)
            player_name = r.text
            playername_lower = player_name.lower()
            playername_for_stat += playername_lower
            for player in players:
                if player_name == player.lower():
                    player = player_name
                    player_stat()

        except:
            errors.append(
                "Unable to get text. Please make sure it's valid and try again."
            )
    return redirect('/chart')


@app.route('/chart')
def chart():
    return render_template('player.html', name='Shot Chart', url='static/img/shotchart.png', player=player)


@app.route('/draft')
def chart():
    draftgraphing()
    return render_template('draft.html', url='static/img/draftplayers.png')


@app.route('/chat')
def chat():
    return render_template('chat.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print(json)
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


@app.route('/imagesearch', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            return detect_faces_in_image(file)

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>Upload</title>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''


def detect_faces_in_image(file_stream):
    # Pre-calculated face encoding of Obama generated with face_recognition.face_encodings(img)

    is_obama = False
    face_found = False
    # Load the uploaded image file
    img = face_recognition.load_image_file(file_stream)
    # Get face encodings for any faces in the uploaded image
    unknown_face_encoding = face_recognition.face_encodings(img)[0]
    results = face_recognition.compare_faces(
        known_faces, unknown_face_encoding)

    if results[0]:
        player = 'Alex Caruso'
    elif results[1]:
        print('Anthony Davis')
    elif results[2]:
        print('Avery Bradley')
    elif results[3]:
        print('Kentavious Caldwell-Pope')
    elif results[4]:
        print('Kostas Antetokounmpo')
    elif results[5]:
        print('Quinn Cook')
    elif results[6]:
        print('DeMarcus Cousins')
    elif results[7]:
        print('Troy Daniels')
    elif results[8]:
        print('Danny Green')
    elif results[9]:
        print('Jared Dudley')
    elif results[10]:
        print('Talen Horton-Tucker')
    elif results[11]:
        print('Dwight Howard')
    elif results[12]:
        print('LeBron James')
    elif results[13]:
        print('Kyle Kuzma')
    elif results[14]:
        print('JaVale McGee')
        face_found = True
    elif results[15]:
        print('Zach Norvell Jr.')
    elif results[16]:
        print('Rajon Rondo')
    else:
        print('The person is not a Los Angeles Laker Player')

    return redirect('/chart')


if __name__ == '__main__':
    socketio.run(app, debug=True)
