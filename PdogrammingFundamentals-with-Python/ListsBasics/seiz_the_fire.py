fires_with_their_cells = input().split('#')
water = int(input())
current_cell_data = []
total_effort = 0
total_fire = 0
valid_range = []
for current_cell in range(len(fires_with_their_cells)):
    if water > 0:
        current_cell_data = fires_with_their_cells[current_cell].split(' = ')
        type_of_fire = current_cell_data[0]
        range = int(current_cell_data[1])
        if type_of_fire == "Low" and 1 <= range <= 50 \
            or type_of_fire == "Medium" and 51 <= range <= 80 \
                or type_of_fire == "High" and 81 <= range <= 125:
            if water >= range:
                valid_range.append(str(range))
                water -= range
                total_effort += 0.25 * range
                total_fire += range
print('Cells:')
for cell in valid_range:
    print(f'- {cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')


