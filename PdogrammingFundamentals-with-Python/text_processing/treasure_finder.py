import re
key = [int(n) for n in input().split()]

while True:
    decrypted_message = ''
    encrypted_string = input()
    if encrypted_string == 'find':
        break

    key_index = 0
    for character_index in range(len(encrypted_string)):
        decrypted_message += chr(ord(encrypted_string[character_index]) - key[key_index])
        key_index += 1
        if key_index == len(key):
            key_index = 0

    pattern = r'(?i)&([a-z]+)&.*<(\w+)>'
    matches = re.findall(pattern, decrypted_message)
    type = matches[0][0]
    coordinates = matches[0][1]
    print(f"Found {type} at {coordinates}")



