import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(5)

def draw_rect(color, y):
    t.penup()
    t.goto(-200, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

draw_rect("orange", 100)
draw_rect("white", 50)
draw_rect("green", 0)

# Ashoka Chakra
t.penup()
t.goto(0, 25)
t.color("blue")
t.pendown()
t.circle(25)

for i in range(24):
    t.penup()
    t.goto(0, 25)
    t.setheading(i * 15)
    t.forward(25)
    t.pendown()
    t.forward(10)

t.hideturtle()
screen.mainloop()
