divisor = int(input())
boundary = int(input())
largest_number = 0
for number in range(1, boundary+1):
    if number % divisor == 0:
        if number > largest_number:
            largest_number = number
print(largest_number)