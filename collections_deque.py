from collections import deque

N = int(input())
counter = 0
d = deque()

while counter < N:
    user_input = input()

    if "append" in user_input or "appendleft" in user_input:
        info = user_input.split()
        value = info[1]
        if value.isdigit():
            value = int(value)
        if info[0] == "append":
            d.append(value)
        elif info[0] == "appendleft":
            d.appendleft(value)

    if user_input == "pop":
        d.pop()
    elif user_input == "popleft":
        d.popleft()

    counter += 1

print(*d)