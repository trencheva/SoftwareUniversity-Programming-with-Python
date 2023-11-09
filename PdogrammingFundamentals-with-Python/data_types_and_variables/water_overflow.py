number_of_lines = int(input())
capacity = 255
total_liters = 0
for i in range(number_of_lines):
    liters = int(input())
    if capacity >= liters:
        total_liters += liters
        capacity -= liters
    else:
        print('Insufficient capacity!')
print(total_liters)