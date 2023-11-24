import re

pattern = r'%([A-Z][a-z]+)%[^$%|.]*<(\w+)>[^$%|.]*\|(\d+)\|([^$%|.]*\d+.*\d*)[$]'
income = 0
while True:
    string = input()
    if string == 'end of shift':
        break

    match = re.findall(pattern, string)
    if match:
        customer_name = match[0][0]
        product = match[0][1]
        price = int(match[0][2]) * float("".join((re.findall(r'\d+\.*\d*', match[0][3]))))
        income += price
        print(f"{customer_name}: {product} - {price:.2f}")
print(f"Total income: {income:.2f}")

