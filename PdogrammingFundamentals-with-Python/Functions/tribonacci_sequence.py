def tribonacci_sequence(number:int) -> list:
    sequence = []
    num_from_sequence = 1
    for current_number in range(number):
        sequence.append(num_from_sequence)
        if current_number >= 3:
            num_from_sequence = 0
            counter = 0
            for i in range(len(sequence)-1, -1, -1):
                counter += 1
                num_from_sequence += sequence[i]
                if counter == 3:
                    break
        else:
            num_from_sequence = sum(sequence)
    return sequence


number_input = int(input())
result = tribonacci_sequence(number_input)
print(*result)
