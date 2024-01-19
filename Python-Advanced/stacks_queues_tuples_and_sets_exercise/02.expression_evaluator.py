from functools import reduce

expression = input().split()

commands = {
    '+': lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
    '-': lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
    '*': lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    '/': lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
}

index = 0
while index < len(expression):
    element = expression[index]

    if element in '+-/*':
        expression[0] = commands[element](index)
        [expression.pop(1) for _ in range(index)]
        index = 1

    index += 1

print(int(expression[0]))


