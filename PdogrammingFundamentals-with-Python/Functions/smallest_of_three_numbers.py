def smallest_finder(first: int, second: int, third: int) -> int:
    return min(first, second, third)


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(smallest_finder(first_number, second_number, third_number))