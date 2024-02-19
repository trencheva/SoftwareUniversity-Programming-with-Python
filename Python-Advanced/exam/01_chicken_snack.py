from collections import deque

amount_of_money = [int(x) for x in input().split()]
food_prices = deque(int(x) for x in input().split())

eaten_food = 0

while amount_of_money and food_prices:
    current_money = amount_of_money.pop()
    current_price = food_prices.popleft()

    if current_price == current_money:
        eaten_food += 1
    elif current_money > current_price:
        change = current_money - current_price
        if amount_of_money:
            amount_of_money[-1] += change
        else:
            amount_of_money.append(change)
        eaten_food += 1

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif eaten_food > 0:
    if eaten_food == 1:
        print(f"Henry ate: {eaten_food} food.")
    else:
        print(f"Henry ate: {eaten_food} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")