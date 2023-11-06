registered_users = {}
n = int(input())
for current_user in range(n):
    input_line = input().split()
    command = input_line[0]
    username = input_line[1]

    if command == 'register':
        if username not in registered_users.keys():
            license_plate_number = input_line[2]
            registered_users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_users[username]}")

    elif command == 'unregister':
        if username not in registered_users.keys():
            print(f"ERROR: user {username} not found")
        else:
            del registered_users[username]
            print(f"{username} unregistered successfully")
for username, license_plate_number in registered_users.items():
    print(f"{username} => {license_plate_number}")
