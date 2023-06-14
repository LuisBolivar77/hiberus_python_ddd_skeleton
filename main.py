from flask import Flask
from injector import Injector

from config import init
from config.DependencyInjection.app_module import AppModule

app = Flask(__name__)
injector = Injector([AppModule()])

init(app, injector)

if __name__ == '__main__':
    app.run()
