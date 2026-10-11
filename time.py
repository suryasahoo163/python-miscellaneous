
# importing whole module 

from tkinter import * 

from tkinter.ttk import *

  
# importing strftime function to 
# retrieve system's time 

from time import strftime 

  
# creating tkinter window 

root = Tk() 

root.title('Clock') 
root.resizable(False,False)
  
# This function is used to  
# display time on the label 

def time(): 

    string = strftime('%I:%M:%S %p') 

    lbl.config(text = string) 

    lbl.after(1000, time) 

  
# Styling the label widget so that clock 
# will look more attractive 

lbl = Label(root, font = ('calibri', 30, 'bold'), 

            background = 'red', 

            foreground = 'blue') 
Label(root,text="WATCH YOUR TIME GOOD LUCK",background="yellow",foreground="gray0").pack(fill="x")
  
# Placing clock at the centre 
# of the tkinter window 

lbl.pack(anchor = 'center') 
time() 

  
mainloop() 