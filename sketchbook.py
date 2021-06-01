from turtle import Turtle, Screen, onkey

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)
    

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
