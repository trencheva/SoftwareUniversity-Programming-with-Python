players_information = {}
final_score_dict = {}
while True:
    command = input()
    if command == "Season end":
        break
    if '->' in command:
        player, position, skill = command.split(' -> ')
        if player not in players_information.keys():
            players_information[player] = {}

        if position not in players_information[player].keys():
            players_information[player][position] = 0
        if players_information[player][position] < int(skill):
            players_information[player][position] = int(skill)
    else:
        first_player, second_player = command.split(' vs ')
        if first_player in players_information and second_player in players_information:
            for first_player_position, skill_f in players_information[first_player].items():
                for second_player_position, skill_s in players_information[second_player].items():
                    if first_player_position == second_player_position:
                        if skill_f > skill_s:
                            del players_information[second_player]
                        elif skill_f < skill_s:
                            del players_information[first_player]

for player, position in players_information.items():
    if player not in final_score_dict:
        final_score_dict[player] = 0
    for skill in position.values():
        final_score_dict[player] += skill

final_score_dict = dict(sorted(final_score_dict.items(), key=lambda x: (-x[1], x[0])))
for name, score in final_score_dict.items():
    print(f'{name}: {score} skill')
    final_information = dict(sorted(players_information[name].items(), key=lambda x: (-x[1], x[0])))
    for position, skill in final_information.items():
        print(f'- {position} <::> {skill}')


