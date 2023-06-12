from flask import Flask
import yaml


def main_app():
    app = Flask(__name__)

    with open('config/routes.yaml', 'r') as file:
        yaml_routes = yaml.safe_load(file)

    for route in yaml_routes:
        path = route['path']
        methods = route['methods']
        class_file = route['class_file']
        class_name = route['class_name']
        action = route['action']

        module_name, file_name = class_file.rsplit('.', 1)
        module = __import__(module_name, fromlist=[file_name])
        controller_class = getattr(module, file_name)
        func = getattr(getattr(controller_class, class_name)(), action)

        app.add_url_rule(path, view_func=func, methods=methods)

    return app


if __name__ == '__main__':
    app = main_app()
    app.run()
