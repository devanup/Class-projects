# Name: Anup Thapa
# Email:  anup.thapa65@myhunter.cuny.edu
# Date: September 30, 2020
# This program prompts the user to enter time in seconds and converts into 12-hour time

def seconds_to_hours(raw_seconds):
    seconds = int(raw_seconds % 60)
    minutes = int((raw_seconds % 3600)/60)
    hours = int((raw_seconds % 86400)/3600)
    print(str(hours) + "h : " + str(minutes) + "m : " + str(seconds) + "s ")


raw_seconds = int(input("Please enter the time in seconds: "))
seconds_to_hours(raw_seconds)

seconds_to_hours(3600)
seconds_to_hours(59)
seconds_to_hours(0)
seconds_to_hours(60)
