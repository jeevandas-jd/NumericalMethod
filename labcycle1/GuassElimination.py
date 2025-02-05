import numpy as np


def gauss_jordan_elimination(A, B):
    n = len(B)

    # Forward Elimination & Making Diagonal Elements 1
    for i in range(n):
        # Partial Pivoting
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            B[[i, max_row]] = B[[max_row, i]]

        # Make diagonal element 1
        pivot = A[i][i]
        if pivot == 0:
            raise ValueError("Matrix is singular or nearly singular")

        A[i] /= pivot
        B[i] /= pivot

        # Make all other elements in column zero
        for j in range(n):
            if j != i:
                factor = A[j][i]
                A[j] -= factor * A[i]
                B[j] -= factor * B[i]

    return B


# Example Usage
n = int(input("Enter the number of equations: "))
A = []
B = []
print("Enter the augmented matrix coefficients row-wise:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row[:-1])
    B.append(row[-1])
A = np.array(A, dtype=float)
B = np.array(B, dtype=float)
B = np.array(list(map(float, [5, 10, 15])))

solution = gauss_jordan_elimination(A, B)
print("Solution:", solution)

