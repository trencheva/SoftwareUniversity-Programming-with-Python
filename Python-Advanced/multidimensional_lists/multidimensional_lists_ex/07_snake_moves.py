from collections import deque

rows, cols = [int(el) for el in input().split()]
initial_word = list(input())

word_copy = deque(initial_word)

for row in range(rows):

    while len(word_copy) < cols:
        word_copy.extend(initial_word)
    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(cols)], sep='')
    else:
        print(*[word_copy.popleft() for _ in range(cols)][::-1], sep='')