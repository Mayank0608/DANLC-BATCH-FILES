import numpy as np
import matplotlib.pyplot as plt

# Given data
square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

# Create scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(square_footage, selling_prices, color='b', marker='o', label='Data Points')

# Fit a trend line
m, b = np.polyfit(square_footage, selling_prices, 1)
plt.plot(square_footage, m * square_footage + b, color='r', linestyle='--', label='Trend Line')

# Labels and title
plt.xlabel("Square Footage")
plt.ylabel("Selling Price (in $1000s)")
plt.title("House Size vs Selling Price")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Conclusion
print(f"The trend line suggests a positive correlation between square footage and selling price. ")
print(f"This means larger houses tend to have higher selling prices in this neighborhood.")
