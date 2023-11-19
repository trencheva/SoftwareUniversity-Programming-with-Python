import re

sentence = input()
searched_word = input()
pattern = fr'(?i)\b{searched_word}\b, i'

match = re.findall(pattern, sentence)
print(len(match))
