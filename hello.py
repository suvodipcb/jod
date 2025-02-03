import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightcyan")
turtle.speed(0)
turtle.pencolor("pink")  # Set pen color for petals

# Function to draw a petal
def draw_petal1(size, angle):
    turtle.fillcolor("mistyrose")
    turtle.begin_fill()
    turtle.circle(size, angle)
    turtle.left(180 - angle)
    turtle.circle(size, angle)
    turtle.end_fill()
    turtle.left(180 - angle)

def draw_rose(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(90)

    for i in range(12):
        draw_petal1(180, 60)

        turtle.right(30)


draw_rose(100, 20)


draw_rose(-150, 20)


def draw_text():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.pencolor("coral")
    turtle.write("Happy Rose Day 🐰🐰🐰", move=False, align="center", font=("Arial", 16, "normal"))

draw_text()


turtle.done()
