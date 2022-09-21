from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def screen_function():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen_function()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        scoreboard.game_over()
        time.sleep(2)

        #restart the game if user wants
        again = input("Do you want to start again? ")
        if again == "yes":
            screen.reset()
            snake = Snake()
            food = Food()
            scoreboard = Scoreboard()
            screen_function()

        else:
            print("Good Bye!")
            game_is_on= False


    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            scoreboard.game_over()

            #restart the game if user wants
            again = input("Do you want to start again? ")
            if again == "yes":
                screen.reset()
                snake = Snake()
                food = Food()
                scoreboard = Scoreboard()
                screen_function()

            else:
                print("Good Bye!")
                game_is_on = False









screen.exitonclick()
