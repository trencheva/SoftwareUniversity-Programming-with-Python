from math import log


def calculation_logarithm(num, base):
    try:
        base = int(base)
        return log(num, base)
    except ValueError:
        return log(num)


number = int(input())
base = input()

print(f"{calculation_logarithm(number, base):.2f}")
