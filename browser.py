import tkinter
from tkinter import *

from googlesearch import search
height=500
width=800

# function sector
def change_page(root,page):
    for win in root.winfo_children():
        win.destroy()
    if page==0:
        main_page()
    if page==1:
        page2()

def on_mainClick(srch):
    data=srch.get()
    try :
        ob=search(data)
    except:
        print("turn on ur internet connection")
    for i in ob:
        print(i)
    


def main_page():
    frm=Frame(root,bg="black")
    Label(frm,text="Surya Browser",font=(2,25,"bold"),bg="black",fg="red").place(x=300,y=120)
    srch=StringVar()
    src=Entry(frm,textvariable=search,fg="white",bg="black",font=(10))
    src.place(height=30,width=400,x=220,y=180)
    click=Button(frm,text="Search",bg="black",fg="green",font=(9),command=lambda:on_mainClick(srch))
    click.place(x=630,y=180,height=32)
    frm.place(x=0,y=0,height=height,width=width)


def page2():
    frm=Frame(root,bg="black")
    src=Entry(frm,textvariable=search,fg="white",bg="black",font=(10))
    src.place(height=30,width=400,x=220,y=180)
    click=Button(frm,text="Search",bg="black",fg="green",font=(9))
    click.place(x=630,y=180,height=32)
    frm.place(x=0,y=0,height=height,width=width)
    
  









root=Tk()
root.title("surya browser")
root.config(bg="red")
root.resizable(False,False)
root.geometry(f"{width}x{height}")
change_page(root,0)
root.mainloop()



