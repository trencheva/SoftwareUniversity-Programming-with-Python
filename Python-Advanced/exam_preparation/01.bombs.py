from collections import deque


def check_bomb_count():
    bombs_collected = True
    for count in bombs_count.values():
        if count < 3:
            bombs_collected = False
    return bombs_collected


bomb_effects = deque(int(el) for el in input().split(', '))
bomb_casings = deque(int(el) for el in input().split(', '))

bombs_count = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}

bombs_info = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}

while bomb_effects and bomb_casings:

    if check_bomb_count():
        break

    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()

    searched_number = effect + casing
    for number, name in bombs_info.items():
        if searched_number == number:
            bombs_count[name] += 1
            break
    else:
        bomb_effects.appendleft(effect)
        bomb_casings.append(casing - 5)


if check_bomb_count():
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print(f"Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

for name, quantity in sorted(bombs_count.items(), key=lambda x: x[0]):
    print(f'{name}: {quantity}')
