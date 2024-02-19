rows = int(input())

protected_airspace = []
fighter_pos = []

armor_value = 300
enemy_count = 4

for row in range(rows):
    line = list(input())
    protected_airspace.append(line)

    if 'J' in line:
        fighter_pos = [row, line.index('J')]
        protected_airspace[fighter_pos[0]][fighter_pos[1]] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()

    fighter_pos = [fighter_pos[0] + directions[command][0], fighter_pos[1] + directions[command][1]]

    if protected_airspace[fighter_pos[0]][fighter_pos[1]] == 'E':
        protected_airspace[fighter_pos[0]][fighter_pos[1]] = '-'
        enemy_count -= 1

        if enemy_count == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor_value -= 100
            if armor_value <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{fighter_pos[0]}, {fighter_pos[1]}]!")
                break

    elif protected_airspace[fighter_pos[0]][fighter_pos[1]] == 'R':
        protected_airspace[fighter_pos[0]][fighter_pos[1]] = '-'
        armor_value = 300


protected_airspace[fighter_pos[0]][fighter_pos[1]] = 'J'

[print(*row, sep='') for row in protected_airspace]