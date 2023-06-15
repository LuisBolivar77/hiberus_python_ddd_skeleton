from dotenv import load_dotenv, find_dotenv
from flask import Flask
from injector import Injector

from config import init
from config.DependencyInjection.app_module import AppModule

app = Flask(__name__)

load_dotenv("config/Environments/.env")

init(app)

if __name__ == '__main__':
    app.run()
