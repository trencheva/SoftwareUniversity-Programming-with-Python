def operate(symbol, *args):
    from functools import reduce
    result = 0
    if symbol == '+':
        result = reduce(lambda a, b: a+b, args)
    elif symbol == '-':
        result = reduce(lambda a, b: a-b, args)
    elif symbol == '*':
        result = reduce(lambda a, b: a*b, args)
    elif symbol == '/':
        result = reduce(lambda a, b: a/b, args)

    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))