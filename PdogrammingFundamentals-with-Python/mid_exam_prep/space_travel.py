travel_route = input().split('||')
fuel = int(input())
ammunition = int(input())
mission_failed = False
for current_command in range(len(travel_route)-1):
    current_command = travel_route[current_command].split()
    command = current_command[0]
    number = int(current_command[1])

    if command == 'Travel':
        if number <= fuel:
            fuel -= number
            print(f"The spaceship travelled {number} light-years.")
        else:
            mission_failed = True
            break
    elif command == 'Enemy':
        if ammunition >= number:
            ammunition -= number
            print(f"An enemy with {number} armour is defeated.")
        else:
            if fuel >= number * 2:
                fuel -= number * 2
                print(f"An enemy with {number} armour is outmaneuvered.")
            else:
                mission_failed = True
                break
    elif command == 'Repair':
        fuel += number
        ammunition += number * 2
        print(f"Ammunitions added: {number * 2}.")
        print(f"Fuel added: {number}.")
if mission_failed:
    print("Mission failed.")
else:
    print("You have reached Titan, all passengers are safe.")