from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.teleport(0,250)
        self.color("white")
        self.write(f"Score: {self.score}",False,"center", ("Arial",15,'normal'))

    def add_score(self):
        self.score += 1

    def print_score(self):
        self.teleport(0, 250)
        self.color("white")
        self.write(f"Score: {self.score}", False, "center", ("Arial", 15, 'normal'))

    def game_over(self):
        self.teleport(0, 200)
        self.color("white")
        self.write("GAME OVER", False, "center", ("Arial", 25, 'normal'))