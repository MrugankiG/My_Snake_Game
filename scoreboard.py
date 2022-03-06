from turtle import Turtle

SCORE_POSITION = 'center'
FONT = ('Courier', 18, 'normal')
GAME_OVER_FONT = ('Courier', 30, 'normal')
Y_COR = 270


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, Y_COR)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 270)
        self.write(f"Score:{self.score}", font=FONT)
        self.goto(100, 270)
        self.write(f"High Score:{self.high_score}", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=SCORE_POSITION, font=GAME_OVER_FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

