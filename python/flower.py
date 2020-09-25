#Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
#Date: August 11, 2020
#This program uses turtle graphics to generate a flower shape

import turtle

wn = turtle.Screen()
wn.bgcolor("hotpink")

tess = turtle.Turtle()
tess.shape("turtle")
tess.pencolor('red')
tess.fillcolor('yellow')

for i in range(0,36):
    tess.forward(200)
    tess.left(170)
    tess.stamp()

wn.exitonclick()
