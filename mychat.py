import tkinter
from tkinter import*


name=""
def sv():
    global name,var
    nm=var.get()
    name=nm
    print(name)
    root.destroy()
root=Tk()
root.resizable(False,False)
var=StringVar()
Label(root,text="enter your name").grid()
Entry(root,textvariable=var).grid()
Button(root,text="save",command=sv).grid()
root.mainloop()

root=Tk()
root.geometry("300x450")
root.resizable(False,False)

######## variable
variable=StringVar()



# function

def sendMsg():
    global variable,bx,name
    if len(variable.get())>0:
        bx.insert(END,name+":"+variable.get())
        import client
        client.send_msg("client: "+variable.get())
        
        variable.set("")
#msg box
scroll1=Scrollbar(root)
scroll2=Scrollbar(root,orient="horizontal")
bx=Listbox(root,yscrollcommand=scroll1.set,xscrollcommand=scroll2.set,height=23,width=46)
bx.grid(row=0,column=0)
scroll1.grid(row=0,column=1)
scroll2.grid(row=1,column=0)
scroll1.config(command=bx.yview)
scroll2.config(command=bx.xview)
Entry(root,textvariable=variable).grid()
Button(root,text="send",command=sendMsg).grid()
#root.bind(<<Enter>>,sendMsg)
root.mainloop()
#####main chat box