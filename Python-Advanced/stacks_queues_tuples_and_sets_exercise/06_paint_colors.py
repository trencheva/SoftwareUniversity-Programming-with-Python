from collections import deque

substrings = deque(input().split())

colors = []

main_colors = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = {
                 "orange": {'red', 'yellow'},
                 "purple": {'blue', 'red'},
                 "green": {'blue', 'yellow'}
                    }

while substrings:
    first = substrings.popleft()
    second = substrings.pop() if substrings else ''

    for combination in (first + second, second + first):
        if combination in main_colors:
            colors.append(combination)
            break
    else:
        for el in (first[:-1], second[:-1]):
            if el:
                substrings.insert(len(substrings) // 2, el)

for color in colors.copy():
    if color in secondary_colors.keys():
        if not secondary_colors[color].issubset(colors):
            colors.remove(color)


print(colors)