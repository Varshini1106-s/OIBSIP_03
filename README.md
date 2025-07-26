# 🗣️ Voice Assistant

A simple voice-controlled assistant built in Python. It uses speech recognition to understand spoken commands and text-to-speech to respond. It can tell you the current time and date, perform Google searches, and more!

---

## ✨ Features

- 🔊 Speaks responses using `pyttsx3`
- 🎙️ Listens and understands voice input with `speech_recognition`
- ⏰ Tells the current time
- 📅 Tells the current date
- 🌐 Performs Google searches via voice command
- 🛑 Stops on "exit" or "stop" command

---

## 🛠️ Requirements

- Python 3.6+
- A working microphone
- Internet connection (for speech recognition)

---

Install dependencies

pip install pyttsx3 SpeechRecognition pyaudio

## 🚀Usage
Run the assistant:

bash
Copy
Edit
python voice_assistant.py
Then speak commands like:

"What time is it?"

"What's the date today?"

"Search for Python tutorials"

"Stop" or "Exit"

 ## 🧠How It Works

-Listens to microphone input

-Converts speech to text using Google Speech Recognition

-Matches commands like "time", "date", or "search"

-Speaks the appropriate response using pyttsx3

-Exits cleanly on "exit" or "stop"

