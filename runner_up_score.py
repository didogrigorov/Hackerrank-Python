n = int(input())
num_list = list(int(num) for num in input().strip().split())[:n]

mylist = set(num_list)

sorted_list = sorted(mylist, key= lambda x: -x)
print(sorted_list[1])