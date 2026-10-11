#text editor
import tkinter
from tkinter import *
from tkinter import ttk, font
root=Tk()
#scroll bar
sc=Scrollbar(root)
font=font.families()



num=IntVar()
val=StringVar()
cmb=ttk.Combobox(root,textvariable=val,state="readonly")
cmb["values"]=(font)
cmb.current(0)
cmb.pack(anchor="nw")
cm=ttk.Combobox(root,textvariable=num,state="readonly")
cm["values"]=[x for x in range(4,80,2)]
cm.current(0)
cm.pack(anchor="nw")
tp=StringVar()
#cmb=ttk.Combobox(root,textvariable=tp)
#cmb["values"]=()
#cmb.pack(anchor="nw")
#def fl(v,nm):
#	return txt.configure(font=(v,str(nm),"normal"))
Label(root,text="text editor for you").pack()

txt=Text(root,height=38)
txt.configure(yscrollcommand=sc.set)
sc.config(command=txt.yview)
sc.pack(side="right",fill="y")

txt.pack()

def col():
	return txt.configure(fg="blue")
def col1():
	return txt.configure(fg="green")
def col2():
	return txt.configure(fg="yellow")
def col3():
	return txt.configure(fg="red")
def col4():
	return txt.configure(fg="gray")
def col5():
	return txt.configure(fg="pink")


def bcol():
	return txt.configure(bg="blue")
def bcol1():
	return txt.configure(bg="green")
def bcol2():
	return txt.configure(bg="yellow")
def bcol3():
	return txt.configure(bg="red")
def bcol4():
	return txt.configure(bg="gray")
def bcol5():
	return txt.configure(bg="pink")

menu=Menu(root)
menu1=Menu(menu)


menu1.add_command(label="blue",command=col)
menu1.add_command(label="green",command=col1)
menu1.add_command(label="yellow",command=col2)
menu1.add_command(label="red",command=col3)
menu1.add_command(label="gray",command=col4)
menu1.add_command(label="pink",command=col5)
menu.add_cascade(label="font colour",menu=menu1)

menu2=Menu(menu)


menu2.add_command(label="blue",command=bcol)
menu2.add_command(label="green",command=bcol1)
menu2.add_command(label="yellow",command=bcol2)
menu2.add_command(label="red",command=bcol3)
menu2.add_command(label="gray",command=bcol4)
menu2.add_command(label="pink",command=bcol5)
menu.add_cascade(label="background",menu=menu2)
root.config(menu=menu)
#text edit
nm=4
vl="ariel"
def change(root):
	global val,num,nm,vl
	nm=num.get()
	vl=val.get()
	txt.configure(font=(vl,nm))
cmb.bind('<<ComboboxSelected>>',change)
cm.bind('<<ComboboxSelected>>',change)

root.mainloop()