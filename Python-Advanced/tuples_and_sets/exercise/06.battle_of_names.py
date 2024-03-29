n_rows = int(input())

even_numbers = set()
odd_numbers = set()

for row in range(1, n_rows + 1):
    name = input()
    ascii_sum = sum([ord(char) for char in name]) // row

    if ascii_sum % 2 == 0:
        even_numbers.add(ascii_sum)
    else:
        odd_numbers.add(ascii_sum)

final_result = set()

if sum(even_numbers) == sum(odd_numbers):
    final_result = even_numbers.union(odd_numbers)
elif sum(even_numbers) < sum(odd_numbers):
    final_result = odd_numbers.difference(even_numbers)
else:
    final_result = even_numbers.symmetric_difference(odd_numbers)

print(*final_result, sep=', ')
