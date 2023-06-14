from flask import request
from flask.views import MethodView
from src.Registration.Application.Upsert.user_creator import UserCreator
from injector import inject


class UserPutController(MethodView):

    @inject
    def __init__(self, injector):
        self.user_creator = injector.get(UserCreator)

    def put(self):
        name = request.get_json()['name']
        return self.user_creator.creator("uuid", name, "email@email.com", "password")
