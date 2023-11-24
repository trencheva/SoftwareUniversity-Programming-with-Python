def rate(plants_info: list, name: str, plant_rating: float):
    for plant in plants_info:
        if name == plant['name']:
            plant['rating'].append(plant_rating)
            return True
    print('error')


def update(plants_info: list, name: str, rarity: int):
    for plant in plants_info:
        if name == plant['name']:
            plant['rarity'] = rarity
            return True
    print('error')


def reset(plants_info: list, name: str):
    for plant in plants_info:
        if name == plant['name']:
            plant['rating'] = []
            return True
    print('error')


num = int(input())
plants_information = []

for _ in range(num):
    plant, rarity = input().split('<->')

    plants_information.append({"name": plant, "rarity": int(rarity), "rating": []})

while True:
    command = input()
    if command == "Exhibition":
        break

    command = command.split(': ')
    action = command[0]

    if action == 'Rate':
        plant_name, rating = command[1].split(' - ')
        rate(plants_information, plant_name, float(rating))

    elif action == 'Update':
        plant_name, new_rarity = command[1].split(' - ')
        update(plants_information,plant_name, int(new_rarity))

    elif action == 'Reset':
        plant_name = command[1]
        reset(plants_information, plant_name)

print('Plants for the exhibition:')
for plant in plants_information:
    if len(plant["rating"]) > 0:
        average_rating = sum(plant["rating"]) / len(plant["rating"])
    else:
        average_rating = 0
    print(f'- {plant["name"]}; Rarity: {plant["rarity"]}; Rating: {average_rating:.2f}')


