from turtle import*

#turtle
color("red","red")
shape("turtle")
pensize(3)

#position
penup()
goto(-10,-150)
pendown()

#heart
begin_fill()
left(140)
forward(180)
circle(-90,200)
left(120)
circle(-90,200)
forward(180)

hideturtle()
end_fill()
exitonclick()