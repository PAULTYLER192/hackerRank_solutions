import numpy as np

# Step 1: Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

#Performing addition
addition_result = A + B

#Performing element-wise multiplication
elementwise_multiplication = A * B

# Performing matrix multiplication
matrix_multiplication = np.dot(A, B)

# Transposing the addition result
transpose_result = addition_result.T

# Printing results
print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Addition Result:")
print(addition_result)

print("Element-wise Multiplication:")
print(elementwise_multiplication)

print("Matrix Multiplication:")
print(matrix_multiplication)

print("Transpose of Addition Result:")
print(transpose_result)