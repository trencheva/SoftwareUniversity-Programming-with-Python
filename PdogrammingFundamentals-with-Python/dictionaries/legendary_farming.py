items = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item_won = False
winner = ''
while True:
    list_of_items = input().split(' ')
    for index in range(0, len(list_of_items), 2):
        quantity = int(list_of_items[index])
        current_item = list_of_items[index + 1].lower()
        if current_item not in items.keys():
            items[current_item] = 0
        items[current_item] += quantity

        if items['shards'] >= 250:
            items['shards'] -= 250
            legendary_item_won = True
            winner = "Shadowmourne"
        elif items['fragments'] >= 250:
            items['fragments'] -= 250
            legendary_item_won = True
            winner = "Valanyr"
        elif items['motes'] >= 250:
            items['motes'] -= 250
            legendary_item_won = True
            winner = "Dragonwrath"
        if legendary_item_won:
            break
    if legendary_item_won:
        break

print(f"{winner} obtained!")
for item, quantity in items.items():
    print(f"{item}: {quantity}")
