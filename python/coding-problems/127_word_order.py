# link: https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

word_counter = OrderedDict()
n = int(input())

for _ in range(n):
    word = input()
    word_counter[word] = word_counter.get(word, 0) + 1

print(len(word_counter))
for word in word_counter:
    print(word_counter[word], end=" ")
