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
        self.high_score = 0
        self.score = 0
        self.display_score()

    def Increase_Score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}  High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display_score()

    # def game_end(self):
    #     self.clear()
    #     self.setposition(0, 0)
    #     self.write(arg=f"Game End ! Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)
