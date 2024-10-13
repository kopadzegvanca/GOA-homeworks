from turtle import *

#we want to paint the house

#step1: draw a square

speed(30)
width(7)
color("red")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square

#drawing a door

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of door

#drawing windows
left(30)
color("red")
forward(60)
left(90)
forward(5)
color("white")
forward(30)
color("blue")
begin_fill()
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(200,200)
pendown()

left(90)
color("red")
forward(60)
right(90)
forward(5)
color("white")
forward(30)
color("blue")
begin_fill()
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

# end of house
exitonclick()