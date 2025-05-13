from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from gemini_caption import initialize_gemini, get_caption
from tts_converter import text_to_speech
from utils import encode_image
from dotenv import load_dotenv

# Load .env variables (like your Gemini API key)
load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
AUDIO_FOLDER = 'static/audio'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    image = request.files.get('image')
    if not image:
        return jsonify({'error': 'No image uploaded.'})

    image = request.files['image']
    filename = secure_filename(image.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)

    try:
        # Encode image
        image_b64 = encode_image(image_path)

        # Initialize Gemini model
        model = initialize_gemini()

        # Get caption from model
        caption = get_caption(model, image_b64)

        # Generate audio
        audio_path = os.path.join(AUDIO_FOLDER, 'caption.mp3')
        text_to_speech(caption, audio_path)

        return jsonify({
            'caption': caption,
            'image_path': '/' + image_path,
            'audio_path': '/' + audio_path
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
