from turtle import Turtle
import random

# color list so that everytime the color of the food is different
FOOD_COLOR = ["deep pink", "coral", "crimson", "dark olive green", "magenta", "violet", "medium violet red",
              "aquamarine", "blue", "pale green", "yellow", "light sky blue", "salmon", "pink", "orange", "orchid",
              "indigo", "dark green", "brown"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(FOOD_COLOR))
        x_range = random.randint(-280, 280)
        y_range = random.randint(-280, 265)
        self.goto(x_range, y_range)
