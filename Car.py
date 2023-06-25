import turtle
from turtle import Turtle
import random

car_color = ["red", "orange", "yellow", "green", "blue", "purple"]
moving_speed = 5
moving_increment = 10
choice = 6

class Cars:
    def __init__(self):
        self.car_list = []
        self.car_speed = moving_speed

    def create(self):
        if random.randint(1,4) == 1:
            new_created = Turtle()
            new_created.shape("square")
            new_created.shapesize(stretch_wid = 1, stretch_len = 2)
            new_created.penup()
            nw_clr = random.choice(car_color)
            new_created.color(nw_clr)

            new_created.goto(280 , random.randint(-250, 260))
            self.car_list.append(new_created)

    def start_moving(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def next_level(self):
        self.car_speed += moving_increment