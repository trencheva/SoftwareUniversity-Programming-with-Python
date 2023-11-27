encrypted_message = input()

while True:
    command = input().split('|')
    if command[0] == "Decode":
        break

    action = command[0]
    if action == 'Move':
        number = int(command[1])
        encrypted_message = encrypted_message[number:] + encrypted_message[:number]
    elif action == 'Insert':
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
print(f"The decrypted message is: {encrypted_message}")
