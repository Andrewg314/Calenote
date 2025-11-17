from flask import Flask
from .controllers.auth_controller import auth_bp
from .controllers.notes_controller import notes_bp
from .controllers.events_controller import events_bp
from dotenv import load_dotenv

# load .env file variables
load_dotenv()

# Create app and register blueprints
def create_app():
    app = Flask(__name__)

    # Registering blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(notes_bp, url_prefix='/notes')
    app.register_blueprint(events_bp, url_prefix='/events')
    return app