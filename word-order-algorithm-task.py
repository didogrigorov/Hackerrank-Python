num = int(input())
words = []

for i in range(num):
    user_input = input()
    words.append(user_input)
    if i == num:
        break

counted_items = []
newlist = words.copy()

word_count = 0

for item in words:
    for word in newlist:
        if item == word:
            word_count += 1
            newlist.remove(word)
    if word_count == 0:
        continue
    else:
        counted_items.append(word_count)
    word_count = 0

print(len(set(words)))
print(' '.join([str(x) for x in counted_items]))


#performance oriented solution

from collections import OrderedDict
import time

n = int(input())

start = time.time()
words = [input() for i in range(n)]
unique_words = OrderedDict()

for word in words:
    if word in unique_words:
        unique_words[word] += 1
    elif word not in unique_words:
        unique_words[word] = 1

print(len(unique_words.keys()))
[print(words, end=' ') for words in unique_words.values()]
