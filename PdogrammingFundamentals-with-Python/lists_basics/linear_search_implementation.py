# Linear Search Implementation

def linear_search(input_list, target):
    result = -1
    for number in range(len(input_list)):
        if target == input_list[number]:
            result = int(number)
    if result != -1:
        print(f"The target element {target} is at index {result}.")
    else:
        print(f"The target element {target} was not found in the list.")


my_list = [1, 3, 8, 7, 9, 11, 56, 98, 17]
target = 17
linear_search(my_list, target)

