import re
demons_input = input()
demons_dict = {}

demons = re.findall(r'[^\s,]+', demons_input)
print(demons)
for demon_name in demons:

    letters_match = re.findall(r'[^0-9+\-*\/\.]', demon_name)
    total_health = sum([ord(char) for char in letters_match])
    digits_match = re.findall(r'[\-+]*[\d]\.*\d*', demon_name)

    damage = sum([float(digit) for digit in digits_match])
    if damage != 0:
        for char in demon_name:
            if char == '*':
                damage *= 2
            elif char == '/':
                damage /= 2

    demons_dict[demon_name] = [total_health, damage]

demons_sorted = sorted(demons_dict.items(), key=lambda x: x)
demons_dict = dict(demons_sorted)

for name, health_and_damage in demons_dict.items():
    print(f'{name} - {health_and_damage[0]} health, {health_and_damage[1]:.2f} damage')
