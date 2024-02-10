import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
garage = CarManager(game_is_on)
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 280:
        scoreboard.level_up()
        player.restart()

screen.exitonclick()