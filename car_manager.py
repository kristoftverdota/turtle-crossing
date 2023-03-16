from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.cars.append(car)

    def move_car(self):
        for cars in self.cars:
            cars.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
