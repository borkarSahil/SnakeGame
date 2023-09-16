from turtle import Turtle, Screen

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(0, 250)
        self.score = 0
        self.display_score()

    def Increase_Score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_end(self):
        self.clear()
        self.setposition(0, 0)
        self.write(arg=f"Game End ! Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)
