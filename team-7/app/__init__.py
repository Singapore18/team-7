from flask import Flask, g
import sqlite3
# from flask_login import LoginManager
# from flask_mongoalchemy  import MongoAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# db = MongoAlchemy(app)
# login = LoginManager(app)
DATABASE = 'jpchase.db'

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

init_db()

from app import routes