import tkinter
from tkinter import *
import socket
#identifires
skt=None
globalX=0
globalY=0
placex=170
placey=0
placexx=20
#function sector
def replace():
    global myVar
    return myVar.set("")
def send():
    global myVar,placex,placey
    sendmsg()
    placey+=30
    Label(root,text=myVar.get(),bg="green",fg="red").place(x=placex,y=placey)
    
    replace()
    return placey
def connect_to_server(port):
    global skt
    skt=socket.socket()
    skt.connect(("localhost",port))
    return skt
def sendmsg():
    global myVar,skt
    msg=myVar.get()
    skt.send(bytes(msg,"utf-8"))
    
def recievemsg():
    global skt,placexx,placey
    rc=skt.recv(1024).decode()
    placey+=30
    Label(root,text=rc,bg="green",fg="red").place(x=placexx,y=placey)
    print(rc)
    return placey

   

connect_to_server(19009)

    


root=Tk()
root.after(1000,recievemsg)
myVar=StringVar()
root.geometry("300x450")
root.resizable(False,False)
Canvas(root,width=10,bg="black",height=450).place(x=0,y=0)
Canvas(root,width=300,bg="black",height=10).place(x=0,y=0)
Canvas(root,width=10,bg="black",height=450).place(x=290,y=0)
Canvas(root,width=300,bg="black",height=10).place(x=0,y=440)
entry=Entry(root,textvariable=myVar,width=30)
entry.place(y=420,x=15)
Button(root,text="X",command=replace,height=0,border=0,width=2).place(y=418,x=202)
Button(root,text="send -->",command=send,border=0).place(x=230,y=418)

# placing messaages in interface



root.mainloop()