from turtle import*
speed(0)
penup()
setx(-150)
pendown()
begin_fill()
color("black","red")
left(90)
def half():
    c = 0
    while(c<180):
        forward(2)
        right(1)
        c = c+1
half()
right(180)
half()
right(45)
forward(325)
right(90)
forward(325)
hideturtle()
end_fill()
done()