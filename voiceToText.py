import speech_recognition as sr

recogniser=sr.Recognizer()
def audio_input():
        with sr.Microphone() as source:
                print("speak:")
                audio=recogniser.listen(source)
        #recognising the audio
        try:
                text=recogniser.recognize_google(audio)
        except:
                text = "Sorry i cant understand you!!!"
                pass
        print(text)
        

def listen():
        msg["text"]="speak:"
        audio_input()
       





import tkinter as tk


root = tk.Tk()
root.geometry("300x400")
root.resizable(False,False)
header = tk.Label(root,text="welcome to voice recoginiser!",font=("Arial",15))
header.pack(pady=40)
msg = tk.Button(root,text="Speak",font=("New Times Roman",18),fg="green",border=0,command=listen)
msg.pack(pady=80)

root.mainloop()