# TODO : CREATE A SNAKE BODY
# TODO : MOVE THE SNAKE
# TODO : CREATE SNAKE FOOD
# TODO : DETECT COLLISION WITH FOOD
# TODO : CREATE THE SCOREBOARD
# TODO : DETECT COLLISION WITH WALL
# TODO : DETECT THE COLLISION WITH TAIL

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

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

# Class
snake = Snake()
food = Food()

# Scoreboard
scoreboard = ScoreBoard()


# Keys to Move Snake
screen.listen()

screen.onkey(key="Up", fun= snake.move_Up)
screen.onkey(key="Down", fun= snake.move_Down)
screen.onkey(key="Right", fun= snake.move_right)
screen.onkey(key="Left", fun= snake.move_left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        # print("Hit")
        food.refresh()
        scoreboard.Increase_Score()
        snake.increase_length_of_snake()
        # snake.create_snake()

#     DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_is_on = False

#    DETECT THE COLLISION WITH TAIL
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False

scoreboard.game_end()


screen.exitonclick()