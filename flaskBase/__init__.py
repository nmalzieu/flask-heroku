from flask import Flask
from settings import DATABASE

app = Flask(__name__)
app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE

app.config['RESTFUL_JSON'] = {'default': lambda obj: obj.isoformat() if hasattr(obj, 'isoformat') else obj}

from flaskBase.api import v1
from flaskBase.web import index
