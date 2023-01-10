num = int(input())
stamps = set()
counter = 0

while counter <= num:
    user_input = input().strip()
    stamps.add(user_input)
    counter += 1

    if counter == num:
        break

print(len(stamps))