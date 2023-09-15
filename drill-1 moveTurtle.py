import turtle

def drunken_Wmove():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
def drunken_Amove():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
def drunken_Smove():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
def drunken_Dmove():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(drunken_Wmove, 'w')
turtle.onkey(drunken_Amove, 'a')
turtle.onkey(drunken_Smove, 's')
turtle.onkey(drunken_Dmove, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
