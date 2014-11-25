from flask import Flask
from settings import DATABASE

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE

from flaskBase.api import v1
