from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.my_speed=1
        self.speed(self.my_speed)

    
    def set_ball(self):
        """return to 0,0"""
        self.goto(0, 0)
        

    def increase_speed(self):
        self.x_move *= 1.2
        self.y_move *= 1.2