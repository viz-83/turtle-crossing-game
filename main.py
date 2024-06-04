import time
import random
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
speed=5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(player.move, "Up")

score=Scoreboard()

cars=[]
for i in range(15):
    cars.append(Car(speed))



game_continue=True
while game_continue:
    time.sleep(0.1)
    score.update()

    for car in cars:
        car.move()

    for car in cars:
        if car.xcor()<-300:
            car.setx(300)
            car.sety(random.randint(-200,200))
    if player.ycor() > 280:
        player.goto(0, -280)
        for car in cars:
            car.speed += 5
        score.level_up()


    for car in cars:
        if player.distance(car)<25:
            game = Scoreboard()
            game_continue=False
            game.game_over()
    screen.update()

screen.exitonclick()