import pyttsx3

print("Welcome to RoboSpeaker 1.1. Created by Sonu")

while True:
    text = input("Enter what you want me to speak: ")
    if text=="q":
        break
# Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
