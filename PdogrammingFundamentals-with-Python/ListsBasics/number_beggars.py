sting_of_integers = input().split(', ')
count_of_beggars = int(input())
total_amount_of_offer = []
index = 0



offer_for_current_beggar = 0
for offer in range(index, len(sting_of_integers) + 1, count_of_beggars):
    offer_for_current_beggar += offer[sting_of_integers]

    index += 1
