sting_of_integers = input().split(', ')
count_of_beggars = int(input())
total_amount_of_offer = []
index = 0

for current_beggar in range(count_of_beggars):
    offer_for_current_beggar = 0

    for offer in range(index, len(sting_of_integers), count_of_beggars):
        offer_for_current_beggar += int(sting_of_integers[offer])
    total_amount_of_offer.append(offer_for_current_beggar)
    index += 1

print(total_amount_of_offer)
