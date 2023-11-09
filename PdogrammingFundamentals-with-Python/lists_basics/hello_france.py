items = input().split('|')
budget = float(input())
profit = 0
sold_items = []

for current_item in range(len(items)):
    item = items[current_item].split('->')
    type_of_the_item = item[0]
    price_of_the_item = float(item[1])
    if type_of_the_item == 'Clothes' and price_of_the_item <= 50 \
            or type_of_the_item == 'Shoes' and price_of_the_item <= 35 \
            or type_of_the_item == 'Accessories' and price_of_the_item <= 20.50:
        if budget >= price_of_the_item:
            budget -= price_of_the_item
            new_price_of_the_item = price_of_the_item + price_of_the_item * 0.40
            profit += new_price_of_the_item - price_of_the_item
            sold_items.append(new_price_of_the_item)
for item in sold_items:
    print(f'{item:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if budget + sum(sold_items) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

