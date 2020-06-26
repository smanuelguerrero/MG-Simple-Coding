import turtle

turtleone = turtle.Turtle()

turtle.speed(200)

def square():
    turtleone.forward(100)
    turtleone.right(90)
    turtleone.forward(100)
    turtleone.right(90)
    turtleone.forward(100)
    turtleone.right(90)
    turtleone.forward(100)

def squaretwo():
    turtleone.left(180)
    turtleone.forward(200)

def squarethree():
    turtleone.right(180)
    turtleone.forward(400)
    
for count in range(4):
    square()

for tortuga in range(1):
    squaretwo()

for count in range(4):
    square()

for zolwik in range(1):
    squarethree()

for count in range(4):
    square()

for tortuga in range(1):
    squaretwo()





