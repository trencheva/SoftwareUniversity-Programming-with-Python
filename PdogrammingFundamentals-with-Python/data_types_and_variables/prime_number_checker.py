number = int(input())
counter_of_delimiters = 0
number_is_prime = True
for current_num in range(1, number + 1):
    if number % current_num == 0:
        counter_of_delimiters += 1
    if counter_of_delimiters > 2:
        number_is_prime = False
print(number_is_prime)