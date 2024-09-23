from turtle import *

width(5)
color("red")

speed(20)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)
color("green")
begin_fill()
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()


penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(120, 120)
pendown()

color("blue")
left(120)

begin_fill()
forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)
end_fill()

penup()
goto(30, 120)
pendown()

begin_fill()
forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)
end_fill()

exitonclick()