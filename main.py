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
garage = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    garage.create_car()
    garage.move_cars()
    if player.ycor() > 280:
        scoreboard.level_up()
        player.restart()
        garage.car_speed += 5
    for car in garage.cars:
        if player.distance(car) < 30 and abs(player.ycor() - car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()