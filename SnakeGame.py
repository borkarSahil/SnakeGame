# TODO : CREATE A SNAKE BODY
# TODO : MOVE THE SNAKE
# TODO : CREATE SNAKE FOOD
# TODO : DETECT COLLISION WITH FOOD
# TODO : CREATE THE SCOREBOARD
# TODO : DETECT COLLISION WITH WALL
# TODO : DETECT THE COLLISION WITH TAIL

from turtle import Turtle, Screen
from snake import Snake
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
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    snake.move()


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