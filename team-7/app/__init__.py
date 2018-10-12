from flask import Flask
# from flask_login import LoginManager
# from flask_mongoalchemy  import MongoAlchemy
# from config import Config

app = Flask(__name__)
# app.config.from_object(Config)
# db = MongoAlchemy(app)
# login = LoginManager(app)

from app import routes