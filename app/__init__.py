from flask import Flask
from .routes import routes
import os

def create_app():
    carpeta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    app = Flask(
        __name__,
        template_folder=os.path.join(carpeta, 'templates'),
        static_folder=os.path.join(carpeta, 'static')
    )

    app.register_blueprint(routes)
    return app