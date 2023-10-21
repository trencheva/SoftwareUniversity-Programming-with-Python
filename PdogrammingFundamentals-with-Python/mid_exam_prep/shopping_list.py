def urgent_func(groceries: list, item_input):
    groceries.insert(0, item_input)
    return groceries


def unnecessary_func(groceries: list, item_input):
    groceries.remove(item_input)
    return groceries


def correct_func(groceries: list, first_item, second_item):
    index = groceries.index(first_item)
    groceries[index] = second_item
    return groceries


def rearrange_func(groceries: list, item_input):
    groceries.remove(item_input)
    groceries.append(item_input)
    return groceries


def is_item_in_list(groceries: list, input_item):
    if input_item in groceries:
        return True
    return False


list_of_groceries = input().split('!')
while True:
    command = input()

    if command == "Go Shopping!":
        break

    command = command.split()
    action = command[0]
    item = command[1]

    if action == 'Urgent':
        if not is_item_in_list(list_of_groceries, item):
            urgent_func(list_of_groceries, item)
    elif action == 'Unnecessary':
        if is_item_in_list(list_of_groceries, item):
            unnecessary_func(list_of_groceries, item)
    elif action == 'Correct':
        new_item = command[2]
        if is_item_in_list(list_of_groceries, item):
            correct_func(list_of_groceries, item, new_item)
    elif action == 'Rearrange':
        if is_item_in_list(list_of_groceries, item):
            rearrange_func(list_of_groceries, item)

print(', '.join(list_of_groceries))
