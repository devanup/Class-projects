# Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
# Date: August 18, 2020
# This program shifts the letters in a word by 13 characters

# getting the input from the user and changing it to uppercase to use for computation
word = input("Enter a word: ").upper()
decimalVal = 0  # storing the decimal value after adding characters by +13
newDecimalVal = 0  # storing the new decimal value after determining the right value
newWord = ""  # storing the new word returned after shifting the letters by 13 characters

for c in word:
    decimalVal = ord(c)+13
    if(decimalVal > 90):
        newDecimalVal = (65 + (decimalVal - 90) - 1)
    else:
        newDecimalVal = decimalVal
    newWord += chr(newDecimalVal)

print(newWord)
