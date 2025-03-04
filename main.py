import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor('yellow')
t = turtle.Turtle()
t.setheading(135)
#square
t.penup()
t.goto(0,0)
t.pendown()
t.fillcolor("cyan")
t.begin_fill()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t.setheading(45)
#square
t.penup()
t.goto(0,0)
t.pendown()
t.fillcolor("brown")
t.begin_fill()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()


turtle.done()