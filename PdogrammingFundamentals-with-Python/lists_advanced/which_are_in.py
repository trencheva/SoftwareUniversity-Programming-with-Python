first_string = input().split(', ')
second_string = input().split(', ')

result = []
for current_string in first_string:
    for string in second_string:
        if current_string in string:
            result.append(current_string)
            break
print(result)