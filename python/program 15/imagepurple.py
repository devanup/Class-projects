# Name: Anup Thapa
#Email:  anup.thapa65@myhunter.cuny.edu
# Date: September 30, 2020
# This program prompts user to input ta name of an image .png file and the name of an output file and it creates a new image that has no green channel

# Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

in_file_name = raw_input("Enter the name of the input file: ")
out_file_name = raw_input("Enter the name of the output file: ")


img1 = plt.imread(in_file_name)  # Read in file name for the image
img2 = img1.copy()  # copy img1 into variable img2 and use for manipulation
img2[:, :, 1] = 0  # setting the green channel to 0
# Save the image we created to the file: reds.png
plt.imsave(out_file_name, img2)
