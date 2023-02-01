from collections import Counter

shoes_numbers = int(input())
shoes_sizes = list(map(int, input().split()))
customers = int(input())
total_price = 0
counter = 0
shoes_dict = Counter(shoes_sizes)

while counter < customers:
    shoe_size, price = list(map(int, input().split()))

    if shoe_size not in shoes_sizes:
        counter += 1
        continue

    if shoes_dict[shoe_size] == 0:
        counter += 1
        continue

    if shoe_size in shoes_dict:
        shoes_dict[shoe_size] -= 1

    total_price += price
    counter += 1

print(total_price)