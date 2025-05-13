import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

def initialize_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash')

def get_caption(model, image_b64):
    response = model.generate_content([
        {"mime_type": "image/jpeg", "data": image_b64},
        "Describe this image."
    ])
    return response.text
