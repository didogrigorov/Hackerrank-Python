from itertools import permutations

user_input = input().split()

word = user_input[0]
word_chars = list(word.upper())
repeats = int(user_input[1])

result = list(sorted(permutations(word_chars, repeats)))

for item in result:
    print(''.join(item))