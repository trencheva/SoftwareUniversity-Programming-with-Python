results = {}
submissions = {}

while True:
    command = input().split('-')
    if len(command) == 1:
        break

    username = command[0]

    if len(command) == 2:
        del results[username]
    elif len(command) == 3:
        language = command[1]
        points = int(command[2])
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

        if username not in results.keys():
            results[username] = 0
        if points > results[username]:
            results[username] = points

print('Results:')
for name, points in results.items():
    print(f'{name} | {points}')
print('Submissions:')
for language, count in submissions.items():
    print(f'{language} - {count}')
