import re

string = input()
pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

matches = re.findall(pattern, string)
mirror_words = []
for words_pair in matches:
    if words_pair[1] == words_pair[2][::-1]:
        mirror_words.append(words_pair)

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")
if mirror_words:
    print('The mirror words are:')
    for index in range(len(mirror_words)):
        if index < len(mirror_words)-1:
            print(f'{mirror_words[index][1]} <=> {mirror_words[index][2]}', end=', ')
        else:
            print(f'{mirror_words[index][1]} <=> {mirror_words[index][2]}')
else:
    print('No mirror words!')
