import re
participants_list = input().split(', ')
participants_dict = {}
while True:
    command = input()
    if command == 'end of race':
        break

    name = re.findall(r'[A-Za-z]', command)
    name = ''.join(name)
    if name in participants_list:
        kilometers = re.findall(r'\d', command)
        kilometers = [int(digit) for digit in kilometers]
        kilometers = sum(kilometers)
        if name not in participants_dict.keys():
            participants_dict[name] = 0
        participants_dict[name] += kilometers
count = 0
extension = ''

participants_dict = dict(sorted(participants_dict.items(), key=lambda x: -x[1]))

for participant, kilometers in participants_dict.items():
    if count == 3:
        break
    count += 1
    if count == 1:
        extension = 'st'
    elif count == 2:
        extension = 'nd'
    else:
        extension = 'rd'
    print(f'{count}{extension} place: {participant}')

