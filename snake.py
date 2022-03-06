from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snakes()
        self.head = self.snake[0]

    def create_snakes(self):
        for position in STARTING_POS:
            self.add_block(position)

    def add_block(self, position):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(position)
        self.snake.append(block)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snakes()
        self.head = self.snake[0]

    # add block to the current snake as it eats food (make the snake bigger)
    def extend_snake(self):
        self.add_block(self.snake[-1].position())

    def move(self):
        for index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)
        self.head.forward(MOVING_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake[0].setheading(RIGHT)
