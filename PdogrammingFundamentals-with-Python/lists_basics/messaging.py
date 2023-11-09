sequence_of_numbers = input().split(' ')
string = list(input())
new_message = []
for char in sequence_of_numbers:
    index = 0
    for number in char:
        index += int(number)

    index %= len(string)

    new_message.append(string.pop(index))
print(''.join(new_message))
