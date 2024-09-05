from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.list_ekans = []
        self.create_snake()
        self.head = self.list_ekans[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_ekans(position)

    def add_ekans(self,position):
        ekans = Turtle("square")
        ekans.color("green")
        ekans.penup()
        ekans.goto(position)
        self.list_ekans.append(ekans)

    def move_snake(self):
        for i in range(len(self.list_ekans) - 1, 0, -1):
            new_x = self.list_ekans[i - 1].xcor()
            new_y = self.list_ekans[i - 1].ycor()
            self.list_ekans[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_ekans(self.list_ekans[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
