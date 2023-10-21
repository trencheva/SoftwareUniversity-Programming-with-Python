energy = int(input())
count = 0
you_lost = False
while True:
    command = input()
    if command == 'End of battle':
        break
    distance = int(command)
    if energy >= distance:
        count += 1
        energy -= distance
    else:
        you_lost = True
        break
    if count % 3 == 0:
        energy += count

if you_lost:
    print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
else:
    print(f"Won battles: {count}. Energy left: {energy}")
