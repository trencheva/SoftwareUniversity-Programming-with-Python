number_of_heroes = int(input())
heroes_dictionary = {}
for current_hero in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes_dictionary[hero_name] = [int(hit_points), int(mana_points)]

command = input().split(' - ')
while command[0] != 'End':
    current_hero = command[1]
    if command[0] == 'CastSpell':
        mana_points_needed = int(command[2])
        spell_name = command[3]
        if heroes_dictionary[current_hero][1] >= mana_points_needed:
            heroes_dictionary[current_hero][1] -= mana_points_needed
            print(f"{current_hero} has successfully cast {spell_name} and now has {heroes_dictionary[current_hero][1]} MP!")
        else:
            print(f"{current_hero} does not have enough MP to cast {spell_name}!")
    elif command[0] == 'TakeDamage':
        damage = int(command[2])
        attacker = command[3]
        heroes_dictionary[current_hero][0] -= damage
        if heroes_dictionary[current_hero][0] > 0:
            print(f"{current_hero} was hit for {damage} HP by {attacker} and now has {heroes_dictionary[current_hero][0]} HP left!")
        else:
            del heroes_dictionary[current_hero]
            print(f"{current_hero} has been killed by {attacker}!")
    elif command[0] == 'Recharge':
        amount_recharged = int(command[2])
        if heroes_dictionary[current_hero][1] + amount_recharged > 200:
            amount_recharged = 200 - heroes_dictionary[current_hero][1]
        heroes_dictionary[current_hero][1] += amount_recharged
        print(f"{current_hero} recharged for {amount_recharged} MP!")
    elif command[0] == 'Heal':
        amount_healed = int(command[2])
        if heroes_dictionary[current_hero][0] + amount_healed > 100:
            amount_healed = 100 - heroes_dictionary[current_hero][0]
        heroes_dictionary[current_hero][0] += amount_healed
        print(f"{current_hero} healed for {amount_healed} HP!")

    command = input().split(' - ')

for hero_name, points in heroes_dictionary.items():
    print(hero_name)
    print(f' HP: {points[0]}')
    print(f' MP: {points[1]}')