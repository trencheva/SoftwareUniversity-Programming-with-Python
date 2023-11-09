from operator import itemgetter

contest_dict = {}
usernames_info_dict = {}
while True:
    information = input()
    if ':' not in information:
        break
    contest, password = information.split(':')
    if contest not in contest_dict.keys():
        contest_dict[contest] = ''
    contest_dict[contest] = password

while True:
    submissions = input()
    if '=>' not in submissions:
        break

    current_contest, current_pass, username, current_points = submissions.split('=>')
    current_points = int(current_points)
    if current_contest in contest_dict.keys():
        if contest_dict[current_contest] == current_pass:
            if username not in usernames_info_dict.keys():
                usernames_info_dict[username] = {}
            for user, contest in usernames_info_dict.items():
                if user == username:
                    if current_contest not in contest.keys() or contest[current_contest] < current_points:
                        contest[current_contest] = current_points


total_points = 0
winner = ''
for user, info in usernames_info_dict.items():
    current_points = 0
    for contest, points in info.items():
        current_points += points
    if current_points > total_points:
        total_points = current_points
        winner = user

print(f"Best candidate is {winner} with total {total_points} points.")
print('Ranking:')
for username, info in sorted(usernames_info_dict.items()):
    print(username)
    sorted_info = dict(sorted(info.items(), key=itemgetter(1), reverse=True))
    for contest, points in sorted_info.items():
        print(f'##  {contest} -> {points}')
