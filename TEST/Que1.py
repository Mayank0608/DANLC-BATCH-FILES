import numpy as np

# Create arrays using basic functions
zeros = [0] * 10
ones = [1] * 10
fives = [5] * 10

# Combine arrays
result = np.array(zeros + ones + fives)

print("Array of 10 zeros, 10 ones, and 10 fives:")
print(result)
