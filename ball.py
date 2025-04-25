from mimetypes import inited

from turtle import Turtle
out_of_bounds = False
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.move_x = 5
        self.move_y = 5
        
        
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
   
        
    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def refresh(self, side):
        self.goto(0,0)
        self.move_x = 5
        self.move_y = 5
        if side == "right":
            self.bounce_y()
        if side == "left":
            self.bounce_x()

          
        
    def inc_speed(self):
        self.move_x *= 1.6
        self.move_y *= 1.6