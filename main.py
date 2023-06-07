from flask import Flask
from app.routes import healthCheck


def main_app():
    app = Flask(__name__)

    app.register_blueprint(healthCheck)

    return app


if __name__ == '__main__':
    main_app().run()
