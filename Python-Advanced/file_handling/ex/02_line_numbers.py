from string import punctuation


with open('files/text.txt') as file:
    content = file.readlines()


with open('files/output.txt', 'w') as output_file:
    for idx in range(len(content)):

        count_letters = 0
        count_marks = 0

        for char in content[idx]:
            if char in punctuation:
                count_marks += 1
            elif char.isalpha():
                count_letters += 1

        output_file.write(f'Line: {idx + 1}: {content[idx][:-1]} ({count_letters})({count_marks})\n')

