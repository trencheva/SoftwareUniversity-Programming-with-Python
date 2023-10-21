def fire_func(warship_list: list, section_index: int, given_damage: int):
    if 0 <= section_index < len(warship_list):
        warship_list[section_index] -= given_damage
        if warship_list[section_index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()
    return warship_list


def defend_fun(pirate_ship_list: list, first_index: int, second_index, given_damage: int):
    if 0 <= first_index < len(pirate_ship_list) and 0 <= second_index < len(pirate_ship_list):
        for current_index in range(first_index, second_index + 1):
            pirate_ship_list[current_index] -= given_damage
            if pirate_ship_list[current_index] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
    return pirate_ship_list


def repair_func(pirate_ship_list: list, section_index: int, given_health: int, max_health: int):
    if 0 <= section_index < len(pirate_ship_list):
        pirate_ship_list[section_index] += given_health
        if pirate_ship_list[section_index] > max_health:
            pirate_ship_list[section_index] = max_health
    return pirate_ship_list


def status_func(pirate_ship_list: list, max_health: int):
    count = sum([1 for section in pirate_ship_list if section < max_health * 0.2])
    print(f"{count} sections need repair.")


pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
maximum_health_capacity = int(input())
while True:
    command = input()
    if command == "Retire":
        print(f"Pirate ship status: {sum(pirate_ship_status)}")
        print(f"Warship status: {sum(warship_status)}")
        break
    command = command.split(' ')
    action = command[0]
    if action == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        warship_status = fire_func(warship_status, index, damage)
    elif action == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        pirate_ship_status = defend_fun(pirate_ship_status, start_index, end_index, damage)
    elif action == 'Repair':
        index = int(command[1])
        health = int(command[2])
        pirate_ship_status = repair_func(pirate_ship_status, index, health, maximum_health_capacity)
    elif action == 'Status':
        status_func(pirate_ship_status, maximum_health_capacity)
