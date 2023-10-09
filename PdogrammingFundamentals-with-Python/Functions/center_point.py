def closest_to_the_center_point(x1, y1, x2, y2):
    first = abs(x1) + abs(y1)
    second = abs(x2) + abs(y2)
    if first <= second:
        return f'({int(x1)}, {int(y1)})'
    return f'({int(x2)}, {int(y2)})'


x1_input = float(input())
y1_input = float(input())
x2_input = float(input())
y2_input = float(input())

print(closest_to_the_center_point(x1_input, y1_input, x2_input, y2_input))

