numbers_as_string = input().split()
list_of_integers = []

for number in numbers_as_string:
    list_of_integers.append(int(number))

is_even = lambda x: x % 2 == 0
result = list(filter(is_even, list_of_integers))
print(result)

