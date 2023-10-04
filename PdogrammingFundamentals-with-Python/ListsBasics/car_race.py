list_of_numbers = input().split(' ')
middle = len(list_of_numbers) // 2
left_car = 0
right_car = 0
for left in list_of_numbers[0:middle]:
    if left == '0':
        left_car *= 0.8
    else:
        left_car += int(left)
for right in list_of_numbers[-1:middle:-1]:
    if right == '0':
        right_car *= 0.8
    else:
        right_car += int(right)
if left_car < right_car:
    print(f"The winner is left with total time: {left_car:.1f}")
elif right_car < left_car:
    print(f"The winner is right with total time: {right_car:.1f}")
