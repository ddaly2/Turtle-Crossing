import time
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, is_game_on):
        super().__init__()
        #This is breaking the runtime....FIX BEFORE MOVING ON
        while is_game_on:
            time.sleep(.5)
            self.shape("square")
            self.penup()
            self.turtlesize(stretch_wid=1, stretch_len=2.5)
            self.goto(300, random.randint(-300, 300))
            self.color(random.choice(COLORS))
            self.setheading(180)
            self.move()

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)


