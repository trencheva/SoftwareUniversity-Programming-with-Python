from collections import deque

quantity_of_water = int(input())
people = deque()

name = input()
while name != 'Start':
    people.append(name)
    name = input()

command = input().split()
while command[0] != 'End':
    if len(command) == 1:
        person = people.popleft()
        liters_needed = int(command[0])
        if liters_needed <= quantity_of_water:
            quantity_of_water -= liters_needed
            print(f"{person} got water")
        else:
            print(f'{person} must wait')
    else:
        _, liters_to_add = command
        quantity_of_water += int(liters_to_add)
    command = input().split()

print(f'{quantity_of_water} liters left')