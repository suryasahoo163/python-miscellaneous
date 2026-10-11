from tkinter import *
nm="player 1"
turn=0
x=("X","X","X")
y=("O","o","O")
winner=""
respond=True
##### functions
def b1c():
    global turn
    if b1["text"]=="" and winner=="":
        if turn%2==0:
            b1["text"]="X"
        elif turn%2==1:
            b1["text"]="O"
        turn+=1
    check()
def b2c():
    global turn
    if b2["text"]=="" and winner=="":
        if turn%2==0:
            b2["text"]="X"
        elif turn%2==1:
            b2["text"]="O"
        turn+=1
    check()
def b3c():
    global turn
    if b3["text"]=="" and winner=="":
        if turn%2==0:
            b3["text"]="X"
        elif turn%2==1:
            b3["text"]="O"
        turn+=1
    check()
def b4c():
    global turn
    if b4["text"]=="" and winner=="":
        if turn%2==0:
            b4["text"]="X"
        elif turn%2==1:
            b4["text"]="O"
        turn+=1
    check()
def b5c():
    global turn
    if b5["text"]=="" and winner=="":
        if turn%2==0:
            b5["text"]="X"
        elif turn%2==1:
            b5["text"]="O"
        turn+=1
    check()
def b6c():
    global turn
    if b6["text"]=="" and winner=="":
        if turn%2==0:
            b6["text"]="X"
        elif turn%2==1:
            b6["text"]="O"
        turn+=1
    check()
def b7c():
    global turn
    if b7["text"]=="" and winner=="":
        if turn%2==0:
            b7["text"]="X"
        elif turn%2==1:
            b7["text"]="O"
        turn+=1
    check()
def b8c():
    global turn
    if b8["text"]=="" and winner=="":
        if turn%2==0:
            b8["text"]="X"
        elif turn%2==1:
            b8["text"]="O"
        turn+=1
    check()
def b9c():
    global turn
    if b9["text"]=="" and winner=="":
        if turn%2==0:
            b9["text"]="X"
        elif turn%2==1:
            b9["text"]="O"
        turn+=1
    check()
def gameover():
    global winner,respond,nm
    winner="match tied"
    respond=False
def check():
    global winner,respond,turn,nm
    if turn% 2 ==0:
        nm="player 1"
    else:
        nm="player 2"
    la.configure(text=f"this is the turn of {nm}")
    if respond==True:
        if (b1["text"]==b2["text"]==b3["text"]):
            if b1["text"]=="X":
                winner="you"
            elif b1["text"]=="O":
                winner="player2"
        elif (b4["text"]==b5["text"]==b6["text"]):
            if b4["text"]=="X":
                winner="you"
            elif b4["text"]=="O":
                winner="player2"
        elif (b7["text"]==b8["text"]==b9["text"]):
            if b8["text"]=="X":
                winner="you"
            elif b8["text"]=="O":
                winner="player2"
        elif (b1["text"]==b4["text"]==b7["text"]):
            if b1["text"]=="X":
                winner="you"
            elif b1["text"]=="O":
                winner="player2"
        elif (b2["text"]==b5["text"]==b8["text"]):
            if b2["text"]=="X":
                winner="you"
            elif b2["text"]=="O":
                winner="player2"
        elif (b3["text"]==b6["text"]==b9["text"]):
            if b6["text"]=="X":
                winner="you"
            elif b6["text"]=="O":
                winner="player2"
        elif (b1["text"]==b5["text"]==b9["text"]):
            if b1["text"]=="X":
                winner="you"
            elif b1["text"]=="O":
                winner="player2"
        elif (b3["text"]==b5["text"]==b7["text"]):
            if b3["text"]=="X":
                winner="you"
            elif b3["text"]=="O":
                winner="player2"
        else:
            if b1["text"]!="" and b2["text"]!="" and b3["text"]!="" and b4["text"]!="" and b5["text"]!="" and b6["text"]!="" and b7["text"]!="" and b8["text"]!="" and b9["text"]!="" :
                gameover()
    l.configure(text=f"winner is {winner}")
    if winner!="":
        respond=False
myname="" 
def svnm(x,root):
    global myname
    root.destroy()
    myname=x
    return myname

root=Tk()

Label(root,text="enter your name").grid()
var=StringVar()
Entry(root,textvariable=var).grid()
Button(root,text="go",command=lambda:svnm(var,root)).grid()
root.mainloop()
     
root=Tk()
root.resizable(False,False)


Label(root,text=myname).grid()
connecting="connecting"
Label(root,text=connecting).grid()





l=Label(root,text=f"winner is {winner}",fg="blue")
la=Label(root,text=f"this is the turn of {nm}")
frm=Frame(root,width=100,height=50,bg="blue")
b1=Button(frm,text="",width=7,height=3,fg="green",command=b1c)
b1.grid(row=0,column=0)
b2=Button(frm,text="",width=7,height=3,fg="green",command=b2c)
b2.grid(row=0,column=1)
b3=Button(frm,text="",width=7,height=3,fg="green",command=b3c)
b3.grid(row=0,column=2)
b4=Button(frm,text="",width=7,height=3,fg="green",command=b4c)
b4.grid(row=1,column=0)
b5=Button(frm,text="",width=7,height=3,fg="green",command=b5c)
b5.grid(row=1,column=1)
b6=Button(frm,text="",width=7,height=3,fg="green",command=b6c)
b6.grid(row=1,column=2)
b7=Button(frm,text="",width=7,height=3,fg="green",command=b7c)
b7.grid(row=2,column=0)
b8=Button(frm,text="",width=7,height=3,fg="green",command=b8c)
b8.grid(row=2,column=1)
b9=Button(frm,text="",width=7,height=3,fg="green",command=b9c)
b9.grid(row=2,column=2)

l.grid()
la.grid()
frm.grid()


root.mainloop()