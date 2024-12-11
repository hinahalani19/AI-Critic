from flask import Blueprint, jsonify, request
from models.critic_model import CriticModel
import logging

class CriticController:
    critic_model = CriticModel()
    blueprint = Blueprint("critic", __name__, url_prefix="/api/v1/critics")

    @staticmethod
    def register_routes(app):
        app.register_blueprint(CriticController.blueprint)

    @blueprint.route("/generate/<movie_name>/<target_language>", methods=["GET"])
    def generate_critic(movie_name, target_language):
        try:
            review = CriticController.critic_model.generate_critic_review(movie_name, target_language)
            return jsonify({"review": review}), 200
        except ValueError as ve:
            logging.warning(f"Validation error: {ve}")
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return jsonify({"error": "Failed to generate critic review."}), 500

    @blueprint.route("/speak", methods=["POST"])
    def speak():
        try:
            data = request.json
            response_text = data.get('response_text')
            language = data.get('language', 'en').lower()

            CriticController.critic_model.text_to_speech(response_text, language)
            return jsonify({"message": "Speech played successfully."}), 200
        except ValueError as ve:
            logging.warning(f"Validation error: {ve}")
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return jsonify({"error": "Failed to play speech."}), 500

    @blueprint.route("/translate", methods=["POST"])
    def translate():
        try:
            data = request.json
            response_text = data.get('response_text')
            target_language = data.get('target_language', 'en').lower()
            source_language = data.get('source_language', 'auto').lower()

            translated_text = CriticController.critic_model.translate_text(
                response_text, target_language, source_language
            )
            return jsonify({"translated_text": translated_text}), 200
        except ValueError as ve:
            logging.warning(f"Validation error: {ve}")
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return jsonify({"error": "Failed to translate text."}), 500
