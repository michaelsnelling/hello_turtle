import turtle
import random

canvas = turtle.Canvas()

gang = []
for x in range(5):
    gang.append(turtle.Turtle())
    gang[x].shape("turtle")

# change all the turtles' color
for x in range (5):
    gang[x].color("purple")

# move all the turtles to a random spot
for mike in gang:
    mike.goto(random.randint(-200, 200), random.randint(-200,200))





input("Press enter to quit")