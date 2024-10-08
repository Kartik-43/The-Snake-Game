from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('Data (HIGH_SCORE).txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        self.goto(0, 270)

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.score}  High Score : {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('Data (HIGH_SCORE).txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()
