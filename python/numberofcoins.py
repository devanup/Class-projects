# Name: Anup Thapa
# Email:  anup.thapa65@myhunter.cuny.edu
# Date: September 30, 2020
# This program prompts the user to input number of cents as an integer and it prints the amount in quarters, dimes, nickles and cents

cents = int(input("Enter the number of cents: "))

print("Quarters: ", cents//25)
cents = cents % 25
print("Dimes: ", cents//10)
cents = cents % 10
print("Nickles: ", cents//5)
cents = cents % 5
print("Pennies: ", cents//1)
