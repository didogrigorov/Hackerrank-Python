import re
number_of_cards = int(input())

for _ in range(number_of_cards):
    card_number = input()
    if not re.match('[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$', card_number):
        print ('Invalid')
        continue
    card_number = card_number.replace('-','')
    if re.search(r'([0-9])\1{3}', card_number):
        print ('Invalid')
        continue
    print ('Valid')