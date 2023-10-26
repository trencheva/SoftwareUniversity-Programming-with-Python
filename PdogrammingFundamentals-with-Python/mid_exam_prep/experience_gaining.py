needed_experience = float(input())
count_of_battles = int(input())
collected_experience = 0
he_succeed = False
for current_battle in range(1, count_of_battles + 1):
    current_experience = float(input())
    collected_experience += current_experience
    if current_battle % 3 == 0:
        collected_experience += current_experience * 0.15
    if current_battle % 5 == 0:
        collected_experience -= current_experience * 0.10
    if current_battle % 15 == 0:
        collected_experience += current_experience * 0.05

    if collected_experience >= needed_experience:
        print(f'Player successfully collected his needed experience for {current_battle} battles.')
        he_succeed = True
        break

if not he_succeed:
    print(f'Player was not able to collect the needed experience, {needed_experience - collected_experience:.2f} more needed.')

