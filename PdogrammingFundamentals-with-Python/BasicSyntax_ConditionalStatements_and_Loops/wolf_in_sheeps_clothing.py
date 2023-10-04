string = input().split(', ')
sheep_counter = 0
wolf_position = 0
for current_position in string[::-1]:
    if current_position == 'sheep':
        sheep_counter += 1
    elif current_position == 'wolf':
        wolf_position = sheep_counter + 1
        if wolf_position == 1:
            print('Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!')
