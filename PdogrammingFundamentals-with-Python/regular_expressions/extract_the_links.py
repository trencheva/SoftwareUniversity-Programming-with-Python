import re
sentence = input()
pattern = r'w{3}\.[A-Za-z0-9\-\.]+[a-z]*\.[a-z]+'

while sentence:
    match = re.findall(pattern, sentence)

    if match:
        print(''.join(match))
    sentence = input()
