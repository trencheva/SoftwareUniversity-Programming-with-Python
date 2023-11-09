def status_finder(numbers: list):
    negative_counter = 0
    for current_number in numbers:
        if current_number < 0:
            negative_counter += 1
        elif current_number == 0:
            return 'zero'
    if negative_counter % 2 != 0:
        return 'negative'
    else:
        return 'positive'


list_input = []
for current_input in range(3):
    number_input = int(input())
    list_input.append(number_input)
print(status_finder(list_input))
