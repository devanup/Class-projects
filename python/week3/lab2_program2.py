#Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
#Date: September 22, 2020
#This program shows the shades of of red to shades of blue by moving forward 20 steps instead of 10.

import turtle #Import the turtle drawing package

turtle.colormode(255)           #Allows colors to be given as 0...255
tess = turtle.Turtle()          #Create a turtle
tess.shape("turtle")            #Make it turtle shaped
tess.backward(100)                      #Move her backwards, to give more space to draw

#For 0,10,20,...,250
for i in range(0,255,10):
     tess.forward(20)           #Move forward
     tess.pensize(i)            #changed
     tess.color(255-i,0,i)          #changed
#decrease the amount of red while increasing the amount of blue by the same amount using the loop variable
