number_of_rooms = int(input())
total_free_chairs = 0
for current_room in range(1, number_of_rooms + 1):
    free_chairs, visitors = input().split()
    difference = len(free_chairs) - int(visitors)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {current_room}")
    total_free_chairs += difference


if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")