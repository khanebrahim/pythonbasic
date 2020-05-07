import turtle
repo=turtle.Screen()
repo.bgcolor("lightgreen")
commit=turtle.Turtle()
commit.pensize(5)
commit.color("#4B0082")
dist=50
angle=90
for _ in range(16):
    commit.forward(dist)
    commit.right(angle)
    dist=dist+10
    angle=angle-3