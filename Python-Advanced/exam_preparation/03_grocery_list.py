def shop_from_grocery_list(budget, grocery_list, *products_info):
    purchased_items = []

    for product, price in products_info:
        if product in grocery_list:
            if budget < price:
                break

            budget -= price
            purchased_items.append(product)
            grocery_list.remove(product)
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(el for el in grocery_list if el not in purchased_items)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
