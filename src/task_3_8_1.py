import numpy

def task381(arr, i, j):
    if i > len(arr):
        return 0
    elif j > len(arr[i]):
        return 0
    else:
        return arr[i - 1][j - 1]

arr = numpy.array([
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2]
])

print(arr)

print(task381(arr, -3, -3))
print(task381(arr, -2, -2))
print(task381(arr, -1, -1))
print(task381(arr, 0, 0))
print()
print(task381(arr, 4, 4))
print(task381(arr, 40, 4))
print(task381(arr, 4, 40))