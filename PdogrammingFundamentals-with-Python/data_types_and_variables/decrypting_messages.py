key_number = int(input())
number_of_lines = int(input())
for character in range(number_of_lines):
    letter = input()
    new_letter = ord(letter) + key_number
    print(chr(new_letter), end='')
