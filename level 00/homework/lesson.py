from turtle import *
color("blue")
forward(250) #im going to make a house
left(90)
forward(190)
left(90)
forward(250)
left(90)
forward(190)
#how to make a door
left(90)
forward(100)
left(90)
color("yellow")
forward(100)
right(90)
forward(65)
right(90)
forward(100)
right(90)
#how to make a roof
penup()
goto(250,190)
pendown()
color("red")
right(50)
forward(195)
left(100)
forward(195)
#how to make windows
#step one: make first window
penup()
goto(20,90)
pendown()
color("orange")
right(140)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
right(90)
forward(35)
right(90)
right(180)
forward(70)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(70)
#step two:make second window
penup()
goto(230,160)
pendown()
right(90)
right(180)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
right(90)
forward(35)
right(90)
right(180)
forward(70)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(70)
exitonclick()