from Snake import Snake
from turtle import Screen
import time
from food import Food
from score_board import ScoreBoard

#                                                setting Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
screen.tracer(0)
screen.listen()

#                                              Setting Snake & Food

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food...

    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall...

    if snake.head.xcor() > 292 or snake.head.xcor() < -292 or snake.head.ycor() > 292 or snake.head.ycor() < -292:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail...

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
