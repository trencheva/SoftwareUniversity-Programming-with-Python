characters = input().split(', ')
characters_dict = {char: ord(char) for char in characters}
print(characters_dict)