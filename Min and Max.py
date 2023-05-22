import numpy

user_input = input().split()
N = int(user_input[0])
i = 0
matrix = []

while i < N:
    nums = list(map(int, input().split()))
    matrix.append(nums)
    i += 1

np_array = numpy.array(matrix)
array_min = numpy.min(np_array, axis=1)
array_max = numpy.max(np_array, axis=1)

print(max(array_min))