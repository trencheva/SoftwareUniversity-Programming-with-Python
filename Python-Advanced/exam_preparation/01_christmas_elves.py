from collections import deque

elves_energy = deque(int(el) for el in input().split())
materials_in_box = [int(el) for el in input().split()]

used_energy = 0
number_of_toys = 0

count = 0
 
while elves_energy and materials_in_box:
    if elves_energy[0] < 5:
        elves_energy.popleft()
        continue

    energy = elves_energy.popleft()
    material = materials_in_box.pop()

    not_enough_energy = False
    count += 1

    if energy >= material:

        if count % 3 == 0:
            if energy >= material * 2:
                used_energy += material * 2
                number_of_toys += 2
                energy -= material * 2
                energy += 1
            else:
                not_enough_energy = True
        else:
            number_of_toys += 1
            used_energy += material
            energy -= material
            energy += 1

        if count % 5 == 0:

            if count % 3 == 0 and not not_enough_energy:
                number_of_toys -= 2
            else:
                number_of_toys -= 1
            energy -= 1

    else:
        not_enough_energy = True

    if not_enough_energy:
        materials_in_box.append(material)
        energy *= 2

    elves_energy.append(energy)

print(f"Toys: {number_of_toys}")
print(f"Energy: {used_energy}")

if elves_energy:
    print(f"Elves left: {', '.join(str(el) for el in elves_energy)}")
if materials_in_box:
    print(f"Boxes left: {', '.join(str(el) for el in materials_in_box)}")