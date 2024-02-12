import time
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_SPEED = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_SPEED

    def create_car(self):
        chance = random.randint(1, 8)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.car_speed)
            if car.xcor() < -310:
                car.hideturtle()
                self.cars.remove(car)




