import turtle
import random

WIN_SIZE = 1200
FLAKE_SIZE = WIN_SIZE // 6
NUM_FLAKES = WIN_SIZE // FLAKE_SIZE
PAD = 30
STEP = FLAKE_SIZE + PAD
ORDER = 4

screen = turtle.Screen()
screen.setup(WIN_SIZE, WIN_SIZE)

pen = turtle.Turtle(visible=False)
pen.pensize(2)
screen.tracer(0, 0)  # turn off animation

def branch(length, depth):
    if depth == 0:
        pen.forward(length)
        pen.backward(length)
        return
    l = length / 3
    pen.forward(l)
    pen.left(60)
    branch(l, depth - 1)
    pen.right(120)
    branch(l, depth - 1)
    pen.left(60)
    pen.backward(l)

def snowflake(cx, cy, size, depth=ORDER):
    pen.penup()
    pen.goto(cx, cy)
    pen.pendown()
    for k in range(6):
        pen.setheading(k * 60)
        branch(size, depth)

random.seed()
for x in range(-WIN_SIZE//2+STEP//2, WIN_SIZE//2, STEP):
    for y in range(-WIN_SIZE//2+STEP//2, WIN_SIZE//2, STEP):
        snowflake(x, y, FLAKE_SIZE)

screen.exitonclick()
