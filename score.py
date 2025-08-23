from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score=0
        self.left_score=0
        self.hideturtle()
        self.penup()
        self.goto(0,210)
        self.color("white")
    
    def display_score(self):
        self.clear()
        self.write(f"Score\n {self.left_score} : {self.right_score}",align="center",font=("normal",27))

    def add_right_score(self):
        """to increase the score of the right player"""
        self.right_score+=1
        
    def add_left_score(self):
        """to increase the score of the left player"""
        self.left_score+=1