contest_dict = {}
total_users_points = {}
while True:
    command = input()
    if '->' not in command:
        break

    username, contest, points = command.split(' -> ')
    if contest not in contest_dict.keys():
        contest_dict[contest] = {}
    if username not in contest_dict[contest].keys():
        contest_dict[contest][username] = 0
    if contest_dict[contest][username] < int(points):
        contest_dict[contest][username] = int(points)

for contest, username in contest_dict.items():
    print(f'{contest}: {len(username)} participants')
    count = 0
    sorted_usernames = dict(sorted(username.items(), key=lambda x: (-x[1], x[0].lower())))
    for name, points in sorted_usernames.items():
        count += 1
        print(f'{count}. {name} <::> {points}')
        if name not in total_users_points.keys():
            total_users_points[name] = 0
        total_users_points[name] += points

print('Individual standings:')
count = 0
sorted_total_points = dict(sorted(total_users_points.items(), key=lambda x: (-x[1], x[0].lower())))
for name, points in sorted_total_points.items():
    count += 1
    print(f'{count}. {name} -> {points}')