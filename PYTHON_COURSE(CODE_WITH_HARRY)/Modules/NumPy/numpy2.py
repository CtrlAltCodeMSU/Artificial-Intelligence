import numpy as np

# Define the matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Select specific rows and columns
rows = np.array([0, 1, 2])
cols = np.array([2, 1, 0])

# Perform fancy indexing
fancy_indexed = matrix[rows, cols]
print("Fancy indexed result:", fancy_indexed)
