products_info = input().split()
products_dict = {}
for product_index in range(0, len(products_info), 2):
    product = products_info[product_index]
    quantities = int(products_info[product_index + 1])

    products_dict[product] = quantities

products_to_search = input().split()

for current_product in products_to_search:
    if current_product in products_dict:
        print(f"We have {products_dict[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")