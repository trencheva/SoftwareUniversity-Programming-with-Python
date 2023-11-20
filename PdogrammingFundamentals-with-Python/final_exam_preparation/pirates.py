cities = {}
while True:
    command = input()
    if command == "Sail":
        break

    city, population, gold = command.split('||')
    if city not in cities:
        cities[city] = [0, 0]
    cities[city][0] += int(population)
    cities[city][1] += int(gold)

while True:
    command = input()
    if command == 'End':
        break
    command = command.split('=>')
    if command[0] == 'Plunder':
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        if cities[town][0] >= 0:
            cities[town][0] -= people
            killed_people = people
        else:
            killed_people = cities[town][0]
        if cities[town][1] >= gold:
            cities[town][1] -= gold
            stolen_gold = gold
        else:
            stolen_gold = cities[town][1]
        print(f"{town} plundered! {stolen_gold} gold stolen, {killed_people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    else:
        town = command[1]
        gold = int(command[2])
        if gold >= 0:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
        else:
            print(f"Gold added cannot be a negative number!")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, people_and_gold in cities.items():
        print(f'{town} -> Population: {people_and_gold[0]} citizens, Gold: {people_and_gold[1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
