import re

purchase_information = input()
list_of_furniture = []
total_cost = 0
pattern = r'>{2}([A-Za-z]+)<{2}(\d+\.?\d*)!(\d+)\b'
while purchase_information != 'Purchase':
    match = re.search(pattern, purchase_information)
    if match:
        name, price, quantity = match.groups()
        list_of_furniture.append(name)
        total_cost += float(price) * int(quantity)
    purchase_information = input()

print('Bought furniture:')
for name in list_of_furniture:
    print(name)
print(f'Total money spend: {total_cost:.2f}')
