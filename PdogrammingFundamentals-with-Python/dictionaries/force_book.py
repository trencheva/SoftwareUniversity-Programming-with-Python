force_sides_dict = {}
command = input()
while command != 'Lumpawaroo':
    if '|' in command:
        force_side, force_user = command.split(' | ')
        user_is_part_of_the_force = False
        for value in force_sides_dict.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_sides_dict.keys():
                force_sides_dict[force_side] = []
            force_sides_dict[force_side].append(force_user)
    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        for value in force_sides_dict.values():
            if force_user in value:
                value.remove(force_user)
                break

        if force_side not in force_sides_dict.keys():
            force_sides_dict[force_side] = []
        force_sides_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for force_side, members in force_sides_dict.items():
    if len(members) > 0:
        print(f"Side: {force_side}, Members: {len(members)}")
        for member in members:
            print(f'! {member}')
