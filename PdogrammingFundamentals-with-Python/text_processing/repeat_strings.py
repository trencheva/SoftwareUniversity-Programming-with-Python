sequence_of_strings = input().split()

new_string = [text * len(text) for text in sequence_of_strings]
print(''.join(new_string))