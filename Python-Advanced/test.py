from collections import deque

chocolates = [int(el) for el in input().split(', ')]
cups_of_milk = deque(int(el) for el in input().split(', '))

milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocolates.append(chocolate - 5)
if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
print('Chocolate:', end=' ')
if chocolates:
    print(f'{", ".join([str(el) for el in chocolates])}')
else:
    print('empty')

print('Milk:', end=' ')
if cups_of_milk:
    print(f'{", ".join([str(el) for el in cups_of_milk])}')
else:
    print('empty')



