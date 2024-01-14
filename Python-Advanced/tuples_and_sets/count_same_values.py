numbers = input().split()

numbers_dict = {}

for num in numbers:
    if num not in numbers_dict:
        numbers_dict[num] = 0
    numbers_dict[num] += 1


for number, count in numbers_dict.items():
    number = float(number)
    print(f"{number:.1f} - {count} times")