import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'qweqwe'
toolbar = DebugToolbarExtension(app)

from app import routes