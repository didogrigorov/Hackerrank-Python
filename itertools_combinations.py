from itertools import combinations

string, k = input().split()
k = int(k)
string = list(string)

for i in range(0, k + 1):
    result = sorted(list(combinations(string, i)))
    for item in result:
        print(*item, sep="")