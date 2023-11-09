some_string = input()

numbers = ''
letters = ''
characters = ''
for char in some_string:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        characters += char

print(numbers)
print(letters)
print(characters)
