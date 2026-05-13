from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()


    def increase(self):
        self.score += 1
        self.update()
