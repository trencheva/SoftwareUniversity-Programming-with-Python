sequence_of_numbers = input().split()
absolute_value = []

for number in sequence_of_numbers:
    absolute_value.append(abs(float(number)))
print(absolute_value)
