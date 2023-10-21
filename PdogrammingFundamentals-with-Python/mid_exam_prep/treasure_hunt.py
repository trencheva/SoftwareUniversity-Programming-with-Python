def loot_func(items: list, command_line):
    loot = command_line[1::]
    for current_loot in loot:
        if current_loot not in items:
            items.insert(0, current_loot)
    return items


def drop_func(items: list, command_line):
    index = int(command_line[1])
    if 0 <= index < len(items):
        item = items.pop(index)
        items.append(item)
    return items


def steal_func(items: list, command_line):
    stolen_items = int(command_line[1])
    list_of_stolen_items = []
    if stolen_items >= len(items):
        for item in range(len(items)):
            stolen_item = items.pop()
            list_of_stolen_items.append(stolen_item)
    else:
        for item in range(stolen_items):
            stolen_item = items.pop()
            list_of_stolen_items.append(stolen_item)
    print(', '.join(list_of_stolen_items[::-1]))
    return items


list_of_items = input().split('|')
while True:
    command = input()
    if command == 'Yohoho!':
        break
    command = command.split()
    if command[0] == 'Loot':
        list_of_items = loot_func(list_of_items, command)
    elif command[0] == 'Drop':
        list_of_items = drop_func(list_of_items, command)
    elif command[0] == 'Steal':
        list_of_items = steal_func(list_of_items, command)
if list_of_items:
    count_items = sum([1 for item in list_of_items])
    sum_of_length = sum(len(item) for item in list_of_items)
    average_treasure_gain = sum_of_length / count_items
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
