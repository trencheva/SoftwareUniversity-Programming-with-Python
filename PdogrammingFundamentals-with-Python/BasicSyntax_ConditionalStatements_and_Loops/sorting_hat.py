while True:
    command = input()
    if command == 'Welcome!':
        print("Welcome to Hogwarts.")
        break
    if command == 'Voldemort':
        print("You must not speak of that name!")
        break
    length_of_the_name = len(command)
    if length_of_the_name < 5:
        print(f"{command} goes to Gryffindor.")
    elif length_of_the_name == 5:
        print(f'{command} goes to Slytherin.')
    elif length_of_the_name == 6:
        print(f"{command} goes to Ravenclaw.")
    else:
        print(f"{command} goes to Hufflepuff.")