from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self,speed):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(1,2)
        self.setpos(random.randint(-270,270),random.randint(-250,260))
        self.speed = speed
    def move(self):
       self.setx(self.xcor()-self.speed)











