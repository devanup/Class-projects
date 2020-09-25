#Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
#Date: September 22, 2020
#This program shows the shades of blue and then repeats the same loop, but backwards

import turtle #Import the turtle drawing package

turtle.colormode(255) #Allows colors to be given as 0...255
tess = turtle.Turtle() #Create a turtle
tess.shape("turtle") #Make it turtle shaped
tess.backward(100) #Move it backwards, leave more space to draw

#for 0,10,20,...,255
for i in range(0,255,10):
    tess.forward(10) #Move forward
    tess.pensize(i) #Set the drawing size to be i (larger each time)
    tess.color(0,0,i) #Set the Blue shade from 0 to 255

#for 255,245,....0
for i in range(255,0,-10):
    tess.forward(10) #Move forward
    tess.pensize(i) #Set the drawing size to be i (smaller each time)
    tess.color(0,0,i) #Set the Blue shade for 255 to 0
