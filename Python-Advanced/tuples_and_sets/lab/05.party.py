n = int(input())

reservation_numbers = set()

for _ in range(n):
    reservation_numbers.add(input())

guest = input()
while guest != 'END':

    if guest in reservation_numbers:
        reservation_numbers.remove(guest)

    guest = input()

print(len(reservation_numbers))
reservation_numbers = sorted(reservation_numbers)

for number in reservation_numbers:
    print(number)