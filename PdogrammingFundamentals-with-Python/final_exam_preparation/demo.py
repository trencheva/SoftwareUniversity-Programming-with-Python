submissions = {}
results = {}
while True:
    input_information = input().split('-')
    if input_information[0] == "exam finished":
        break
    username = input_information[0]
    if len(input_information) == 3:
        language, points = input_information[1], int(input_information[2])
        if language not in submissions.keys():
            submissions[language] = 0
        if username not in results.keys():
            results[username] = {}
        if language not in results[username].keys():
            results[username][language] = 0
        if results[username][language] < points:
            results[username][language] = points
        submissions[language] += 1

    else:
        results.pop(username)

print('Results:')
for name, language_and_points in results.items():
    total_points = 0
    for points in language_and_points.values():
        total_points += points
    print(f'{name} | {total_points}')

print('Submissions:')
for language, submissions_count in submissions.items():
    print(f'{language} - {submissions_count}')


