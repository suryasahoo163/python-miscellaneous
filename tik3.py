import tkinter,tik_client
from tkinter import *

######################        variables/identifires          #########################
mysymbol="x"
myno=0
myid=0
turn="YOUR TURN"
gameover=False
no_of_click=0

player="Connecting"
####################              functions                #########################
######  game button click and work logic
def click(n,b):
    global no_of_click,myno,gameover,mysymbol,turn
    if b["text"]=="" and not gameover:
        if no_of_click%2==myno :
            b["text"]=mysymbol
            turn="player2"
        print(no_of_click)
    no_of_click+=1
    return no_of_click,b["text"]
#######  saving name and getting id
myname=""
def save(mynam,frm):
    global myid
    myname=mynam
    frm.destroy()
    
    tik_client.send("id")
    myid=tik_client.rcv()
    print(myname,myid)
    nextpage(myname,myid)
    
   
######## taking id and name function     
def name_enter(root):
    frm=Frame(root,bg="black")
    Label(frm,text="enter your name",bg="black",fg="white").grid()
    name=StringVar()
    Entry(frm,textvariable=name).grid()
    Button(frm,text="save and play",bg="black",fg="white",command=lambda:save(name.get(),frm)).grid()
    frm.grid()

#######  recieve player
def connect_player():
    global player
    if tik_client.rcv().isdigit():
        player=tik_client.player_id
        print(player)



######### main game function

def main_game(myname,myid):
    global root,player
    
    L=Label(root,text=f"ID:{myid}\nUSER:{myname}\n{turn}",font=(1,10),bg="black",fg="red")
    L.grid()
    L2=Label(root,text=player,bg="black",fg="white",font=(1,10))
    L2.grid()
    frm=Frame(root,width=100,height=50,bg="blue")
    b1=Button(frm,text="",width=7,height=3,fg="green",font=(2,14),command=lambda:click(1,b1))
    b1.grid(row=0,column=0)
    b2=Button(frm,text="",width=7,height=3,fg="green",font=(2,14),command=lambda:click(2,b2))
    b2.grid(row=0,column=1)
    b3=Button(frm,text="",width=7,height=3,fg="green",font=(2,14),command=lambda:click(3,b3))
    b3.grid(row=0,column=2)
    b4=Button(frm,text="",width=7,height=3,fg="green",font=(2,14),command=lambda:click(4,b4))
    b4.grid(row=1,column=0)
    b5=Button(frm,text="",width=7,height=3,fg="green",font=(2,14),command=lambda:click(5,b5))
    b5.grid(row=1,column=1)
    b6=Button(frm,text="",width=7,height=3,fg="green",font=(2,14),command=lambda:click(6,b6))
    b6.grid(row=1,column=2)
    b7=Button(frm,text="",width=7,height=3,fg="green",font=(2,14),command=lambda:click(7,b7))
    b7.grid(row=2,column=0)
    b8=Button(frm,text="",width=7,height=3,fg="green",font=(2,14),command=lambda:click(8,b8))
    b8.grid(row=2,column=1)
    b9=Button(frm,text="",width=7,height=3,fg="green",font=(2,14),command=lambda:click(9,b9))
    b9.grid(row=2,column=2)
    L.config(text=f"ID:{myid}\nUSER:{myname}\n{turn}")
    frm.grid()
    L2.config(text=player)

    root.after(100,connect_player())
def nextpage(myname,myid):
 
    print(myid)
    for widget in root.winfo_children():
        widget.destroy()
   
    main_game(myname,myid)
















############################          main            ######################################################
root=Tk()
root.configure(bg="black")


name_enter(root)


root.mainloop()