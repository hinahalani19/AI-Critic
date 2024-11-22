import google.generativeai as genai
from googletrans import Translator
from gtts import gTTS
import io
import os
import pygame

# Configure API key generated from https://ai.google.dev/gemini-api/docs
genai.configure(api_key="")

# Define Gemini model to use
model = genai.GenerativeModel("gemini-1.5-flash")

responseText = ""
language = 'en'
translated_text = ""



# Generate text content
def generate_critic(movieName):
    responseText = ""
    response = model.generate_content(f"can you roast {movieName} movie and give fun critic review in very short")
    print(f"Query: can you roast {movieName} movie and give fun critic review in very short")
    responseText = response.text
    print(responseText)
    return responseText



# Text to Speech using gTTS by Gemini with mp3 file save
def speak_with_mp3(responseText, language):
    ttsResponse = gTTS(text=responseText, lang=language, slow=False) # Generate TTS
    ttsResponse.save("GeminiMovieReview.mp3")
    os.system("start GeminiMovieReview.mp3")



# Text to Speech using gTTS by Gemini withot mp3 file save
def speak_without_save(responseText, language):
    print("language= "+ language)
    ttsResponse = gTTS(text=responseText, lang=language, slow=False) # Generate TTS
    fp = io.BytesIO() # Get the audio data in memory (in-memory binary stream)
    ttsResponse.write_to_fp(fp) #writes the audio data to this stream
    fp.seek(0) # Reset the file pointer to the beginning
    pygame.mixer.init() # Initialize pygame mixer
    pygame.mixer.music.load(fp) # Load the audio data directly from the BytesIO object
    pygame.mixer.music.play() # Play the audio
    # Wait for the music to finish playing (optional, but good practice)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Check every 100ms
    # Cleanup (important!)
    pygame.mixer.quit()
    fp.close()



# Translate the text
def translate(responseText, target_language="en", source_language="auto"):
     translated_text = ""
     try:
        translator = Translator()  # For Google Translate API
        translation = translator.translate(responseText, dest=target_language, src=source_language)
        translated_text = translation.text
        print(translated_text)
        return translated_text
     except Exception as e:
        print(f"An error occurred: {e}")
    

# Adjust target language as needed
def translate_and_speak(responseText, target_language):
    # call speak function
    speak_without_save(translate(responseText), target_language)
   



#translate_and_speak(generate_critic("DDLJ"))
#speak_without_save(generate_critic("DDLJ"), language)