from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def Game_over(self):
        self.goto(0,0)
        self.write("GAME IS OVER", align=ALIGNMENT, font=FONT)


    def increase(self):
        self.score += 1
        self.clear()
        self.update()