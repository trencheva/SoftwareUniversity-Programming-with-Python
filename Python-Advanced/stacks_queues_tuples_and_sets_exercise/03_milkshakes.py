from collections import deque

chocolates = [int(el) for el in input().split(', ')]
cus_of_milk = deque([int(el) for el in input().split(', ')])

milkshakes = 0
while milkshakes < 5 and chocolates and cus_of_milk:
    curr_chocolate = chocolates.pop()
    curr_milk = cus_of_milk.popleft()
    if curr_milk <= 0 and curr_chocolate <= 0:
        continue
    elif curr_milk <= 0:
        chocolates.append(curr_chocolate)
        continue
    elif curr_chocolate <= 0:
        cus_of_milk.appendleft(curr_milk)
        continue
    if curr_milk == curr_chocolate:
        milkshakes += 1
    else:
        cus_of_milk.append(curr_milk)
        chocolates.append(curr_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cus_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cus_of_milk)}")
else:
    print("Milk: empty")