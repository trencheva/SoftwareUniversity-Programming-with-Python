import re

text = input()
cool_threshold = 1
cool_emoji_list = []
pattern = r'(::|\*\*)([A-Z][a-z][a-z]+)\1'
matches = re.findall(pattern, text)
digits = re.findall(r'\d', text)
for digit in digits:
    cool_threshold *= int(digit)

for match in matches:
    coolness = 0
    for char in match[1]:
        coolness += ord(char)
    if coolness > cool_threshold:
        result = match[0] + match[1] + match[0]
        cool_emoji_list.append(result)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(matches)} emojis found in the text. The cool ones are:')
print(' \n'.join(cool_emoji_list))