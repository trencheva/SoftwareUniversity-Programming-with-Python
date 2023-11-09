string_of_gifts = input().split(' ')
line = input().split(' ')
command = line[0]
product = line[1]
while command != 'No' and product != 'Money':

    if command == 'OutOfStock':
        while product in string_of_gifts:
            index = string_of_gifts.index(product)
            string_of_gifts[index] = 'None'
    elif command == 'Required':
        index = int(line[2])
        if index in range(len(string_of_gifts)):
            string_of_gifts[index] = product
    elif command == 'JustInCase':
        string_of_gifts[-1] = product
    line = input().split(' ')
    command = line[0]
    product = line[1]
while 'None' in string_of_gifts:
    string_of_gifts.remove('None')
print(*string_of_gifts)
