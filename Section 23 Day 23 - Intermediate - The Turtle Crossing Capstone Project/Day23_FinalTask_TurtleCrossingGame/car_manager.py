from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, x_pos=320):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        random_y = random.randint(-250, 250)
        self.goto(x_pos, random_y)

    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE+(MOVE_INCREMENT*(level-1)))
