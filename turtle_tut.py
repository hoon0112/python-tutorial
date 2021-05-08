import turtle

t = turtle.Turtle()
t.color("blue")

def move_square():
  for i in range(4):
    t.forward(100)
    t.left(90)

move_square()
input()