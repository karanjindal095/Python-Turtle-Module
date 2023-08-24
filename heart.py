from turtle import*
bgcolor("white")
# create turtle instance
shape("turtle")
color("red")
fillcolor("red")
pensize(3)

# position the turtle
penup()
goto(0,-150)
pendown()

# draw the heart shape
begin_fill()
bgcolor("black")
left(140)
forward(224)
def loop():
 for i in range(200):
    right(1)
    forward(2)
loop()
left(120)
loop()
forward(224)
end_fill()

# hide the turtle
hideturtle()

# exit the program on user click on screen 
exitonclick()



