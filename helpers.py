import sqlite3
from flask import g

# Sets the database variable to refer to events.db
DATABASE = 'events.db'

# Helper function to access the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    db.row_factory = sqlite3.Row
    return db

# Helper function to query database
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# Helper function to easily insert data into table
def insert_event(title,date, image):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO events (Title,Date,Image) VALUES (?,?,?)", (title,date,image))
    con.commit()
    con.close()