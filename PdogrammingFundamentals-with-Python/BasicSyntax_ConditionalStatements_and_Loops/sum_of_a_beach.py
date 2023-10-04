string = input().lower()
sunny_list = ['sand', 'sun', 'fish', 'water']
counter = 0

for match in sunny_list:
    if match in string:
        counter += string.count(match)

print(counter)
