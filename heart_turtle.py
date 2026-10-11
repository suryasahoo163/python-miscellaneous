from turtle import*
pensize(4)
color('black')
begin_fill()
fillcolor("red")
left(150)
forward(180)
circle(-90,180)
setheading(60)
circle(-90,180)
forward(180)
end_fill()


penup()
forward(100)
pensize(500)
color("blue")

write("I Love You",font=("Arial", 30, "normal"))
hideturtle()
mainloop()
