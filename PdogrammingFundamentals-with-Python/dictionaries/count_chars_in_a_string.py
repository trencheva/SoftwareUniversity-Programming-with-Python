text = input()
dictionary = {}

for letter in text:
    if letter != ' ':
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

for letter, count_letter in dictionary.items():
    print(f'{letter} -> {count_letter}')