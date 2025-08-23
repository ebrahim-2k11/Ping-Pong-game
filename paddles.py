from turtle import Turtle

class Paddles(Turtle):
    def __init__(self,goto):
        super().__init__()

        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        self.goto(goto)

    def goup(self):
        """to go up"""
        self.goto(self.xcor(),self.ycor()+40)
        
    def godown(self):
        """to go down"""
        self.goto(self.xcor(),self.ycor()-40)
