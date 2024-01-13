from collections import deque

quantity_of_food = int(input())

orders = deque(int(order) for order in input().split())

print(max(orders))

for order in orders.copy():
    if quantity_of_food >= order:
        food_to_be_removed = orders.popleft()
        quantity_of_food -= food_to_be_removed
    else:
        print(f"Orders left:", *orders)
        break
else:
    print(f'Orders complete')
