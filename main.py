from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Python Game")
screen.tracer(0)


positions = [(-10,0),(-20,0),(-30,0),(-40,0)]



sheru_gang = []
for position in positions:
    sheru = Turtle("square")
    sheru.speed(0)
    sheru.penup()

    sheru.color("white")
    sheru.goto(position)
    sheru_gang.append(sheru)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    for seru_number in range(len(sheru_gang) -1, 0, -1):
        newx = sheru_gang[seru_number - 1].xcor()
        newy = sheru_gang[seru_number - 1].ycor()
        sheru_gang[seru_number].goto(newx, newy)
    sheru_gang[0].forward(20)



screen.exitonclick()