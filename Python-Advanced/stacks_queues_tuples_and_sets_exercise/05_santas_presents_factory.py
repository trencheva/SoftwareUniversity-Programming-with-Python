from collections import deque

materials = [int(m) for m in input().split()]
magic_levels = deque(int(l) for l in input().split())

crafting_combinations = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

crafted_presents = []

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[-1] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic_level:
        continue

    result = material * magic_level

    if crafting_combinations.get(result):
        crafted_presents.append(crafting_combinations[result])
    elif result < 0:
        materials.append(material + magic_level)
    elif result > 0:
        materials.append(material + 15)

if {'Doll', 'Wooden train'}.issubset(crafted_presents) or {'Teddy bear', 'Bicycle'}.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

[print(f'{toy}: {crafted_presents.count(toy)}') for toy in sorted(set(crafted_presents))]
