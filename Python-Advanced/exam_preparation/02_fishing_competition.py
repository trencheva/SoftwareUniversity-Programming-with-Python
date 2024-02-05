def check_indices(fisher_position):
    if 0 <= fisher_position[0] < len(fishing_area) and 0 <= fisher_position[1] < len(fishing_area):
        return True
    return False


def move_to_opposite_side(fisher_position):
    if fisher_position[0] < 0:
        fisher_position[0] = len(fishing_area) - 1
    elif fisher_position[0] == len(fishing_area):
        fisher_position[0] = 0
    if fisher_position[1] < 0:
        fisher_position[1] = len(fishing_area) - 1
    elif fisher_position[1] == len(fishing_area):
        fisher_position[1] = 0
    return fisher_position


fishing_area = []
fisher_pos = []

quota = 0

MIN_QUOTA = 20

for row in range(int(input())):
    line = list(input())

    fishing_area.append(line)

    if 'S' in line:
        fisher_pos = [row, line.index('S')]

        fishing_area[fisher_pos[0]][fisher_pos[1]] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
while command != 'collect the nets':

    fisher_pos[0], fisher_pos[1] = fisher_pos[0] + directions[command][0], fisher_pos[1] + directions[command][1]

    if not check_indices(fisher_pos):
        fisher_pos = move_to_opposite_side(fisher_pos)

    if fishing_area[fisher_pos[0]][fisher_pos[1]].isdigit():
        quota += int(fishing_area[fisher_pos[0]][fisher_pos[1]])

    elif fishing_area[fisher_pos[0]][fisher_pos[1]] == 'W':
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{fisher_pos[0]},{fisher_pos[1]}]")
        break

    fishing_area[fisher_pos[0]][fisher_pos[1]] = '-'
    command = input()

else:
    fishing_area[fisher_pos[0]][fisher_pos[1]] = 'S'

    if quota >= MIN_QUOTA:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {MIN_QUOTA - quota} tons of fish more.")

    if quota > 0:
        print(f"Amount of fish caught: {quota} tons.")

    [print(*row, sep='') for row in fishing_area]

