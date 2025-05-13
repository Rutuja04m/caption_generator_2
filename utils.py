import base64
import io
from PIL import Image

def encode_image(image_path):
    with Image.open(image_path) as img:
        buffered = io.BytesIO()
        img.save(buffered, format=img.format)
        img_bytes = buffered.getvalue()
        return base64.b64encode(img_bytes).decode()
