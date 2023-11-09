factor = int(input())
count_of_integers = int(input())
list_of_numbers = []
for current_number in range(1, count_of_integers + 1):
    list_of_numbers.append(factor * current_number)
print(list_of_numbers)