from flask import request, jsonify
from flask.views import MethodView
from src.Registration.Application.Upsert.user_creator import UserCreator
from injector import inject
from src.Shared.Infrastructure.api_controller import ApiController


class UserPutController(MethodView, ApiController):

    @inject
    def __init__(self):
        self.user_creator = self.injector.get(UserCreator)

    def put(self):
        uuid = request.get_json()['uuid']
        name = request.get_json()['name']
        email = request.get_json()['email']
        password = request.get_json()['password']

        self.user_creator.creator(uuid, name, email, password)

        response = jsonify({'message': 'Created'})
        return response, 201
