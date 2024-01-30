from collections import deque

worms = [int(worm) for worm in input().split()]
holes = deque(int(hole) for hole in input().split())

matches = 0
worms_count = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1
    else:
        worm -= 3
        if worm > 0:
            worms.append(worm)
if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and worms_count == matches:
    print("Every worm found a suitable hole!")
elif not worms:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join([str(el) for el in worms])}")
if holes:
    print(f"Holes left: {', '.join([str(el) for el in holes])}")
else:
    print("Holes left: none")