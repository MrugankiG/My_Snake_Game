from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from boundary import Boundary
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

top_boundary = Boundary()
moving_snake = Snake()
food = Food()
scores = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(fun=moving_snake.up, key="Up")
screen.onkey(fun=moving_snake.down, key="Down")
screen.onkey(fun=moving_snake.left, key="Left")
screen.onkey(fun=moving_snake.right, key="Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    moving_snake.move()

    # collision with food
    if moving_snake.head.distance(food) < 15:
        food.refresh()
        scores.increase_score()
        moving_snake.extend_snake()

    # collision with walls
    if moving_snake.head.xcor() > 290 or moving_snake.head.xcor() < -290 or moving_snake.head.ycor() < -290 or \
            moving_snake.head.ycor() > 275:
        game_is_on = False
        scores.game_over()

    # if snake bites itself
    for segment in moving_snake.snake[1:]:
        if moving_snake.head.distance(segment) < 10:
            game_is_on = False
            scores.game_over()


screen.exitonclick()
