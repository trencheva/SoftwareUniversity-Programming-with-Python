from collections import deque


def list_manipulator(numbers: list, *args) -> list:
    command = args[0]
    info = args[1]
    nums = deque(numbers)

    if command == 'add':
        if info == 'end':
            nums.extend(args[2:])
        elif info == 'beginning':
            [nums.appendleft(el) for el in args[-1:-(len(args)-1):-1]]
    elif command == 'remove':
        if info == 'end':
            if len(args) > 2:
                [nums.pop() for _ in range(args[-1])]
            else:
                nums.pop()
        elif info == 'beginning':
            if len(args) > 2:
                [nums.popleft() for _ in range(args[-1])]
            else:
                nums.popleft()

    return list(nums)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
