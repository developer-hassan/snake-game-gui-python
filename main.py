# Import required modules for game implementation
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create and setup a screen for game
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Create the snake, food, and scoreboard objects from their blueprints
snake = Snake()
food = Food()
score_board = Scoreboard()

# Add the event listeners on the screen to perform specific actions on a key-press
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Turn on the game to proceed
game_is_on = True
# While the game is in process
while game_is_on:
    # Update the screen with 0.1 seconds delay
    screen.update()
    time.sleep(0.1)
    # Move the snake on screen forward
    snake.move()

    # Detect collision with special food
    if food.special_diet.isvisible():
        if snake.head.distance(food.special_diet) < 15:
            score_board.special_update()
            snake.extend()
            food.hide_special_diet()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.update()
        snake.extend()
        snake.special_diet += 1
        
        # If the special diet is visible
        if food.special_diet.isvisible():
            # Then hide the special diet
            food.hide_special_diet()
        
        # Display the special diet every 5th time
        if snake.special_diet % 5 == 0:
            food.show_special_diet()


    # Detect collision with wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        score_board.game_over()

    # Detect collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
