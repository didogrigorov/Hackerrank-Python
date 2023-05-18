x, k = map(int, input().split())
polynomial = input()

result = eval(polynomial.replace("x", str(x)))
if result == k:
    print(True)
else:
    print(False)
