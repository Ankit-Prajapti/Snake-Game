from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh_food()

    def refresh_food(self):
        random_x_axis = random.randint(-280, 280)
        random_y_axis = random.randint(-280, 240)
        self.goto(x=random_x_axis, y=random_y_axis)