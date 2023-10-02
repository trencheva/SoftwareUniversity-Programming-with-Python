from sys import maxsize
string_of_numbers = input().split(' ')
times_to_remove = int(input())

for current_removal in range(times_to_remove):
    smallest_number = maxsize
    for current_number in string_of_numbers:
        if int(current_number) < int(smallest_number):
            smallest_number = current_number
    string_of_numbers.remove(smallest_number)
print(', '.join(string_of_numbers))