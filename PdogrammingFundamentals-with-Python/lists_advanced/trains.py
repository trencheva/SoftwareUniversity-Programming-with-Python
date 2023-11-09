def trains(number: int) -> list:
    train = [0] * number

    while True:
        command = input().split()

        if command[0] == 'End':
            print(train)
            break

        if command[0] == 'add':
            train[-1] += int(command[1])

        elif command[0] == 'insert':
            index = int(command[1])
            train[index] += int(command[2])

        elif command[0] == 'leave':
            index = int(command[1])
            train[index] -= int(command[2])

    return train


number_of_trains = int(input())

trains(number_of_trains)
