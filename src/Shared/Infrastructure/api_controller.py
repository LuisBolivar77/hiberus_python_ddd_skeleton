from injector import Injector
from config.DependencyInjection.app_module import AppModule


class ApiController:
    injector = Injector([AppModule()])
