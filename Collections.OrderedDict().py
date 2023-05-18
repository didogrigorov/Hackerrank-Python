from collections import OrderedDict

items = int(input())
items_dict = OrderedDict()

for i in range(items):
    price = 0
    item_name = ""

    user_input = input().split() # banana fries 12
    for item in user_input:
        if item.isdigit():
            int_item = int(item)
            price += int_item
        else:
            item_name += item + " "

    item_name = item_name.strip()
    if item_name in items_dict:
        items_dict[item_name] += price
    else:
        items_dict[item_name] = price


for k, v in items_dict.items():
    print(f"{k} {v}")