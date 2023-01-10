from itertools import product

input1 = list(map(int, input().split()))
input2 = list(map(int, input().split()))
result = product(input1, input2)
print(*result)