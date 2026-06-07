import speech_recognition as sr
import pyttsx3
import datetime
import sys
import webbrowser

from ai_helper import ask_ai

def speak(text):
    print("Assistant:", text)
    engine = pyttsx3.init()
    try:     

        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id) 
        elif voices:
            engine.setProperty('voice', voices[0].id)
        
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking: {e}")

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Adjusted for noise, waiting for speech...")

            audio = recognizer.listen(source, timeout=10)
            print(f"Received audio data ({len(audio.frame_data)} bytes)")

        try:
            print("Sending to Google Speech Recognition...")
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()

        except sr.UnknownValueError:
            print("Could not understand audio - Google could not interpret the words")
            return ""
        except sr.RequestError as e:
            print(f"Network error with Google API: {e}")
            return ""
            
    except sr.WaitTimeoutError:
        print("No speech detected or the microphone timed out.")
        return ""
    except OSError as e:
        print(f"Microphone unavailable: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error in listen(): {type(e).__name__}: {e}")
        return ""
if __name__ == "__main__":

    speak("Voice Assistant Started")

    while True:

        command = listen()
    
        if not command:  
            continue

        if "hello" in command:
            speak("Hello, ask me anything! I can tell you the time, date, or even a joke!")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today is {current_date}")
        elif "how are you" in command:
            speak("I am doing well, thankyou for asking, how are you?")
        elif "what is your name" in command:
            speak("My name is trivya, I am your voice assistant")
        elif "who created you" in command:
            speak("I was created by Shalini")   
        elif "who are you" in command:
            speak("I am trivya, your voice assistant. I can tell you the time, date, and even a joke!")
        elif "python tutorial" in command:
            speak("opening python tutorial")
            query = command.replace(" ", "+")
            webbrowser.open("https://www.google.com/search?q=" + query)
        elif "youtube" in command:
            speak("opening Youtube")
            webbrowser.open("https://www.youtube.com")
        elif "google" in command:
            speak("opening Google")
            webbrowser.open("https://www.google.com")
        elif "github" in command:
            speak("opening Github")
            webbrowser.open("https://www.github.com")
        elif "exit" in command:
            speak("Goodbye, nice to talk to you, Have a great day!")
            print("Voice Assistant Stopped")
            sys.exit(0)
        else:
            response = ask_ai(command)
            short_response = response[:250]
            speak(response)



