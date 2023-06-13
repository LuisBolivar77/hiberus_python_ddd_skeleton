from flask import request
from flask.views import MethodView
from src.Registration.Application.Upsert.user_creator import UserCreator
from injector import inject


class UserPutController(MethodView):

    @inject
    def __init__(self, user_creator: UserCreator):
        self.user_creator = user_creator

    def put(self):
        name = request.get_json()['name']
        return f"Hello World {name}"
