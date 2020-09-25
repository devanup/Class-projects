#Name: Anup Thapa
#Email: anup.thapa65@myhunter.cuny.edu
#Date: September 2, 2020
#This program is : a modification of program from Section 4.3

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("hotpink")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("black")
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("lightgreen")
tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin

alex.forward(50)                 # make alex draw a pentagon
alex.left(70)
alex.forward(50)
alex.left(81)
alex.forward(50)
alex.left(67)
alex.forward(50)
alex.left(77)
alex.forward(50)
alex.left(71)

wn.exitonclick()
