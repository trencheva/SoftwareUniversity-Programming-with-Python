import re
n = int(input())

for _ in range(n):
    string = input()

    pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'
    match = re.findall(pattern, string)
    if match:
        command = match[0][0]
        print(f'{command}:', end=' ')
        message = match[0][1]
        for letter in message:
            print(ord(letter), end=' ')
        print()
    else:
        print(f"The message is invalid")