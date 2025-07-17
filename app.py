import os
import cv2
import face_recognition
import speech_recognition as sr
import pyttsx3
from flask import Flask, render_template, jsonify

# Flask App
app = Flask(__name__)

# Load known face
KNOWN_FACE_PATH = "known_faces/user.jpg"
known_image = face_recognition.load_image_file(KNOWN_FACE_PATH)
known_encoding = face_recognition.face_encodings(known_image)[0]

# Voice Authentication Settings
VOICE_PASSWORD = "open sesame"

# Text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Face recognition logic
def is_face_recognized():
    cap = cv2.VideoCapture(0)
    result = False
    speak("Scanning your face...")
    for _ in range(10):
        ret, frame = cap.read()
        if not ret:
            continue
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb_frame)
        encodings = face_recognition.face_encodings(rgb_frame, faces)
        for face_encoding in encodings:
            match = face_recognition.compare_faces([known_encoding], face_encoding)
            if match[0]:
                result = True
                break
        if result:
            break
    cap.release()
    return result

# Voice recognition logic
def is_voice_matched():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    speak("Please say the voice password.")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)
    try:
        voice_text = recognizer.recognize_google(audio)
        print(f"Recognized: {voice_text}")
        return VOICE_PASSWORD.lower() in voice_text.lower()
    except sr.UnknownValueError:
        return False
    except sr.RequestError:
        return False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/unlock")
def unlock():
    if not is_face_recognized():
        return jsonify({"status": "Face not recognized", "unlocked": False})
    if not is_voice_matched():
        return jsonify({"status": "Voice mismatch", "unlocked": False})
    speak("Access granted. Unlocking door.")
    return jsonify({"status": "Access granted", "unlocked": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)