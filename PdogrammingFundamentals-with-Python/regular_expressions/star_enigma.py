import re

n = int(input())
attacked_planets = []
destroyed_planets = []

for message in range(n):
    encrypted_message = input()
    decrypted_message = ''

    pattern = r'(?i)[star]'
    matches = re.findall(pattern, encrypted_message)
    key = len(matches)

    for char in encrypted_message:
        decrypted_char = chr(ord(char) - key)
        decrypted_message += decrypted_char

    regex = r'(?i)@([a-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([AD])![^@\-!:>]*->(\d+)'

    information = re.findall(regex, decrypted_message)
    if information:
        if information[0][2] == 'A':
            attacked_planets.append(information[0][0])
        elif information[0][2] == 'D':
            destroyed_planets.append(information[0][0])

print(f"Attacked planets: {len(attacked_planets)}")
for planet in list(sorted(attacked_planets, key=lambda x: x)):
    print(f'-> {planet}')
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in list(sorted(destroyed_planets, key=lambda x: x)):
    print(f'-> {planet}')
