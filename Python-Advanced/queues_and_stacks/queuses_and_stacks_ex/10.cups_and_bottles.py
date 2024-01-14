from collections import deque

cups = deque(int(cup) for cup in input().split())
bottles = deque(int(bottle) for bottle in input().split())

wasted_water = 0

while cups:
    if bottles:
        current_cup = cups.popleft()
        while current_cup > 0:
            current_bottle = bottles.pop()
            current_cup -= current_bottle
            if current_cup < 0:
                wasted_water += abs(current_cup)
                break
    else:
        print(f"Cups: ", *cups)
        break

else:
    bottles_left = [str(bottle) for bottle in bottles]
    print(f"Bottles: ", *bottles_left)

print(f"Wasted litters of water: {wasted_water}")
