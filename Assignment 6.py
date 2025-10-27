# Importing the numpy library
import numpy as np

# Creating a simple array
arr1 = np.array([2, 4, 6, 8, 10])
print("Original Array:", arr1)

# Creating another array to perform operations
arr2 = np.array([1, 3, 5, 7, 9])
print("Second Array:", arr2)

# Adding two arrays
sum_arr = arr1 + arr2
print("Sum of both arrays:", sum_arr)

# Subtracting arrays
sub_arr = arr1 - arr2
print("Subtraction result:", sub_arr)

# Multiplying arrays
mul_arr = arr1 * arr2
print("Multiplication result:", mul_arr)

# Dividing arrays
div_arr = arr1 / arr2
print("Division result:", div_arr)

# Some useful NumPy functions
print("Mean of arr1:", np.mean(arr1))
print("Max value in arr2:", np.max(arr2))
print("Square root of arr1:", np.sqrt(arr1))

# Comparing with Python list (for performance understanding)
import time

# Using Python list
list1 = [i for i in range(1000000)]
start = time.time()
list_result = [x * 2 for x in list1]
end = time.time()
print("Time with Python list:", end - start)

# Using NumPy array
arr = np.arange(1000000)
start = time.time()
arr_result = arr * 2
end = time.time()
print("Time with NumPy array:", end - start)