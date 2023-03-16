import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

    for car in cars.cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    if player.finish():
        player.go_back()
        cars.level_up()
        scoreboard.level_up()

screen.exitonclick()
