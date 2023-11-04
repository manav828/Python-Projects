from turtle import Turtle

STARTING_POSI = [(0,0) , (-20,0) , (-40,0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSI:
            self.add_segment(i)

    def add_segment(self,i):
        seg = Turtle('square')
        seg.color('white')
        seg.penup()
        seg.goto(i)
        self.segments.append(seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        self.segments[0].forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(270)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(0)