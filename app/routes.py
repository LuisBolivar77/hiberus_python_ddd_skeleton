from flask import Blueprint, jsonify


healthCheck = Blueprint("HealthCheck", __name__)


@healthCheck.route("/health_check")
def check_health():
    return jsonify({'status': 'OK'}), 200
