import matplotlib.pyplot as plt

# Sample data
x = [10, 5, 11, 8, 18]
y = [0, 3, 5, 10, 9]

# Create a plot
plt.plot(x, y, color='magenta', marker='3', linestyle='-')

# Add labels to the x-axis and y-axis
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Change the title of the plot
plt.title('Testing out graph')

# Display the plot
plt.show()

#An interesting thing I learned playing around with matplotlib is the ease of changing the colors of the line and different line styles.
#Another interesting thing is how easy it is to make sense of the code for it since it's using a simple code format for X and Y axis 
#information.
#
#
#
