# Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
# Date: September 30, 2020
# This program prompts the user to enter number of stamps the turtle will print

import turtle

stamps = int(input("Enter number of stamps the turtle will print: "))

tom = turtle.Turtle()
tom.shape("circle")
tom.penup()  # lift the turtle pen up

steps = 20  # set the num. of steps to 20

for i in range(stamps):
    tom.stamp()
    if(i % 4 == 0):  # if the num. of loop iteration is divisible by 4 increment steps by 2
        steps += 2
    tom.forward(steps)
    tom.right(24)
