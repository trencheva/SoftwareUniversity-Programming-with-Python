def grocery_store(**products_data):

    result = sorted(products_data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return '\n'.join(f'{product}: {quantity}' for product, quantity in result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
