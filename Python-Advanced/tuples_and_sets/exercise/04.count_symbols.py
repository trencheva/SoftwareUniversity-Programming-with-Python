text = input()

result = {}

for char in text:
    if char not in result:
        result[char] = 0
    result[char] += 1


for char_name, occ in sorted(result.items()):
    print(f'{char_name}: {occ} time/s')
