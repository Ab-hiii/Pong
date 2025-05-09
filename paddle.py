from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        
        super().__init__()
        
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        

    def down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
       
        
        
        
        