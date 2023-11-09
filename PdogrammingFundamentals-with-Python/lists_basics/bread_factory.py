events = input().split('|')
energy = 100
coins = 100
day_is_completed = True
for current_event in events:
    event = current_event.split('-')
    event_name = event[0]
    number = int(event[1])
    if event_name == 'rest':
        current_energy = energy + number
        if current_energy > 100:
            current_energy = 100
        gained_energy = current_energy - energy
        energy = current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
    elif event_name == 'order':
        if energy >= 30:
            print(f"You earned {number} coins.")
            coins += number
            energy -= 30
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event_name}.")
        else:
            day_is_completed = False
            break
if day_is_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
else:
    print(f"Closed! Cannot afford {event_name}.")