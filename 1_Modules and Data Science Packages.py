
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


random_numbers = np.random.rand(10)


mean_random_numbers = np.mean(random_numbers)
sum_random_numbers = np.sum(random_numbers)


print("List of random numbers:", random_numbers)
print("Mean of the numbers:", mean_random_numbers)
print("Sum of the numbers:", sum_random_numbers)


plt.plot(random_numbers)
plt.title("Simple Line Plot of Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.show()
