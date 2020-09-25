#Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
#Date: August 11, 2020
#This program implements the given pseudocode

import turtle

wn = turtle.Screen()
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("purple")


for size in range(0,15):
    tess.forward(50)
    tess.left(24)

tess.left(125)

for size in range(0,15):
    tess.forward(50)
    tess.left(24)

tess.left(125)

for size in range(0,15):
    tess.forward(50)
    tess.left(24)

wn.exitonclick()
