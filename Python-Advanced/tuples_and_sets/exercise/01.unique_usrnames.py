names = set()

for _ in range(int(input())):
    name = input()
    names.add(name)

print(*names, sep='\n')

# another solution
# print(*{input() for _ in range(int(input()))}, sep='\n')
