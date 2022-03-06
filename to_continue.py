from turtle import Turtle

FONT = ('Courier', 20, 'normal')


class ToContinue(Turtle):
    def __init__(self):
        super().__init__()
        self.color("light sky blue")
        self.hideturtle()
        self.penup()

    def ask_the_user(self):
        self.write("To continue, press 'enter',\n"
                   " to Quit, press 'esc'", align="center", font=FONT)

    def clear_text(self):
        self.clear()