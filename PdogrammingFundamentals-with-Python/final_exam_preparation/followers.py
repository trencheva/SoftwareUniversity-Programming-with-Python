followers = {}

while True:
    command = input()
    if command == "Log out":
        break
    tokens = command.split(': ')
    action = tokens[0]
    username = tokens[1]

    if action == 'New follower':
        if username not in followers.keys():
            followers[username] = [0, 0]

    elif action == 'Like':
        count = int(tokens[2])
        if username not in followers.keys():
            followers[username] = [count, 0]
        else:
            followers[username][0] += count

    elif action == 'Comment':
        if username not in followers.keys():
            followers[username] = [0, 1]
        else:
            followers[username][1] += 1

    elif action == 'Blocked':
        if username not in followers.keys():
            print(f"{username} doesn't exist.")
        else:
            followers.pop(username)
print(f'{len(followers)} followers')
for name, likes_and_comments in followers.items():
    print(f'{name}: {sum(likes_and_comments)}')

