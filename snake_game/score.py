from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('arial' , 24, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreBoard()
    def incres_Score(self):
        self.score +=1
        self.clear()
        self.update_scoreBoard()

    def update_scoreBoard(self):
        self.write(f'Score = {self.score}', align=ALIGNMENT , font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f' Game Over', align=ALIGNMENT , font=FONT)




