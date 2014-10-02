#!/usr/bin/env python
from flaskBase import db
db = db.db
from flaskBase.models import *

db.create_all()
