import time
from snake import Snake
from turtle import Screen
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

move = True
while move:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score.incres_Score()

    #collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()< -280:
        move = False
        score.game_over()

    #self collision
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
           move = False
           score.game_over()

screen.exitonclick()
