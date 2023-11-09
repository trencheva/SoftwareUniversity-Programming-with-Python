first_character = int(input())
last_character = int(input())
for current_char in range(first_character, last_character + 1):
    print(chr(current_char), end=' ')
