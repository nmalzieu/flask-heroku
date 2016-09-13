import flask_restful

from flaskBase import app
from flaskBase.db import db
from flaskBase.decorators import login_required


class flaskBaseAPI(flask_restful.Api):

    def handle_error(self, error):
        db.session.rollback()
        return super(flaskBaseAPI, self).handle_error(error)


API = flaskBaseAPI(app)


class SampleRessource(flask_restful.Resource):

    @login_required
    def get(self):
        return {'message': 'hello'}, 200


API.add_resource(SampleRessource, '/api/v1/sample/')
