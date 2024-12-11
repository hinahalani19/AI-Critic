from flask import Flask
from flask_cors import CORS
from controllers.critic_controller import CriticController
from config import configure_generative_ai
from utils.logger import configure_logging

def create_app():
    app = Flask(__name__)
    CORS(app)
    configure_logging()
    configure_generative_ai()

    # Register routes
    CriticController.register_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)