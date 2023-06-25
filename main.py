from tkinter import *
from TurtleGame import turtle_game

FONT = ("Courier", 24, "normal")

root = Tk()
root.title("Turtle Game")
root.geometry("600x600")


def turtle_game_start():
    new_game = turtle_game()
def show_high_score():
    show_sores.pack(pady=20)


turtle_game_button = Button(root, text="Turtle Game", command=turtle_game_start, fg="blue", font=FONT)
High_score_button = Button(root, text = "High Score",command = show_high_score, fg="blue", font=FONT)
with open("HighScore.txt") as f:
    content = f.read()

show_sores = Label(root, text = content, font = FONT)
turtle_game_button.pack()

High_score_button.pack()

root.mainloop()


