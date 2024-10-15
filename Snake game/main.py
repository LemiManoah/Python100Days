from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
segments = []

#create snake instance
snake = Snake()

#create food instance
food = Food()

#create scoreboard instance
scoreboard = Scoreboard()


#control snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    #collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -280 or snake.head.ycor() >280 or  snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    #collision with tail
    #if snake head collides with any of the other segments,  trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()