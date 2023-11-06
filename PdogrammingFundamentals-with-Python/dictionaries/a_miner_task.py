resources_dict = {}
while True:
    command = input()

    if command == 'stop':
        break

    quantity = int(input())

    if command not in resources_dict.keys():
        resources_dict[command] = 0
    resources_dict[command] += quantity

for resource, quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")
