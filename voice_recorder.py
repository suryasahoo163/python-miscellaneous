import tkinter 
from tkinter import *
import pygame.mixer,pyttsx3,wikipedia

### initializing
engine=pyttsx3.init()
engine.setProperty('volume', 1)
engine.setProperty("rate", 200)
#variables
clr="gray"
data=''
clrfg="white"
msg="hellow sir, how can i help you plz say!"
txt="voice API"
#function
def speak(msg):
    engine.say(msg)
    engine.runAndWait()

def search(que):
    global data
    data=wikipedia.summary(que,sentences=10)
    print (data)
def do():
    speak(data)

 
 
 
root=Tk() 
var=StringVar()
root.geometry("300x100")
root.resizable(False,False)
root.config(bg=clr)

l1=Label(root,text=txt,bg=clr,fg=clrfg,font=(30))
l1.pack(side="top")
ent=Entry(root,text=var,bg=clr,width=30)
ent.pack()
bn=Button(root,text="search",bg=clr,fg=clrfg,command=lambda:search(var.get()))
bn.pack()
Button(root,text="READ LOUD",bg=clr,border=0,fg=clrfg,command=do).pack(side="bottom")



root.mainloop()