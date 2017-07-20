from turtle import *
import math

# Name your Turtle.
Walter = Turtle()
Walter.penup()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
Walter.setposition(x_pos, y_pos)

### Write your code below:
Walter.begin_fill()
Walter.fillcolor("aquamarine1")
Walter.pendown()
for counter in range(4):
    Walter.right(90)
    Walter.forward(20)
Walter.penup()
Walter.end_fill()





# Close window on click.
exitonclick()
