from turtle import Turtle

str_pos = (0, -280)
dis_inc = 10
Finish_line = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(str_pos)
        self.setheading(90)

    def start_from_begining(self):
        self.goto(str_pos)
    def upward(self):
        self.forward(dis_inc)

    def go_back(self):
        self.backward(dis_inc)

    def go_right(self):
        self.right(10)

    def go_left(self):
        self.left(10)

    def level_complete(self):
        if self.ycor() >= 280:
            return True
        else:
            return False
