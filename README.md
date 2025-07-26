Voice Assistant
A simple voice-controlled assistant built with Python that can tell the time and date, perform Google searches, and respond to spoken commands using speech recognition and text-to-speech.

Features
🔊 Text-to-speech responses using pyttsx3

🎤 Voice recognition with speech_recognition

⏰ Tells the current time and date

🌐 Performs Google searches based on voice input

🛑 Can exit the program with voice commands

Requirements
Python 3.x

Microphone (for voice input)

Dependencies
Install the required Python packages using pip:

bash
Copy
Edit
pip install pyttsx3 SpeechRecognition pyaudio
⚠️ Note: On some systems, installing pyaudio might require additional setup.
For Windows: pip install pipwin && pipwin install pyaudio
For macOS/Linux: Use your package manager to install portaudio, then install pyaudio.

How It Works
The assistant uses your microphone to listen for voice input.

It recognizes the command using Google Speech Recognition.

It responds with text-to-speech and performs an action:

Say "time" to hear the current time.

Say "date" to hear today’s date.

Say "search" followed by your query to perform a Google search.

Say "exit" or "stop" to close the assistant.

Usage
Run the script:

bash
Copy
Edit
python voice_assistant.py
Speak commands clearly into your microphone when prompted.

Example Commands
"What time is it?"

"What's the date today?"

"Search for weather in Paris"

"Stop"

Limitations
Requires an internet connection for Google Speech Recognition.

May not handle complex or noisy speech input well.

