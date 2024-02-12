from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align="center")
