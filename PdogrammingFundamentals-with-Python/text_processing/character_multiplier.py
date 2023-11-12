first, second = input().split()
final_result = 0

if len(first) > len(second):
    for index in range(len(second)):
        final_result += ord(first[index]) * ord(second[index])
    for index in range(len(second), len(first), 1):
        final_result += ord(first[index])
elif len(second) > len(first):
    for index in range(len(first)):
        final_result += ord(first[index]) * ord(second[index])
    for index in range(len(first), len(second), 1):
        final_result += ord(second[index])
else:
    for index in range(len(first)):
        final_result += ord(first[index]) * ord(second[index])

print(final_result)