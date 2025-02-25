import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create an array of 5 random numbers
random_numbers = np.random.rand(5)
print("Random Numbers:", random_numbers)

# Create a pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("Table:")
print(df)

# Data for the bar chart
categories = ['A', 'B', 'C']
values = [5, 7, 3]

# Create a bar chart
plt.bar(categories, values, color=['red', 'blue', 'green'])

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Basic Bar Chart')

# Display the plot
plt.show()
