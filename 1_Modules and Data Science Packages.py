
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


random_numbers = np.random.randint(10, size=10)




mean_random_numbers = np.mean(random_numbers)
sum_random_numbers = np.sum(random_numbers)


print("List of random numbers:", random_numbers)
print("Mean of the numbers:", mean_random_numbers)
print("Sum of the numbers:", sum_random_numbers)


plt.plot(random_numbers)
plt.title("Line graph of random numbers")
plt.xlabel("Random number X Axis")
plt.ylabel("Random Number Y Axis")
plt.show()
