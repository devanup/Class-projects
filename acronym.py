# Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
# Date: August 18, 2020
# This program prints the acronym of a phrase entered by the user

phrase = input("Enter a phrase: ")
phraseUppCase = phrase.upper()
print("Your phrase in capital letters: ", phraseUppCase)

phraseNoSpace = phraseUppCase.split(" ")
acronym = ""

for item in phraseNoSpace:
    acronym += item[0]

print(acronym)
