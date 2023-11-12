some_text = input()
new_string = ''

for char in some_text:
    new_string += chr(ord(char) + 3)

print(new_string)