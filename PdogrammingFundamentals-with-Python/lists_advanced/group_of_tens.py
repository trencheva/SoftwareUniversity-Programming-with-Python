list_of_integers = [int(number) for number in input().split(', ')]
group = 10
while list_of_integers:
    current_group = [nums for nums in list_of_integers if nums <= group]
    print(f"Group of {group}'s: {current_group}")
    list_of_integers = [member for member in list_of_integers if member not in current_group]
    group += 10

