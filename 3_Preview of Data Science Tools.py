import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


random_numbers = np.random.rand(5)
print("Random Numbers:", random_numbers)


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("Table:")
print(df)


categories = ['A', 'B', 'C']
values = [5, 7, 3]


plt.bar(categories, values, color=['red', 'blue', 'green'])


plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Basic Bar Chart')


plt.show()
