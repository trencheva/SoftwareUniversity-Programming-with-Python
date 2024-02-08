from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

created_items = {}

healing_items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

while textiles and medicaments:
    textile = textiles.popleft()
    med = medicaments.pop()

    searched_sum = textile + med

    if searched_sum in healing_items.keys():
        created_items[healing_items[searched_sum]] = created_items.get(healing_items[searched_sum], 0) + 1

    elif searched_sum > 100:
        created_items["MedKit"] = created_items.get("MedKit", 0) + 1
        diff = searched_sum - 100
        medicaments.append(medicaments.pop() + diff)

    else:
        medicaments.append(med + 10)

if not textiles and not medicaments:
    print(f"Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

[print(f"{item} - {amount}") for item, amount in sorted_items]

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments[::-1])}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")