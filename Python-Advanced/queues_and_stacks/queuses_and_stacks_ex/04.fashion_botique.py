clothes = [int(i) for i in input().split()]
rack_capacity = int(input())

racks_count = 1
current_rack_capacity = rack_capacity

while clothes:
    clothing_piece = clothes.pop()

    if current_rack_capacity - clothing_piece >= 0:
        current_rack_capacity -= clothing_piece
    else:
        racks_count += 1
        current_rack_capacity = rack_capacity - clothing_piece

print(racks_count)