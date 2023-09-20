while True:
    string = input()
    if string != 'End':
        if string != 'SoftUni':
            new_string = ''
            for character in string:
                new_string += character * 2
            print(new_string)
    else:
        break