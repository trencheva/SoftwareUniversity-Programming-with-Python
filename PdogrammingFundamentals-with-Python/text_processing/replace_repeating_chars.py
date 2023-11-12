single_string = input()
new_string = single_string[0]

for char in single_string:
    if char != new_string[-1]:
        new_string += char

print(new_string)
