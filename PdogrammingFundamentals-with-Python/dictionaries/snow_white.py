dwarf_data = []


def data(name, color, physics):
    result = {'name': name, 'hat_color': color, 'dwarf_physics': physics}
    return result


index = 0
command = input()
while command != 'Once upon a time':
    tokens = command.split(' <:> ')
    dwarf_name, dwarf_hat_color, dwarf_physics = tokens[0], tokens[1], int(tokens[2])
    for current_data in dwarf_data:
        if current_data['name'] == dwarf_name and current_data['hat_color'] == dwarf_hat_color:
            if current_data['dwarf_physics'] < dwarf_physics:
                current_data['dwarf_physics'] = dwarf_physics
                index = dwarf_data.index(current_data)
    if dwarf_data:
        if dwarf_data[index]['name'] != dwarf_name or dwarf_data[index]['hat_color'] != dwarf_hat_color:
            dwarf_data.append(data(dwarf_name, dwarf_hat_color, dwarf_physics))
    else:
        dwarf_data.append(data(dwarf_name, dwarf_hat_color, dwarf_physics))

    command = input()


dwarf_data = sorted(dwarf_data, key=lambda x: -x['dwarf_physics'])

for dwarf in dwarf_data:
    hat_color = dwarf['hat_color']
    name = dwarf['name']
    physics = dwarf['dwarf_physics']
    print(f"({hat_color}) {name} <-> {physics}")
