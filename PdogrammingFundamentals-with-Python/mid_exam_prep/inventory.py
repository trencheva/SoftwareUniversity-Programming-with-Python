list_of_items = input().split(', ')
while True:
    command = input()
    if command == "Craft!":
        break
    command = command.split(' - ')
    action = command[0]
    item = command[1]
    if action == "Collect":
        if item not in list_of_items:
            list_of_items.append(item)
    elif action == 'Drop':
        if item in list_of_items:
            list_of_items.remove(item)
    elif action == 'Combine Items':
        item = item.split(':')
        old_item = item[0]
        new_item = item[1]
        if old_item in list_of_items:
            index = list_of_items.index(old_item)
            list_of_items.insert(index + 1, new_item)
    elif action == 'Renew':
        if item in list_of_items:
            list_of_items.remove(item)
            list_of_items.append(item)
print(', '.join(list_of_items))
