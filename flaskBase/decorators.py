from functools import wraps

import flask
from flask import request
from flask.ext import restful

import models


def login_required(fun):
    @wraps(fun)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if auth:
            user_id = auth.username
            api_key = auth.password
            user = models.User.query.get(user_id)
            # Checking validity
            if user and user.api_key == api_key:
                # Yay, user is good, attaching it
                flask.request.user = user
                return fun(*args, **kwargs)

        return restful.abort(403)
    return decorated_function
