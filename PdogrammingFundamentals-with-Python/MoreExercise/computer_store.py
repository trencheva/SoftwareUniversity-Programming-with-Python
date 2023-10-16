price = input()
total_price = 0
taxes = 0
price_without_taxes = 0

while price != 'special':
    if price == 'regular':
        break
    price = float(price)
    if price < 0:
        print("Invalid price!")
    else:
        price_without_taxes += price
    price = input()

taxes = price_without_taxes * 0.20
total_price = price_without_taxes + taxes

if price == 'special':
    total_price -= total_price * 0.10
if total_price == 0:
    print('Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print('-----------')
    print(f"Total price: {total_price:.2f}$")