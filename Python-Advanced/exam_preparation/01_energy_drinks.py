from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))

MAX_CAFFEINE = 300

drank_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    caffeine = milligrams_of_caffeine.pop()
    energy_drink = energy_drinks.popleft()

    if caffeine * energy_drink + drank_caffeine <= MAX_CAFFEINE:
        drank_caffeine += caffeine * energy_drink

    else:
        energy_drinks.append(energy_drink)
        drank_caffeine -= 30

        if drank_caffeine < 0:
            drank_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {drank_caffeine} mg caffeine.")