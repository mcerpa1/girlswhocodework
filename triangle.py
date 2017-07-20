from turtle import *
import math

# Name your Turtle.
Howard = Turtle()
Howard.penup()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
Howard.setposition(x_pos, y_pos)

### Write your code below:
Howard.begin_fill()
Howard.fillcolor("blue")
Howard.pendown()
for counter in range(3):
    Howard.right(120)
    Howard.forward(100)
Howard.penup()
Howard.end_fill()






# Close window on click.
exitonclick()
