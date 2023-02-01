from itertools import combinations

string, k = input().split()
k = int(k)

string = list(string)
string.sort()

for i in range(0, k + 1):
    result = list(combinations(string, i))
    for item in result:
        print(*item, sep="")