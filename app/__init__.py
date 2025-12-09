from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # REGISTER BLUEPRINT
    from .controllers.message_controller import message_bp
    app.register_blueprint(message_bp, url_prefix="/api")

    return app


