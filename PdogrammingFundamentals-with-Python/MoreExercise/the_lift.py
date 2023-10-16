count_of_people = int(input())
current_state_of_the_lift = [int(s) for s in input().split()]
new_wagon = []
for current_place in current_state_of_the_lift:
    wagon_capacity = 4 - current_place
    if count_of_people > wagon_capacity:
        current_place += wagon_capacity
        count_of_people -= wagon_capacity
    else:
        current_place += count_of_people
        count_of_people -= count_of_people
    new_wagon.append(current_place)
if count_of_people > 0:
    print(f"There isn't enough space! {count_of_people} people in a queue!")
elif count_of_people == 0:
    print('The lift has empty spots!')

print(f"{' '.join(str(s) for s in new_wagon)}")