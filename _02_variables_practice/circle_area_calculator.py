import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # circle = 123
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    radius = simpledialog.askinteger(title = "circle guy", prompt= "radius in pixels")
    # Make a new turtle
    turtle.turtles()
    turtle.speed(0)
    # Have your turtle draw a circle with the correct radius
    turtle.circle(radius)

    # Call the turtle .penup() method
    turtle.penup()
    # Move your turtle to a new x,y position using .goto()
    turtle.goto(0,131)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    math.pi
    # Write the area of your circle using the turtle .write() method
    turtle.write(arg="area = " + str(radius), move=True, align='left', font=('Arial',8,'normal'))
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    #hideturtle()
    # Call turtle.done()
    turtle.done()
