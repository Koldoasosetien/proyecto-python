# app/app.py
from flask import Flask
from app.routes.routes import ALL_BLUEPRINTS
from app.models.db import engine, session
from app.models.tablas import Base

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    # Crear tablas
    Base.metadata.create_all(engine)

    # Cerrar sesión automáticamente al final del request
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        session.remove()

    for bp in ALL_BLUEPRINTS:
        app.register_blueprint(bp)

    return app
