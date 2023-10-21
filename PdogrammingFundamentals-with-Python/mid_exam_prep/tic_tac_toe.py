first_line = input().split()
second_line = input().split()
third_line = input().split()
winner = ''
win_count = 0
if first_line[2] == second_line[2] == third_line[2]:
    winner = first_line[2]
    if winner != '0':
        win_count += 1
if first_line[1] == second_line[1] == third_line[1]:
    winner = first_line[1]
    if winner != '0':
        win_count += 1
if first_line[0] == second_line[0] == third_line[0]:
    winner = first_line[1]
    if winner != '0':
        win_count += 1
if first_line[0] == first_line[1] == first_line[2]:
    winner = first_line[0]
    if winner != '0':
        win_count += 1
if second_line[0] == second_line[1] == second_line[2]:
    winner = second_line[0]
    if winner != '0':
        win_count += 1
if third_line[0] == third_line[1] == third_line[2]:
    winner = third_line[0]
    if winner != '0':
        win_count += 1
if first_line[0] == second_line[1] == third_line[2]:
    winner = first_line[0]
    if winner != '0':
        win_count += 1
if first_line[2] == second_line[1] == third_line[0]:
    winner = first_line[2]
    if winner != '0':
        win_count += 1
if win_count == 1:
    if winner == '2':
        print('Second player won')
    elif winner == '1':
        print('First player won')
    else:
        print('Draw!')
else:
    print('Draw!')

