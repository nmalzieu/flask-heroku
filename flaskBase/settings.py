import os

### DATABASE SETTINGS ###

DATABASE = os.environ.get('DATABASE_URL', "postgresql://postgres:postgres@localhost/flaskBase")
