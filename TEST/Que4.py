#Convert a List and Tuple into Arrays

import numpy as np

my_list = [9, 8, 3, 6, 2, 6, 7, 8]
my_tuple = ([5, 4, 2], [1, 2, 3])

# Convert to arrays using np.array()
list_array = np.array(my_list)
tuple_array = np.array(my_tuple)

print("List converted into array:")
print(list_array)
print("\nTuple converted into array:")
print(tuple_array)
