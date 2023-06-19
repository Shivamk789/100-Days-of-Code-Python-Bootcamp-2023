from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x_ran = random.randint(-288, 288)
        y_ran = random.randint(-288, 288)
        self.goto(x_ran, y_ran)




