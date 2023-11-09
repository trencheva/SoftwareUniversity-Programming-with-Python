numbers = input().split()
rounded_numbers = []

for number in numbers:
    rounded_numbers.append(round(float(number)))
print(rounded_numbers)