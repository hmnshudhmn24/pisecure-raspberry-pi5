# 🔒 PiSecure - Face & Voice Recognition Door Unlock System (Raspberry Pi 5)

PiSecure is an AI-powered security system built for Raspberry Pi 5 that combines facial recognition and voice authentication to unlock a door. It's a smart, touchless, and secure solution for your personal or office space.

## 💡 Features

- Face recognition using OpenCV + face_recognition
- Voice recognition with speech-to-text (Google Speech API)
- Flask web UI to initiate authentication
- Text-to-speech feedback using pyttsx3
- Camera and microphone integration
- Real-time access decision with detailed status

## 🛠️ Tech Stack

- Python 3
- OpenCV
- face_recognition (Dlib)
- SpeechRecognition
- pyttsx3 (TTS)
- Flask

## 🧰 Hardware Requirements

- Raspberry Pi 5
- Pi Camera or USB webcam
- Microphone
- Door actuator or relay module (for actual unlocking)
- Speaker (for voice feedback)

## 🚀 Setup Instructions

### 1. Install dependencies

```bash
sudo apt update
sudo apt install python3-pip python3-opencv libatlas-base-dev portaudio19-dev
pip3 install flask face_recognition opencv-python pyttsx3 SpeechRecognition
```

### 2. Add Your Face

Place a clear image of your face in `known_faces/user.jpg`. This image will be used for recognition.

### 3. Set Voice Password

In `app.py`, change:

```python
VOICE_PASSWORD = "open sesame"
```

To your preferred passphrase.

### 4. Run the App

```bash
python3 app.py
```

Access the dashboard at `http://<your_pi_ip>:5050` and press "Unlock Door".

## 🔐 How it Works

1. Face is scanned using webcam.
2. If matched, system prompts for voice.
3. If voice is verified, door is unlocked.
4. TTS feedback is provided throughout.

## ⚠️ Notes

- Ensure lighting is decent for camera accuracy.
- Ensure microphone is configured properly.
- You can connect the final output to a GPIO pin to control a relay for unlocking.

## 📸 Screenshots

![Dashboard UI](preview.png)

## 📜 License

MIT

---

Built with ❤️ on Raspberry Pi 5.