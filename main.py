from turtle import Screen
import time

from scoreboardbrain import Scoreboard
from snakebrain import Snake
from foodbrain import Food


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Ekans")
screen.tracer(0)

ekans = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(ekans.up, "Up")
screen.onkey(ekans.down, "Down")
screen.onkey(ekans.left, "Left")
screen.onkey(ekans.right, "Right")


game_is_on=True
while game_is_on:
    score.print_score()
    screen.update()
    time.sleep(0.1)
    ekans.move_snake()

    #Detect Food Collision
    if ekans.head.distance(food) <15:
        food.refresh()
        ekans.extend()
        score.clear()
        score.add_score()

    if ekans.head.xcor() >280 or ekans.head.ycor() >280 or ekans.head.xcor() <-280 or ekans.head.ycor() <-280:
        score.game_over()
        game_is_on = False

    for i in ekans.list_ekans[1:]:
        if ekans.head.distance(i)<10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
