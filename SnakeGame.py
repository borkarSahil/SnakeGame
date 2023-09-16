# TODO : CREATE A SNAKE BODY
# TODO : MOVE THE SNAKE
# TODO : CREATE SNAKE FOOD
# TODO : DETECT COLLISION WITH FOOD
# TODO : CREATE THE SCOREBOARD
# TODO : DETECT COLLISION WITH WALL
# TODO : DETECT THE COLLISION WITH TAIL

from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")

#           APPROACH 1
# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(x=-20,y=0)
#
# segment_3 = Turtle(shape="square")
# segment_3.goto(x=-40,y=0)
# segment_3.color("white")

#           APPROACH 2
starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []

screen.tracer(0)

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    for seg_num in range(len(segments) -1, 0, -1):     # start = 2, stop = 0, step = -1
        # In this we try to move 3rd segment to 2nd segment and 2nd segment
        # to 1st segment and then move 1st segment
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

# def move_Up():
#     new_segment.forward(10)
#
# def move_Down():
#     new_segment.backward(10)
#
# def move_right():
#     new_segment.right(90)
#
# def move_left():
#     new_segment.left(90)
#
# screen.listen()
# screen.onkey(key="w", fun=move_Up)
# screen.onkey(key="s", fun=move_Down)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="a", fun=move_left)







screen.exitonclick()