n = int(input())
all_numbers_are_even = True
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        all_numbers_are_even = False
        break
if all_numbers_are_even:
    print("All numbers are even.")