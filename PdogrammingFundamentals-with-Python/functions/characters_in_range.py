def all_the_characters(first: str, second: str) -> list:
    characters = []
    for current_character in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_character))
    return characters


first_character = input()
second_character = input()
print(*all_the_characters(first_character, second_character))
