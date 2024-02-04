marks = ("-", ",", ".", "!", "?")

with open('files/text.txt') as file:
    text = file.readlines()

    for line in range(0, len(text), 2):

        for mark in marks:
            text[line] = text[line].replace(mark, '@')

        print(' '.join(text[line].split()[::-1]))
