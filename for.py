import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()# create a turtle named alex
n=10
h=70
szog=360/n
for i in range(n):
    alex.forward(h)           # tell alex to move forward by 150 units
    alex.left(szog)
