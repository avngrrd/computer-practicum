import random

m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

matrix = [[random.randint(0, 50) for _ in range(n)] for _ in range(m)]
print("Originalnaya matrix:")
for row in matrix:
    print(row)

new_matrix = [row[:] for row in matrix]

for i in range(m):
    for j in range(n):
        if i + j > n - 1:
            new_matrix[i][j] = 1

print("Modified matrix:")
for row in new_matrix:
    print(row)
