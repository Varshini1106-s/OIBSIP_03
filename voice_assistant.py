import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speaking rate

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    return command.lower()

def run_assistant():
    os.system('clear')  # clear terminal on Linux/macOS/GitHub Codespaces
    speak("Hello! How can I help you?")
    while True:
        command = take_command()
        if not command:
            continue

        speak(f"You said: {command}")

        if 'hello' in command:
            speak("Hi there! How can I assist you?")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%B %d, %Y')
            speak(f"Today's date is {date}")
        elif 'search' in command:
            speak("What should I search for?")
            query = take_command()
            if query:
                url = f"https://www.google.com/search?q={query}"
                webbrowser.open(url)
                speak(f"Here are the search results for {query}")
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    run_assistant()
