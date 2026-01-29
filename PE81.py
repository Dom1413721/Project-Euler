import numpy as np

# Load the file directly into a 2D NumPy array
matrix = np.loadtxt("0081_matrix.txt", delimiter=",", dtype=int)

def min_path(x):
    y = x
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if i == 0:
                if j == 0:
                    y[i,j] = x[i,j]
                else:
                    y[i,j] = y[i,j-1]+x[i,j]
            elif j == 0:
                y[i,j] = y[i-1,j]+x[i,j]
            else:
                y[i,j] = +x[i,j]+min(y[i-1,j], y[i,j-1])

    return(y)

print(min_path(matrix))

