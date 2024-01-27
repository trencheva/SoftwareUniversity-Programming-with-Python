def sum_numbers():
    numbers = [int(x) for x in input().split()]
    positives = 0
    negatives = 0

    for num in numbers:
        if num > 0:
            positives += num
        else:
            negatives += num

    print(negatives)
    print(positives)

    if positives > abs(negatives):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


sum_numbers()
