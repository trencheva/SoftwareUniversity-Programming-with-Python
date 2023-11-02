products_dict = {}

while True:
    product_info = input()

    if product_info == "statistics":
        break

    product, quantity = product_info.split(': ')
    quantity = int(quantity)

    if product in products_dict:
        products_dict[product] += quantity
    else:
        products_dict[product] = quantity

total_products = len(products_dict)
total_quantities = sum(products_dict.values())

string_of_products = ''
for k, v in products_dict.items():
    string_of_products += f"\n- {k}: {v}"
print(f"Products in stock:{string_of_products}\nTotal Products: {total_products}\nTotal Quantity: {total_quantities}")
