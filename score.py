from turtle import Turtle

Font = ["Courier", 24, "normal"]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.int_list = []
        with open("HighScore.txt") as f:
            for line in f:
                self.int_list.append(int(line))
        self.high_score = self.int_list[0]

        self.penup()
        self.goto(-280, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.level} High Score: {self.high_score} ", align= "left", font = Font)


    def level_up(self):
        self.level += 1
        if (self.level > self.high_score):
            self.high_score = self.level
        self.update_score()

    def game_over(self):
        self.int_list.append(self.level)
        self.int_list.sort(reverse = True)
        print(self.int_list)
        with open("HighScore.txt", mode = 'w') as f:
            for i in range(5):
                f.write(str(self.int_list[i]) + "\n")
        self.goto(-200, 0)
        self.write(f"Game Over", align="center", font=Font)
