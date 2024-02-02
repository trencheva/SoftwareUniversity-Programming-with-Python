from collections import deque

initial_fuel = [int(el) for el in input().split()]
consumption_idx = deque(int(el) for el in input().split())
needed_fuel = deque(int(el) for el in input().split())

altitudes = []
not_enough_fuel = False
altitude_count = 0
needed_altitudes = len(needed_fuel)

while initial_fuel and consumption_idx and needed_fuel:
    altitude_count += 1
    fuel = initial_fuel.pop() - consumption_idx.popleft()

    if fuel >= needed_fuel.popleft():
        print(f"John has reached: Altitude {altitude_count}")
        altitudes.append(f'Altitude {altitude_count}')
    else:
        print(f"John did not reach: Altitude {altitude_count}")
        print("John failed to reach the top.")
        not_enough_fuel = True
        break


if altitudes and not_enough_fuel:
    print(f"Reached altitudes: {', '.join(altitudes)}")
elif not altitudes:
    print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")