for i in range(2,6):
    print(*list(map(lambda x: list(range(1,6))[-1],list(range(1,6)))),sep=__name__[:0])

for i in range(1,int(input())):
    print((pow(10, i)//9)*i)