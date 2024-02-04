import re

with open('../words.txt') as words:
    words_to_search = words.read()
    words_to_search = [word.lower() for word in words_to_search.split()]

with open('../input_text.txt') as input_text:
    text = input_text.read().lower()


word_count = {}

for word in words_to_search:
    pattern = re.compile(rf'\b{word}\b')
    results = re.findall(pattern, text)
    word_count[word] = results.count(word)

sorted_words_count = sorted(word_count.items(), key=lambda x: -x[1])

with open('../output.txt', 'a') as output:
    for word, count in sorted_words_count:
        output.write(f'{word} - {count}\n')