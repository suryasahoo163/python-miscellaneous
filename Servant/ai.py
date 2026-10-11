import subprocess as sp
import sys
import os, pyttsx3
import speech_recognition as sr
import pywhatkit as pkit
# features :- opens applications in you system

# intitialization
## pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",120)
engine.setProperty("volume",1)
## speach recognition
recognizer = sr.Recognizer()


# functions
def listen():
    with sr.Microphone() as source:
        audioText = recognizer.listen(source,phrase_time_limit=10)
        try:
            text = recognizer.recognize_google(audioText)
            return text.lower()
        except:
            return " "
    

def speak(msg):
    engine.say(str(msg))
    engine.runAndWait()



# test pywhatkit

pkit.start_file("chrome")
sys.exit()





# main loop
print("AI Online...")
while True:
    # loop for wakening 

    wake = listen()
  
    if "wake up" in wake:
        speak("Yes sir!")
        command = listen()
        if command == " ":
            speak("Sorry Speak Again...")
            command = listen()
        elif "exit" in command:
            break
        else:
            print(command)
    elif "exit" in wake:
        break

speak("System Closing")

sys.exit()

