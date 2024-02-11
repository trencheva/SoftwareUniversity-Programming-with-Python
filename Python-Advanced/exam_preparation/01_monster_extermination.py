from collections import deque

monsters_armour = deque(int(x) for x in input().split(","))
striking_impact = [int(x) for x in input().split(",")]

killed_monsters = 0

while monsters_armour and striking_impact:

    armor = monsters_armour.popleft()
    impact = striking_impact.pop()

    if impact >= armor:

        impact -= armor
        killed_monsters += 1

        if impact > 0:
            if striking_impact:
                new_impact = impact + striking_impact.pop()
                striking_impact.append(new_impact)
            else:
                striking_impact.append(impact)

    else:
        monsters_armour.append(armor - impact)

if not monsters_armour:
    print("All monsters have been killed!")

if not striking_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")