import numpy as np
import os

matrix = np.load("./task2/matrix_29_2.npy")

size = len(matrix)

x = list()
y = list()
z = list()

limit = 529

for i in range(0, size):
    for j in range(0, size):
        if matrix[i][j] > limit:
            x.append(i)
            y.append(j)
            z.append(matrix[i][j])

np.savez("./task2/points", x=x, y=y, z=z)
np.savez_compressed("./task2/points_zip", x=x, y=y, z=z)

print(f"points     = {os.path.getsize('./task2/points.npz')}")
print(f"points_zip = {os.path.getsize('./task2/points_zip.npz')}")