houses = [int(s) for s in input().split('@')]
house_index = 0
while True:
    command = input()
    if command == 'Love!':
        break

    jump_length = int(command.split()[1])
    house_index += jump_length
    if house_index >= len(houses):
        house_index = 0
    if houses[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        houses[house_index] -= 2
        if houses[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")

print(f"Cupid's last position was {house_index}.")
if sum(houses) > 0:
    count = sum([1 for house in range(len(houses)) if houses[house] > 0])
    print(f"Cupid has failed {count} places.")
else:
    print("Mission was successful.")
