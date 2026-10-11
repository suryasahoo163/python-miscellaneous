#work 
'''
1.input id
2.input password
3.if right
    @ withdraw
    i.select account
        # current acount
        #saving account
            & enter your money
            ->show money
            ->reset
    @ check balance

4.if wrong
    i.paswword is wrong
    ii.reset all every thing
'''

# coding
######## importing library
import tkinter
from tkinter import *
from tkinter import messagebox
import tester,pickle
from plyer import notification
####### variables
info=""
######## functions

# first page id nad password
def f1(root):
    frm=Frame(root,bg="black")
    lx=120
    ex=lx+230
    le1y=120
    le2y=le1y+35
    wd=20
    ht=40
    wt=90
    btnx=230
    btny=200
    btn2x=btnx+120
    btn2y=btny
    Label(frm,text="WELCOME",fg="red",bg="black",font=("ariel",30,"bold")).place(y=45,x=230)
    ID=StringVar()
    PASSWORD=StringVar()
    Label(frm,text="ENTER YOUR ID",bg="black",fg="white",font=('Helvetica', 13, 'bold')).place(y=le1y,x=lx)
    Label(frm,text="ENTER YOUR PASSWORD",bg="black",fg="white",font=('Helvetica', 13, 'bold')).place(y=le2y,x=lx)
    Entry(frm,textvariable=ID,bg="black",fg="white",width=wd,insertbackground='red',font=('Helvetica', 15)).place(y=le1y,x=ex,height=23)
    Entry(frm,textvariable=PASSWORD,bg="black",fg="white",width=wd,insertbackground='red',font=('Helvetica', 15)).place(y=le2y,x=ex,height=23)
    Button(frm,text="CANCEL",fg="white",bg="black",font=("helvetica",12,"bold"),command=lambda:cancel(ID,PASSWORD)).place(x=btnx,y=btny,height=ht,width=wt)
    Button(frm,text="VERIFY",fg="white",bg="black",font=("helvetica",12,"bold"),command=lambda:verify(ID,PASSWORD)).place(x=btn2x,y=btn2y,height=ht,width=wt)
    frm.place(x=0,y=0,height=400,width=650)
    
    
    



    
def cancel(ID,PASSWORD):
    ID.set("")
    PASSWORD.set("")

def verify(ID,PASSWORD):
    found=False
    global info
    info=tester.sendrqst(ID.get()+" "+PASSWORD.get())

    if info !="False".split():
        nextpage(ID,PASSWORD,2)
    else:
        nextpage(None,None,1)
    # for i in data.account_list:
    #     if str(i)==ID.get() and data.account_list[i]==PASSWORD.get():
    #         no=2
    #         found=True
    #         nextpage(ID,PASSWORD,no)
    # if found==False:
    #     no=1
    #     nextpage(None,None,no)
    return info

def verification_error_page():
    frm=Frame(root,bg="black")
    Label(frm,text="SORRY...\n YOUR ID AND PASSWORD IS WRONG\n PLEASE TRY AGAIN...",font=(1,20,"bold"),bg="black",fg="red").place(x=60,y=100)
    Button(frm,text="TRY AGAIN",bg="black",fg="green",command=lambda:nextpage(None,None,0),font=(1,14,"bold")).place(x=260,y=220,height=50,width=130)
    frm.place(x=0,y=0,height=400,width=650)

def nextpage(id,password,no):
    global info
    for widget in root.winfo_children():
        widget.destroy()
    if no==1:
        verification_error_page()
    elif no==0:
        f1(root)
    elif no==2:
        balance_page(info)
    elif no==3:
        enter_balance()
    

def balance_page(info):
    info=list(info)
    ID=info[-1]
    # PASS=data.data[2]
    BANKNM=info[2]
    LOC=info[3]
    BAL=info[4]
    LW=info[5]
    giventext=f"BANK NAME: {BANKNM}\n{LOC}\nACCOUNT NO.: {ID}\nBALANCE: {BAL}\nLAST WITHDRAW: {LW}\n\nChoose your next step..."
    frm=Frame(root,bg="black")
    #balance frame
    Label(frm,text=giventext,bg="black",fg="white",font=("courier new",20,"bold")).place(x=0,y=0,height=250,width=650)
    ### withdraw button
    Button(frm,text="WITHDRAW",command=lambda:nextpage(None, None, 3),bg="green2",fg="firebrick1",font=("helvetica",11,"bold")).place(x=370,y=300,height=50,width=130)
    Button(frm,text="CANCEL",command=lambda:nextpage(None, None, 0),bg="green2",fg="firebrick1",font=("helvetica",11,"bold")).place(x=160,y=300,height=50,width=130)
    frm.place(x=0,y=0,height=400,width=650)


def enter_balance():
    var=StringVar()
    frm=Frame(root,bg="black")
    Label(frm,text="Enter Amount here...",bg="black",fg="red",font=("system",30,"bold")).place(x=120,y=70)
    Entry(frm,bg="black",fg="azure",textvariable=var,insertbackground='red',font=("system",20,"bold")).place(x=230,y=170,height=40,width=200)
    Button(frm,text="PROCEED",command=lambda:proceed_page(var.get(),var),bg="green2",fg="firebrick1",font=("helvetica",11,"bold")).place(x=370,y=270,height=50,width=130)
    Button(frm,text="CANCEL",command=lambda:nextpage(None, None, 0),bg="green2",fg="firebrick1",font=("helvetica",11,"bold")).place(x=160,y=270,height=50,width=130)
    frm.place(x=0,y=0,height=400,width=650)

######################################################################
def proceed_page(bal,var):
    bal=bal.strip()
    bal=int(bal)
    global info
    total=info[4]
    if bal<=total:
        notification.notify(title="Transaction successful",message=f"you got {bal} rupees from account {info[-1]}\nthank you...",timeout=10)
        total-=bal
        tester.set_account(total,bal)
        print(total)
        var.set("")
        nextpage(None, None, 0)

        
    else:
        messagebox.showinfo("error","Insufficient Balance")
        var.set("")
        

######## 





######################################################################
####### mainloop
root=Tk()
root.geometry("650x400")
# root.config(bg="black")
root.resizable(False,False)
root.title("Home ATM")

f1(root)
root.mainloop()
####### MAINLOOP CLOSED