from collections import defaultdict

n, m = input().split()
n = int(n)
m = int(m)

a_dict = defaultdict(list)
indexes = []

for i in range(1, n + 1):
    a_dict[n].append(input())
# {5: [a,a,b,a,b]}
b_list = [input() for j in range(m)]

for item in b_list:
    if item not in a_dict[n]:
        print(-1)
    for i in range (len(a_dict[n])):
        if item == a_dict[n][i]:
            indexes.append(i + 1)
    if indexes:
        print(' '.join([str(x) for x in indexes if x != " "]))
    indexes = []