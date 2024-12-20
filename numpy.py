import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(data)

print("\nArray after addition:")
print(data + 5)  

print("\nArray after multiplication:")
print(data * 2)  

print("\nStatistics:")
print(f"Sum: {np.sum(data)}")        
print(f"Mean: {np.mean(data)}")      
print(f"Max: {np.max(data)}")        
print(f"Min: {np.min(data)}")        

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(matrix)

print("\nAccessing Elements:")
print(f"Element at (0, 1): {matrix[0, 1]}")  
print(f"First row: {matrix[0]}")           

print("\nTransposed Matrix:")
print(matrix.T)
