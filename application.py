import os
import re
from flask import Flask, jsonify,redirect, render_template, request
from werkzeug import secure_filename
import sqlite3
from flask import g
import datetime
import requests
import datefinder
from helpers import *

# Configure application
app = Flask(__name__)

# Sets the database variable to refer to events.db
DATABASE = 'events.db'

# Sets the upload folder for uploads to the web application to the static folder so they can be accessed later
UPLOAD_FOLDER = '/Users/gavinlifrieri/Programming/CS50Final/Eventr/static'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/scan",methods = ['GET', 'POST'])
def scan():
    if request.method=='GET':
        return render_template("scan.html")
    elif request.method=='POST':

        # Handles getting the file from the form and securely saving it to the server 
        if 'file' not in request.files:
            return redirect("/")
        
        file = request.files['file']

        if file.filename == '' or not allowed_file(file.filename):
            return redirect("/")

        # Saves valid vile to the server
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Data to be delivered to optical character recognition API
        payload = {'isOverlayRequired': "false",
               'apikey': "9189727c0e88957",
               'language': "eng",
               }
        name = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(name, 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image', files={'filename': f}, data=payload)
        text = r.json()['ParsedResults'][0]['ParsedText']

        # Datefinder library finds potential matches and assigns to matches
        matches = datefinder.find_dates(text)

        # Date initialized to sentinal value to determine if any valid matches found
        date = 0
        for match in matches:
            date = match
        if date == 0:
            # On failure, redirect to manual enter
            return redirect("/manual")
        else:
            title = request.form.get("title")
            

            if not title:
                return redirect("/")

            insert_event(title, date, filename)
            return redirect("/events")

@app.route("/events")
def events():
    # Creates events list of event objects for jinja templating
    events = []
    for e in query_db('select * from events'):
        events.append({
                        "title": e["Title"],
                        "date": e["Date"],
                        "image": e["Image"]
                    })
    return render_template("events.html", events=events)

@app.route("/event/<image>")
def event(image):
    # Route to handle rendering of poster associated with a given event
    return render_template("event.html", image=image)

@app.route("/manual",methods = ['GET', 'POST'])
def manual():
    if request.method=='GET':
        return render_template("manual.html")
    elif request.method=='POST':
        if 'file' not in request.files:
            return redirect("/")
        file = request.files['file']

        if file.filename=='' or not allowed_file(file.filename):
            return redirect("/")
        
        # Validates input
        title = request.form.get("title")
        date = request.form.get("date")
        if not title or not date:
            return redirect("/")

        # Adds valid file to server
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        name = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        insert_event(title,date,filename)
    return redirect("/events")