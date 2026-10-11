import tkinter
from tkinter import *
from tkinter import messagebox
root=Tk()
a="hii iam surya and its my new GUI"
def at():
	messagebox.showinfo("save","your file is successfully saved")
def ot():
	messagebox.showinfo("enter","enter your file below")
def it():
	messagebox.showinfo("exit","your file is ready to exit")
def ut():
	messagebox.showinfo("reset","your file is successfully reseted")	
q=Label(root, text=a,bg="grey",fg="maroon")
q.pack(anchor="nw")
m=Menu(root)
m1=Menu(m)
m1.add_command(label="save" ,command=at)
m1.add_command(label="enter",command=ot)
m1.add_command(label="exit",command=it)
m1.add_command(label="reset",command=ut)
m.add_cascade(label="file",menu=m1)
m2=Menu(m)
m2.add_command(label="power cell")
m2.add_command(label="info")
m2.add_command(label="making gui")
m2.add_command(label="exit")
m.add_cascade(label="help",menu=m2)

root.config(menu=m)
l=Frame(root,bg="grey").pack(anchor="nw",fill=X)
z=101
h=1300
can=Canvas(root,width=z,height=h,bg="red")
can.pack(side="left")
can=Canvas(root,width=z,height=h,bg="blue")
can.pack(side="left")
can=Canvas(root,width=z,height=h,bg="green")
can.pack(side="left")
can=Canvas(root,width=z,height=h,bg="black")
can.pack(side="left")
can=Canvas(root,width=z,height=h,bg="yellow")
can.pack(side="left")
can=Canvas(root,width=z,height=h,bg="pink")
can.pack(side="left")
can=Canvas(root,width=z,height=h,bg="purple")
can.pack(side="left")

root.mainloop()