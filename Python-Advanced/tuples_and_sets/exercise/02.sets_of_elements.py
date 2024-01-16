# Another solution
# first_set = set()
# second_set = set()
#
# n, m = input().split()
#
# for _ in range(int(n)):
#     element = input()
#     first_set.add(element)
#
# for _ in range(int(m)):
#     element = input()
#     second_set.add(element)
#
# print(*first_set.intersection(second_set), sep='\n')

n, m = [int(num) for num in input().split()]

first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

print(*first_set & second_set, sep='\n')
