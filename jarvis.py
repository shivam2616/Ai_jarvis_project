from speak import speak
from listen import listen
from commands import execute_command

speak("Hello I am Jarvis")

while True:

    command = listen()

    if command:
        execute_command(command)