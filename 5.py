
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print("You said:", data)
            return data.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can choose voices[1].id for a different voice
    engine.setProperty('rate', 150)  # Adjust speech speed
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        command = recognize_speech()

        if "your name" in command:
            speak("My name is Devil.")

        elif "how old are you" in command:
            speak("I am 1 year old.")

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}.")

        elif 'youtube' in command:
            webbrowser.open("https://www.youtube.com/")

        elif 'github' in command:
            webbrowser.open("https://github.com/rajCodeDev")

        elif 'joke' in command:
            joke = pyjokes.get_joke(language="en", category="neutral")
            print(joke)
            speak(joke)

        elif 'music' in command:
            webbrowser.open("https://youtu.be/Rid5Mj2J8xk")

        elif 'exit' in command:
            speak("Goodbye!")
            break

