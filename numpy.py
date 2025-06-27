import numpy as np

# Creating NumPy arrays from list
my_list = [1, 2, 3]
arr1 = np.array(my_list)
print("Array from list:", arr1)

# 2D Array (Matrix)
my_matrix = [[1, 2, 3], [4, 5, 6]]
arr2d = np.array(my_matrix)
print("\n2D Matrix:\n", arr2d)

# Indexing rows in any order
arr2d = np.array([[i]*10 for i in range(10)])
print("\nSelected Rows (2,4,6,8):\n", arr2d[[2, 4, 6, 8]])
print("Selected Rows (6,4,2,7):\n", arr2d[[6, 4, 2, 7]])

# Boolean indexing
arr = np.arange(1, 11)
print("\nOriginal Array:\n", arr)
bool_arr = arr > 4
print("Boolean Array (arr > 4):\n", bool_arr)
print("Filtered Values (arr > 4):\n", arr[bool_arr])
print("Filtered Values (arr > 2):\n", arr[arr > 2])
x = 2
print(f"Filtered Values (arr > {x}):\n", arr[arr > x])

# NumPy Operations
arr = np.arange(10)  # 0 to 9
print("\narr / arr:\n", arr / arr)       # Warning: 0/0 is nan
print("1 / arr:\n", 1 / arr)             # Warning: 1/0 is inf
print("arr ** 3:\n", arr**3)             # Cube of elements

# Universal Array Functions
print("\nnp.sqrt(arr):\n", np.sqrt(arr))         # Square root
print("np.exp(arr):\n", np.exp(arr))             # Exponential (e^x)
print("np.max(arr):", np.max(arr))               # Max value
print("np.sin(arr):\n", np.sin(arr))             # Sine values
print("np.log(arr):\n", np.log(arr))             # Logarithm
