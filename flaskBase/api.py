import flask
from flask.ext import restful

from . import app
from db import db
from decorators import login_required

API = restful.Api(app)


class SampleRessource(restful.Resource):

    @login_required
    def get(self):
        request = flask.request
        return {'message': 'hello'}, 200

API.add_resource(SampleRessource, '/api/sample/')
