from turtle import*

#we want to paint a hous

#step 1:  draw a square
shape("turtle")

speed(30)  
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
begin_fill()

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draw a window

penup()
goto(140, 140)
pendown()

color("blue")
begin_fill()

right(150)
forward(50)

right(90)
forward(30)

right(90)
forward(50)

right(90)
forward(30)
end_fill()

#window2

color("black")

begin_fill()
penup()
goto(30, 140)
pendown()


right(90)
forward(50)

right(90)
forward(30)

right(90)
forward(50)

right(90)
forward(30)




end_fill()

exitonclick()