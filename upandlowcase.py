#Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
#Date: September 16, 2020
#This program prints the message typed by the user in upper case and lower case

def my_function(str):
    print(str)
    print(str.upper())
    print(str.lower())
    
my_function("Mihi cura futuri")
my_function("CSci 127")

for college in ["Hunter college","The City College of New York","Baruch College"]:
    my_function(college)
