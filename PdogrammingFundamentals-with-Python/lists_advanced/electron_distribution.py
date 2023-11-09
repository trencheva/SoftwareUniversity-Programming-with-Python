number_of_electrons = int(input())
list_with_filled_shells = []
for current_shell in range(1, number_of_electrons + 1):
    max_number_of_electrons = 2 * current_shell ** 2
    if number_of_electrons > max_number_of_electrons:
        number_of_electrons -= max_number_of_electrons
        list_with_filled_shells.append(max_number_of_electrons)
    else:
        list_with_filled_shells.append(number_of_electrons)
        break

print(list_with_filled_shells)