def naughty_or_nice_list(santa_list, *args, **kwargs):
    final_result = []

    sorted_kids = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }

    for idx in range(len(args)):
        number = int(args[idx].split('-')[0])
        command = args[idx].split('-')[1]
        occurrences = 0
        name = ''

        for idx in range(len(santa_list)):
            num, kid_name = santa_list[idx]

            if number == num:
                index_to_remove = idx
                name = kid_name
                occurrences += 1

        if occurrences == 1:
            sorted_kids[command].append(name)
            santa_list.pop(index_to_remove)

    for name, command in kwargs.items():
        occurrences = 0
        current_name = ''

        for idx in range(len(santa_list)):
            num, kid_name = santa_list[idx]

            if kid_name == name:
                current_name = kid_name
                index_to_remove = idx
                occurrences += 1
        if occurrences == 1:
            sorted_kids[command].append(current_name)
            santa_list.pop(index_to_remove)

    for num, name in santa_list:
        sorted_kids["Not found"].append(name)

    for key, value in sorted_kids.items():
        if value:
            final_result.append(f'{key}: {", ".join(value)}')

    return '\n'.join(final_result)


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
