from turtle import Turtle

X_COR = -300
Y_COR = 270
SCREEN_SIZE = 600

# line to separate the score text and the screen
class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(X_COR, Y_COR)
        self.hideturtle()
        self.pendown()
        self.forward(SCREEN_SIZE)

