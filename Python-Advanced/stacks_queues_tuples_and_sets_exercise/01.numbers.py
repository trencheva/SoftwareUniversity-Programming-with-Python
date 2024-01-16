first = {int(num) for num in input().split()}
second = {int(num) for num in input().split()}

for _ in range(int(input())):
    tokens = input().split()

    command = tokens[:2]

    if command[0] == 'Add':
        nums = {int(num) for num in tokens[2:]}
        if command[1] == 'First':
            first = first.union(nums)
        else:
            second = second.union(nums)

    elif command[0] == 'Remove':
        nums = {int(num) for num in tokens[2:]}
        if command[1] == 'First':
            for el in nums:
                if el in first:
                    first.remove(el)
        else:
            for el in nums:
                if el in second:
                    second.remove(el)

    else:
        if first.issubset(second) or second.issubset(first):
            print(True)
        else:
            print(False)


print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
