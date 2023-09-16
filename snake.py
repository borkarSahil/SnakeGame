from turtle import Turtle

# CONSTANTS
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.length = len(self.segments)

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start = 2, stop = 0, step = -1
            # In this we try to move 3rd segment to 2nd segment and 2nd segment
            # to 1st segment and then move 1st segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def increase_length_of_snake(self):
        x_cor = self.segments[self.length - 1].xcor()
        y_cor = self.segments[self.length - 1].ycor()
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x_cor, y_cor)
        self.segments.append(new_segment)
