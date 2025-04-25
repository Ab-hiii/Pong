from turtle import Turtle
align = 'center'
font = ('Courier', 20, 'normal')

class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(position)
        self.show_score()
        
    def update_score(self):
        self.clear()
        self.score += 1
        self.show_score()
        
        
    def show_score(self):
        self.write(self.score,align = align, font = font)