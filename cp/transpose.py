rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))

matrix = []
print("Enter the elements of the matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        value = float(input(f"Enter element [{i+1}][{j+1}]: "))
        row.append(value)
    matrix.append(row)

# Initialize the transpose matrix with the swapped dimensions
transpose = [[0] * rows for _ in range(cols)]

# Perform the transpose
for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

# Display the transpose of the matrix
print("Transpose of the matrix:")
for row in transpose:
    print(row)
