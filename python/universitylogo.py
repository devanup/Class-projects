# Name: Anup Thapa
# Email:  anup.thapa65@myhunter.cuny.edu
# Date: September 30, 2020
# This program creates a blue 'U' logo on a 30x30 grid. The 'U' is set to be 0% red, 0% green, and 100% blue

import matplotlib.pyplot as plt
import numpy as np

# creating three sheets of 30x30 array
logoImg = np.ones((30, 30, 3))

logoImg[:, :10, :2] = 0
logoImg[:, -10:, :2] = 0

logoImg[-10:, :, :2] = 0
logoImg[-10:, :, :2] = 0

# saving image as logo.png
plt.imsave("logo.png", logoImg)
