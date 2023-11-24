string_with_stops = input()

while True:
    command = input()
    if command == 'Travel':
        break

    tokens = command.split(':')

    if tokens[0] == 'Add Stop':
        index = int(tokens[1])
        string = tokens[2]

        if 0 <= index < len(string_with_stops):
            string_with_stops = string_with_stops[0:index] + string + string_with_stops[index:]

    elif tokens[0] == 'Remove Stop':
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if 0 <= start_index < len(string_with_stops) and 0 <= end_index < len(string_with_stops):
            string_with_stops = string_with_stops[:start_index] + string_with_stops[end_index + 1:]

    elif tokens[0] == 'Switch':
        old_string = tokens[1]
        new_string = tokens[2]

        if old_string in string_with_stops:
            string_with_stops = string_with_stops.replace(old_string, new_string)
    print(string_with_stops)

print(f"Ready for world tour! Planned stops: {string_with_stops}")
