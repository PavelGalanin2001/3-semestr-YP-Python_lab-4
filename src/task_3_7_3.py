import numpy

def task373(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 3:
                sum += 1
    return sum

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

print(task373(arr))