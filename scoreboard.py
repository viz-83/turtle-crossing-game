from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.goto(-230,230)
        self.lvl=1
        # self.update()

    def update(self):
        self.clear()
        self.write(f"Level:{self.lvl}", align="center", font=FONT)

    def level_up(self):
        self.lvl+=1
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)

