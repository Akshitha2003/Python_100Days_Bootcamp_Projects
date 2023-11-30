from turtle import Turtle

STARTING_X_POSITION = [0, -20, -40]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos_x in STARTING_X_POSITION:
            self.add_segment(pos_x)

    def add_segment(self, pos_x):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.setx(x=pos_x)
        self.segments.append(new_snake)

    def extend(self):
        self.add_segment(self.segments[-1].xcor())

    def move(self):
        for snake_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_num - 1].xcor()
            new_y = self.segments[snake_num - 1].ycor()
            self.segments[snake_num].setposition(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
