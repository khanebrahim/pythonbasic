import turtle
git=turtle.Screen()
git.bgcolor("lightgreen")
github=turtle.Turtle()
github.color("blue")
github.pensize(5)

dist = 5
github.up()
for _ in range(30):
    github.stamp()
    github.forward(dist)
    github.right(24)
    dist=dist + 2
bn.exitonclick()


