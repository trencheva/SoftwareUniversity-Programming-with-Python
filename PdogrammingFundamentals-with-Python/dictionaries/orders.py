# my_dict = {'beer': [2, 2]}
#
# new_dict = {key: my_dict[key][0] * my_dict[key][1] for key in my_dict}
products_price = {}
products_quantity = {}
while True:
    command = input().split()
    if len(command) == 1:
        break

    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in products_quantity.keys():
        products_quantity[product] = 0
    products_quantity[product] += quantity
    products_price[product] = price

for product, quantity in products_quantity.items():
    total_price = products_price[product] * products_quantity[product]
    print(f"{product} -> {total_price:.2f}")
