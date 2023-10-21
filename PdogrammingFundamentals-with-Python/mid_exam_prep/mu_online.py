health = 100
bitcoins = 0
room = 0
list_of_rooms = input().split('|')
was_killed = False
for current_room in list_of_rooms:
    room += 1
    command = current_room.split()[0]
    number = current_room.split()[1]
    number = int(number)

    if command == "potion":
        health_help = health
        health += number
        if health > 100:
            health = 100
        amount = health - health_help
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins += number
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            was_killed = True
            break

if was_killed:
    print(f"You died! Killed by {command}.")
    print(f"Best room: {room}")
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
