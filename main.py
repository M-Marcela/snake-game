from snake import Snake
from food import Food
from scoreboard import Score
from borders import Borders
import turtle
import time

window = turtle.Screen()
window.screensize(300, 300)
window.bgcolor("black")
window.title("My Snake Game")
window.tracer(0)

borders = Borders()
snake = Snake()
food = Food()
score = Score()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")

game_go = True
delay = 0.15
while game_go:
    window.update()
    time.sleep(delay)
    snake.move()

# Detect collision with food.
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.calculate_score()
        delay -= 0.005
        
# Detect collision with wall.
    if snake.snake_head.xcor() > 300 or snake.snake_head.xcor() <-300 or snake.snake_head.ycor() > 300 or snake.snake_head.ycor() <-300:
        game_go = False
        score.game_over()

# Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_go = False
            score.game_over()


