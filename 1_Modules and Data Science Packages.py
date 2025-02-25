# Import the necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Use NumPy to create a list of 10 random numbers
random_numbers = np.random.rand(10)

# Calculate the mean and sum of these numbers
mean_random_numbers = np.mean(random_numbers)
sum_random_numbers = np.sum(random_numbers)

# Print the list of random numbers, their mean, and their sum
print("List of random numbers:", random_numbers)
print("Mean of the numbers:", mean_random_numbers)
print("Sum of the numbers:", sum_random_numbers)

# Use Matplotlib to plot a simple line graph of these numbers
plt.plot(random_numbers)
plt.title("Simple Line Plot of Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.show()
