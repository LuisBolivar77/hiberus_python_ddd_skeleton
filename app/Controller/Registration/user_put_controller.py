from flask import request


class UserPutController:

    def user_put(self):
        name = request.get_json()['name']
        email = request.get_json()['email']
        password = request.get_json()['password']
        return f"Hello World {name}"
