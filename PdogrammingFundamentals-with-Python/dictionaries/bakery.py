info = input().split()

products_dict = {}
for i in range(0, len(info), 2):
    food = info[i]
    quantities = int(info[i + 1])
    products_dict[food] = quantities

print(products_dict)