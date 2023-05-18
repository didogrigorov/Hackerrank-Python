import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    result = numpy.array(arr, float)
    res_arr = numpy.flip(result)
    return res_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)