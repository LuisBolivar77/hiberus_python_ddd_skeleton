import yaml
from dotenv import load_dotenv


def init(app):
    load_dotenv("config/Environments/.env")
    init_routes(app)


def init_routes(app):
    with open('config/Routes/routes.yaml', 'r') as file:
        yaml_routes = yaml.safe_load(file)

    with app.app_context():
        for route in yaml_routes:
            path = route['path']
            methods = route['methods']
            class_file = route['class_file']
            class_name = route['class_name']
            action = route['action']

            module_name, file_name = class_file.rsplit('.', 1)
            module = __import__(module_name, fromlist=[file_name])
            controller_class = getattr(module, file_name)
            func = getattr(controller_class, class_name)

            app.add_url_rule(path, view_func=func.as_view(action), methods=methods)
