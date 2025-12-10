from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # REGISTER ROUTES
    from .controllers.webhook_controller import webhook_bp
    app.register_blueprint(webhook_bp, url_prefix="/webhook")

    return app




