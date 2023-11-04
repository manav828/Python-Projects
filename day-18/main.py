from turtle import Turtle, Screen
import random

point = Turtle()
scr = Screen()
# scr.setup(500, 500)
point.speed('fastest')
point.shape('turtle')


def randcolour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    print(random_color)
    return random_color


for i in range(0, 72):
    point.color(randcolour())
    point.circle(100)
    point.left(5)

scr.exitonclick()
