text = input()

result = {}

for char in text:
    result[char] = result.get(char, 0) + 1

for char_name, occ in sorted(result.items()):
    print(f'{char_name}: {occ} time/s')
