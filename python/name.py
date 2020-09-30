# Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
# Date: September 29, 2020
# This program prompts the user to enter a list of names in a specific format and then formats the inputted string in a specific order and then outputs it


# Names must be entered in the following format: lastname, firstname; lastname, firstname;
sentence = input("Please enter your list of names: ")

# removing leading whitespace and then splitting names as separate elements and storing them in names as a list
names = sentence.lstrip().split("; ")

for name in range(len(names)):
    # strip whitespace from the current element and then split and get the firstname initial, then split the current element to get the lastname
    print(names[name].strip().split(", ")[1]
          [0] + ". " + names[name].split(",")[0])
# print(names[index#].split(", ")[1][0] + ". " + names[index#].split(",")[0])
