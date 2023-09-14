from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,x_coordinates):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(x_coordinates, y = 0)
        self.setheading(90)
        self.shapesize(stretch_len= 5.0)

    def up(self):
        new_y = self.ycor() +20
        self.goto(x = self.xcor(), y = new_y )
    def down(self):
        new_y = self.ycor()-20
        self.goto(x = self.xcor(), y = new_y)