import google.generativeai as genai
import logging
from gtts import gTTS
import io
import pygame

class CriticModel:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_critic_review(self, movie_name):
        if not movie_name:
            raise ValueError("Movie name cannot be blank.")
        try:
            logging.info(f"Generating critic review for movie: {movie_name}")
            response = self.model.generate_content(
                f"Can you roast {movie_name} movie and give a fun critic review in very short"
            )
            return response.text
        except Exception as e:
            logging.error(f"Error generating critic review: {e}")
            raise

    def text_to_speech(self, response_text, language='en'):
        try:
            if not response_text:
                raise ValueError("Response text cannot be empty.")

            logging.info(f"Converting text to speech in language: {language}")
            tts_response = gTTS(text=response_text, lang=language, slow=False)
            fp = io.BytesIO()
            tts_response.write_to_fp(fp)
            fp.seek(0)

            pygame.mixer.init()
            pygame.mixer.music.load(fp)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.quit()
            fp.close()
        except Exception as e:
            logging.error(f"Error during text-to-speech conversion: {e}")
            raise

    def translate_text(self, response_text, target_language='en', source_language='auto'):
        from googletrans import Translator

        try:
            logging.info("Translating text using Google Translator API.")
            translator = Translator()
            translation = translator.translate(
                response_text, dest=target_language, src=source_language
            )
            return translation.text
        except Exception as e:
            logging.error(f"Error during translation: {e}")
            raise
