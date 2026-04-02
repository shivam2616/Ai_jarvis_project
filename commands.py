import webbrowser
import datetime
import wikipedia
import pywhatkit
from speak import speak

def execute_command(command):

    command = command.lower()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "search" in command:
        command = command.replace("search", "")
        speak("Searching " + command)
        pywhatkit.search(command)

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)
        
    elif "story" in command:
        story = command.replace("story","")
        speak("Searching " + story)
        pywhatkit.search(story)
         
    elif "open instagram" in command or "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")
        
    elif "open facebook" in command  or command == "facebook":
        speak("Opening facebook")
        webbrowser.open("https://www.facebook.com")    

    elif "exit" in command:
        speak("Goodbye")
        exit()