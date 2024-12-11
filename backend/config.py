import google.generativeai as genai
import logging

def configure_generative_ai():
    try:
        genai.configure(api_key="")
        logging.info("Google Generative AI configured successfully.")
    except Exception as e:
        logging.error(f"Failed to configure Google Generative AI: {e}")
        raise
