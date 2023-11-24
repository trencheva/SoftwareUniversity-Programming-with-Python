import re

number_of_barcodes = int(input())
pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

for current_barcode in range(number_of_barcodes):
    barcode = input()
    match = re.match(pattern, barcode)

    if match:
        number = re.findall(r'\d', barcode)

        if number:
            print(f'Product group: {"".join(number)}')
        else:
            print('Product group: 00')

    else:
        print('Invalid barcode')