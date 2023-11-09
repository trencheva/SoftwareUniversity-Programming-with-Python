string_of_integers = input().split(', ')
new_list = []
left_part = []
right_part = []

for current_number in range(len(string_of_integers)):
    if int(string_of_integers[current_number]) == 0:
        right_part.append(0)
    else:
        left_part.append(int(string_of_integers[current_number]))
new_list = left_part + right_part
print(new_list)

