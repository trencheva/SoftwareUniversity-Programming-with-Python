def sorting_cheeses(**kwargs):
    result = ''
    sorted_kwargs = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for name, info in sorted_kwargs:
        result += f'{name}\n'
        for el in sorted(info, reverse=True):
            result += f'{el}\n'
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
