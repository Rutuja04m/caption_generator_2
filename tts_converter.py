from gtts import gTTS

def text_to_speech(text, output_path="caption_audio.mp3"):
    tts = gTTS(text=text)
    tts.save(output_path)
    return output_path
