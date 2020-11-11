import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio as pa
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    """Take a string audio and say it."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning... Raaam Raaam... Jai mata dee")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon")
    elif hour>=18 and hour<20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak(f"Hii Sir, my name is Kiara. How may I help you?")

def takeCommand():
    """It take microphone input from the user and returns string output."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1.2
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please say again.")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif any(item in query for item in ['open youtube', 'start youtube']):
            webbrowser.open("www.youtube.com")
        elif any(item in query for item in ['open stack overflow', 'start stack overflow']):
            webbrowser.open("www.stackoverflow.com")
        elif any(item in query for item in ["open google", "start google"]):
            webbrowser.open("www.google.com")
        # elif any(item in query for item in ['music', 'song']):
        #     music_dir = r"C:\Users\akku\Music"
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs)-1)]))
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            # %I:%M:%S --> 12HourFormat, minutes, seconds specifiers
            hourIn_24Format = int(datetime.datetime.now().strftime("%H"))
            meridiem = "AM" if hourIn_24Format<12 else "PM"
            speak(f"Sir, the time is {strTime}...{meridiem}")