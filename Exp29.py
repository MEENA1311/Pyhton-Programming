import turtle

t = turtle.Turtle()
t.speed(5)

# House body
t.penup()
t.goto(-50, -50)
t.pendown()
t.color("blue")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()

# Roof
t.color("yellow")
t.begin_fill()
t.goto(-50, 50)
t.goto(0, 100)
t.goto(50, 50)
t.goto(-50, 50)
t.end_fill()

# Door
t.penup()
t.goto(-10, -50)
t.pendown()
t.color("white")
t.begin_fill()
for _ in range(2):
    t.forward(20)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()

# Lamp post
t.penup()
t.goto(60, -50)
t.pendown()
t.color("black")
t.pensize(3)
t.goto(60, 60)
t.penup()
t.goto(60, 60)
t.dot(20, "yellow")

# Flag
t.penup()
t.goto(60, 40)
t.pendown()
t.color("blue")
t.begin_fill()
for _ in range(2):
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.right(90)
t.end_fill()

t.hideturtle()
turtle.done()
