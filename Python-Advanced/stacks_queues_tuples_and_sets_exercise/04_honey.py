from collections import deque

bees = deque(int(bee) for bee in input().split())
nectar = [int(nec) for nec in input().split()]
symbols = deque(input().split())

honey = 0

functions = {
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if not b == 0 else 0,
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        honey += abs(functions[symbols.popleft()](current_bee, current_nectar))
    else:
        bees.appendleft(current_bee)

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(b) for b in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(n) for n in nectar)}")

