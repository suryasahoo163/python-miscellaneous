import tkinter,client
from client import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
nam=""
import random
def save():
	global nam
	o=0
	nam=text.get()
	for i in nam:
		if i==" ":
			o+=1
	if len(nam)!=o:
		root.destroy()
	else:
		messagebox.showinfo("error","your name must contain alphabet ")
	text.set("")

root=Tk()

Label(root,text="Enter your name below",fg="maroon").grid()
text=StringVar()
Entry(root,textvariable=text).grid()
Button(root,text="save",command=save).grid(row=1,column=2)
root.mainloop()


#connect()






if __name__=="__main__":

    root=Tk()
    root.geometry("400x590")
    root.resizable(False,False)
    ####making of list box########
    i="hii there am using message box"
    frm=Frame(root)
    scl=Scrollbar(frm)
    scl.pack(fill="y",side="right")
    scl2=Scrollbar(frm,orient="horizontal")
    scl2.pack(fill="x",side="bottom")
###adding images#####




    def message(me,e):
	    f=Frame(root,borderwidth=2)
	    Label(f,text=me,bg="lightskyblue").pack()
	    f.pack(anchor=e)

    Label(root,text="message box",fg="gray19",wraplengt=0).pack()

    listb=Listbox(frm,yscrollcommand=scl.set,xscrollcommand=scl2.set,height=31,fg="cyan",bg="magenta3")



    listb.insert(END)
    listb.pack(fill="both")
    scl.config(command=listb.yview)
    scl2.config(command=listb.xview)
    frm.pack(fill="both")
    ft=Frame(root)
    def send():
	    yo=name.get()
	    p=0
	    for i in yo:
		    if i==" ":
			    p+=1
	    if len(yo)==p:
		    pass
	    else:
		    listb.insert(END,nam+": "+yo)
		    send_msg(nam+": "+yo)
	    name.set("")
	
    def tkdata():
	    if len(rcv())>0:
		    r=rcv()
		    listb.insert(END,"server:"+r)	
		    r=""
    tkdata()
    b=Button(ft,text="send",compound="left",fg="red2",width=10,command=send).pack(side="bottom")
    ft.pack(fill="x",side="bottom")

    name=StringVar()
    en=Entry(ft,width=25,bd=5,bg="gray",fg="white",textvariable=name).pack(side="bottom")





    root.mainloop()