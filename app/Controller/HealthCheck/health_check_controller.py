from flask import jsonify
from flask.views import MethodView


class HealthCheckController(MethodView):

    def __init__(self, injector):
        pass

    def get(self):
        return jsonify({"status": "OK"}), 200
