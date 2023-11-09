elements = input().split()
command = input()
move = 0
while command != 'end':
    move += 1
    index1, index2 = map(int, command.split())
    if index1 == index2 or index1 < 0 or index2 > len(elements) - 1:
        new_element = str(f'-{move}a')
        index = len(elements) // 2
        elements.insert(index, new_element)
        elements.insert(index + 1, new_element)
        print("Invalid input! Adding additional elements to the board")

    elif elements[index1] == elements[index2]:
        removed_element = elements[index1]
        if index1 > index2:
            elements.pop(index1)
            elements.pop(index2)
        else:
            elements.pop(index2)
            elements.pop(index1)
        print(f"Congrats! You have found matching elements - {removed_element}!")

    elif elements[index1] != elements[index2]:
        print('Try again!')

    if not elements:
        print(f"You have won in {move} turns!")
        break
    command = input()
if elements:
    print('Sorry you lose :(')
    print(' '.join(elements))
