from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        self.score=0
        self.color("purple")
        self.penup()
        self.goto(0,2710)
        self.write(f"Score:{self.score}", align="center" , font=("Ariel, 24, normal "))
        self.hideturtle()

    def increase_score(self):
        self.score+=1
        self.write(f"Score:{self.score}", align="center", font=("Ariel, 24, normal "))