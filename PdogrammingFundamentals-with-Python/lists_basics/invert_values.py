string_of_numbers = input().split(" ")
opposite_numbers = []
for number in string_of_numbers:
    opposite_numbers.append(-int(number))
print(opposite_numbers)