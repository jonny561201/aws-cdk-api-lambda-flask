from flask import Flask
from src.routes import APP_BLUEPRINT


def create_app(app_name):
    app = Flask(app_name)
    app.register_blueprint(APP_BLUEPRINT)
    return app
