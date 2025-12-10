from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # REGISTER ROUTES
    from .controllers.message_controller import message_bp
    app.register_blueprint(message_bp, url_prefix="")  # tanpa /api biar URL lebih sederhana

    return app

 



