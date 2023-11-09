distances_as_integers = [int(s) for s in input().split()]
sum_of_removed_elements = 0
while distances_as_integers:
    index = int(input())

    if 0 <= index < len(distances_as_integers):
        removed_element = distances_as_integers[index]
        distances_as_integers.remove(removed_element)
    elif index < 0:
        removed_element = distances_as_integers[0]
        distances_as_integers[0] = distances_as_integers[-1]
    else:
        removed_element = distances_as_integers[-1]
        distances_as_integers[-1] = distances_as_integers[0]

    sum_of_removed_elements += removed_element

    for element in range(len(distances_as_integers)):
        if distances_as_integers[element] <= removed_element:
            distances_as_integers[element] += removed_element
        else:
            distances_as_integers[element] -= removed_element


print(sum_of_removed_elements)
