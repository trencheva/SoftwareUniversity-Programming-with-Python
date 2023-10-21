count_of_people = int(input())
current_state_of_the_lift = [int(s) for s in input().split()]
for current_place in range(len(current_state_of_the_lift)):
    wagon_capacity = 4 - current_state_of_the_lift[current_place]
    if count_of_people > wagon_capacity:
        current_state_of_the_lift[current_place] += wagon_capacity
    else:
        current_state_of_the_lift[current_place] += count_of_people
    count_of_people -= wagon_capacity
    if count_of_people < 0:
        break
if count_of_people < 0:
    print("The lift has empty spots!")
elif count_of_people > 0:
    print(f"There isn't enough space! {count_of_people} people in a queue!")

print(f"{' '.join(str(s) for s in current_state_of_the_lift)}")