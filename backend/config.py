import google.generativeai as genai
import logging

def configure_generative_ai():
    try:
        genai.configure(api_key="AIzaSyCV6myTaX1-SlCtuqebN1Vi4eV_VUCT-iM")
        logging.info("Google Generative AI configured successfully.")
    except Exception as e:
        logging.error(f"Failed to configure Google Generative AI: {e}")
        raise
