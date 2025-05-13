# caption_generator_2
updated version of caption generator->
# Image Caption Generator with Audio Output

This is a simple yet powerful web application that allows users to:

- Upload an image
- Generate a detailed caption for the image using an AI model
- Listen to the generated caption using audio output (text-to-speech)

The project is built with **Python (Flask)** for the backend and **HTML + CSS + JavaScript** for the frontend. The UI is clean and centered, featuring a modern card-style layout with lifted design effects.

---

##  Features

-  Upload an image
-  Generate a descriptive caption using deep learning
-  Listen to the caption through an audio player
-  Beautiful, responsive UI

---

##  Folder Structure
├── app.py # Flask backend logic
├── templates/
│ └── index.html # Main frontend page
├── static/
│ ├── styles.css # All UI styling
│ └── script.js # Frontend JS logic
├── uploads/ # Temporarily stores uploaded images
├── audio/ # Stores generated audio files
├── model/ # (Optional) Place your model weights here
├── README.md # This file

1.Clone the Repo

2.Create & Activate Virtual Environment 
(Python only) (in terminal) 
python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate 

3.Install Dependencies 
pip install -r requirements.txt


4.Set Up Environment Variables Create a .env file in the root folder and add your API key: (in terminal)

GOOGLE_API_KEY=your_actual_api_key_here
(my API KEY= AIzaSyBxcj7TRG1GW1N0tbvdnw4XItgIEjUgwfk or you can create and use yu own API Key)

5.Run the Application 
python app.py 
