def total_price_of_an_order(product, quantity):
    result = None
    if product == 'coffee':
        result = quantity * 1.50
    elif product == 'coke':
        result = quantity * 1.40
    elif product == 'water':
        result = quantity * 1.00
    elif product == 'snacks':
        result = quantity * 2.00
    return result


product_input = input()
quantity_input = int(input())
total_price = total_price_of_an_order(product_input, quantity_input)
print(f'{total_price:.2f}')

