first_set = set()
second_set = set()

n, m = input().split()

for _ in range(int(n)):
    element = input()
    first_set.add(element)

for _ in range(int(m)):
    element = input()
    second_set.add(element)

print(*first_set.intersection(second_set), sep='\n')