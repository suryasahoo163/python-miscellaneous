from turtle import *
bgcolor("black")
x=1
speed(5)
color("yellow")
begin_fill()
circle(50,360)
end_fill()
color("skyblue")
shape("circle")
up()
right(90)
forward(40)
left(90)
while x<50:
	circle(x+100,360)
	x+=1
	
mainloop()