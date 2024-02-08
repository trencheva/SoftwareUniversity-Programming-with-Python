def create_sequence(n):
    seq = [0, 1]

    for _ in range(n-2):
        nex_num = seq[-1] + seq[-2]
        seq.append(nex_num)

    return seq


def locate_number(number, seq):

    try:
        index = seq.index(number)
        return f"The number - {number} is at index {index}"
    except ValueError:
        return f"The number {number} is not in the sequence"

