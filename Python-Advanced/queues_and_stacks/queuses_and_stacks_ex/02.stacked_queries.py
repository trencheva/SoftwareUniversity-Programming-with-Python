stack = []
map_functions = {
    '1': lambda x: stack.append(int(x[1])),
    '2': lambda x: stack.pop() if stack else None,
    '3': lambda x: print(max(stack)) if stack else None,
    '4': lambda x: print(min(stack)) if stack else None,

}

for _ in range(int(input())):
    numbers_data = input().split()
    command = numbers_data[0]

    map_functions[command](numbers_data)
stack.reverse()
print(*stack, sep=', ')

# if command[0] == "1":     alternative decision, using if else
#     number = int(numbers_data[1])
#     stack.append(number)
# elif command[0] == "2":
#     if stack:
#         stack.pop()
# elif command[0] == "3":
#     if stack:
#         print(max(stack))
# else:
#     if stack:
#         print(min(stack))
