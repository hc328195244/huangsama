import turtle
import time


turtle.setup(width=0.9, height=0.9)
turtle.bgcolor("red")
turtle.fillcolor("yellow")
turtle.color('yellow')
turtle.speed(10)
#大星
turtle.begin_fill()
turtle.up()
turtle.goto(-600, 220)
turtle.down()
for i in range(5):
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()


#第1颗
turtle.begin_fill()
turtle.up()
turtle.goto(-400, 295)
turtle.setheading(305)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.left(144)
turtle.end_fill()


#第2颗
turtle.begin_fill()
turtle.up()
turtle.goto(-350, 212)
turtle.setheading(30)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()

#第3颗
turtle.begin_fill()
turtle.up()
turtle.goto(-350, 145)
turtle.setheading(5)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()

#第4颗
turtle.begin_fill()
turtle.up()
turtle.goto(-400, 90)
turtle.setheading(300)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.left(144)
turtle.end_fill()
time.sleep(3)

