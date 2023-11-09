cards_string = input().split(' ')
number_of_shuffles = int(input())
middle_of_the_string = len(cards_string) // 2

for current_shuffle in range(number_of_shuffles):
    shuffled_cards = []
    left_part = cards_string[0:middle_of_the_string]
    right_part = cards_string[middle_of_the_string::]

    for i in range(len(left_part)):
        shuffled_cards.append(left_part[i])
        shuffled_cards.append(right_part[i])
        cards_string = shuffled_cards

print(cards_string)