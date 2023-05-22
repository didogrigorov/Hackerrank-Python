import numpy

N = int(input())
i = 0
matrix = []

while i < N:
    add = list(map(float, input().split()))
    matrix.append(add)
    i += 1

np_arr = numpy.array(matrix)
print(round(numpy.linalg.det(matrix), 2))