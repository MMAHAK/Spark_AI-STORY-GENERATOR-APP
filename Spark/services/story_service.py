import os
import uuid
from dotenv import load_dotenv
from gtts import gTTS
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("Missing Gemini API key. Set GEMINI_API_KEY in your .env file.")

genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_ai_story(genre: str, theme: str, length: str):
    prompt = f"""
    You are a creative storyteller.

    Write a {length} {genre} story about "{theme}".

    Requirements:
    - Make it engaging and imaginative
    - Include a clear beginning, middle, and end
    - Add some emotions and vivid descriptions
    - Keep it well-structured
    """

    response = model.generate_content(prompt)

    return response.text


def text_to_speech(story_text):
    tts = gTTS(text=story_text, lang="en")

    filename = f"story_{uuid.uuid4().hex}.mp3"
    file_path = f"static/{filename}"

    tts.save(file_path)

    return file_path