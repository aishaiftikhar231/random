from turtle import Screen
from snake_2 import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_2 = Snake()
food=Food()

screen.listen()
screen.onkey(snake_2.up, "Up")
screen.onkey(snake_2.down, "Down")
screen.onkey(snake_2.left, "Left")
screen.onkey(snake_2.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_2.move()
    if snake_2.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()









screen.exitonclick()