import flask
from flask.ext import restful

from flaskBase import app
from flaskBase.db import db
from flaskBase.decorators import login_required


class flaskBaseAPI(restful.Api):

    def handle_error(self, error):
        db.session.rollback()
        return super(flaskBaseAPI, self).handle_error(error)


API = flaskBaseAPI(app)


class SampleRessource(restful.Resource):

    @login_required
    def get(self):
        request = flask.request
        return {'message': 'hello'}, 200

API.add_resource(SampleRessource, '/api/v1/sample/')
