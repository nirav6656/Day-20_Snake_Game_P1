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
    # sheru.speed(0)
    sheru.penup()

    sheru.color("white")
    sheru.goto(position)
    sheru_gang.append(sheru)

game_on = True
while game_on:
    screen.update()
    for new_sheru in sheru_gang:
        new_sheru.forward(10)
        time.sleep(1)







screen.exitonclick()