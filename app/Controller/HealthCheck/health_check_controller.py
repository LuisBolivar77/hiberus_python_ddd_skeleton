from flask import jsonify


class HealthCheckController:

    def health_check(self):
        return jsonify({"status": "OK"}), 200
