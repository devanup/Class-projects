# Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
# Date: September 30, 2020
# This program prompts the user for 6-digit hex number input and uses it to stamp a turtle of that color

import turtle

number = input("Please enter a 6-digit Hexadecimal number: ")
color = "#" + number

thea = turtle.Turtle()
thea.shape("turtle")
thea.color(color)
thea.stamp()


# turtle.done()
