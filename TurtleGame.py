import time
from turtle import Screen
from player import Player
from Car import Cars
from score import Scoreboard


Font = ["Courier", 24, "normal"]
class turtle_game:
    def __init__(self):
        scr = Screen()
        scr.setup(width=600, height=600)
        scr.tracer(0)
        scr.title("Turtle Crossing Game")

        timmy = Player()
        new_car = Cars()
        score_board = Scoreboard()
        scr.update()
        scr.listen()

        scr.onkey(timmy.upward, "Up")
        scr.onkey(timmy.go_back, "Down")
        scr.onkey(timmy.go_right, "Right")
        scr.onkey(timmy.go_left, "Left")

        running = True
        while running:
            time.sleep(0.1)
            scr.update()

            add = new_car.create()
            new_car.start_moving()

            for car in new_car.car_list:
                if car.distance(timmy) < 20:
                    running = False
                    score_board.game_over()

            for car in new_car.car_list:
                if car.distance(timmy) <= 50 and timmy.ycor() > -280 :
                    score_board.level_up()
            if timmy.level_complete():
                timmy.start_from_begining()
                new_car.next_level()
                # score_board.level_up()

        scr.exitonclick()
