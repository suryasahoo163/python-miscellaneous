#calculator
import tkinter 
from tkinter import*

n=5
m=10
an=""
ans=""
root=Tk()
var=StringVar()
Label(root,text="calculator",fg="lightsteelblue1",bg="lightsteelblue1").grid(row=0,column=0)
pa=Entry(root,textvariable=var,bg="ghost white",fg="gray10").grid(row=1,column=1)
f=Frame(root,bg="lightsteelblue1")
root.configure(bg="lightsteelblue1")
Label(root,text="CALCULATOR",bg="lightsteelblue1",fg="green4").grid(row=0,column=1)
def calc():
	global ans,an
	ans=eval(ans)
	ans=str(ans)
	var.set(ans)

def a1():
	global ans
	ans+="1"
	var.set(ans)
def a2():
	global ans
	ans+="2"
	var.set(ans)
def a3():
	global ans
	ans+="3"
	var.set(ans)
def a4():
	global ans
	ans+="4"
	var.set(ans)
def a5():
	global ans
	ans+="5"
	var.set(ans)
def a6():
	global ans
	ans+="6"
	var.set(ans)
def a7():
	global ans
	ans+="7"
	var.set(ans)
def a8():
	global ans
	ans+="8"
	var.set(ans)
def a9():
	global ans
	ans+="9"
	var.set(ans)
def a0():
	global ans
	ans+="0"
	var.set(ans)
def aa():
	global ans
	ans+="+"
	var.set(ans)
def an():
	global ans
	ans+="-"
	var.set(ans)
def am():
	global ans
	ans+="*"
	var.set(ans)
def ad():
	global ans
	ans+="/"
	var.set(ans)
def ac():
	global ans,var
	ans=""
	var.set("")
def ab():
	global ans
	ans=ans[:-1:]
	var.set(ans)
Button(f,text="+",command=lambda:aa("+")).grid(row=m+1,column=n+2)
Button(f,text="×",command=am).grid(row=m+2,column=n+1)
Button(f,text="=",command=calc).grid(row=m+2,column=n+2)
Button(f,text="/",command=ad).grid(row=m+2,column=n+3)
Button(f,text="-",command=an).grid(row=m+3,column=n+2)
Button(f,text="1",command=a1).grid(row=m+4,column=n+1)
Button(f,text="2",command=a2).grid(row=m+4,column=n+2)
Button(f,text="3",command=a3).grid(row=m+4,column=n+3)
Button(f,text="4",command=a4).grid(row=m+5,column=n+1)
Button(f,text="5",command=a5).grid(row=m+5,column=n+2)
Button(f,text="6",command=a6).grid(row=m+5,column=n+3)
Button(f,text="7",command=a7).grid(row=m+6,column=n+1)
Button(f,text="8",command=a8).grid(row=m+6,column=n+2)
Button(f,text="9",command=a9).grid(row=m+6,column=n+3)
Button(f,text="0",command=a0).grid(row=m+7,column=n+2)
Button(f,text="c",command=ac).grid(row=m+7,column=n+3)
Button(f,text="<-",command=ab).grid(row=m+7,column=n+1)
f.grid(row=2,column=1)
#####commands#######


root.mainloop()