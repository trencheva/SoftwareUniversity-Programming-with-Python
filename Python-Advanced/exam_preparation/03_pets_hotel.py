def accommodate_new_pets(hotel_capacity, max_weight_limit, *pets_info):
    total_pets_count = {}
    result = []

    for pet_type, weight in pets_info:

        if hotel_capacity == 0:
            result.append("You did not manage to accommodate all pets!")
            break

        if max_weight_limit >= weight:
            total_pets_count[pet_type] = total_pets_count.get(pet_type, 0) + 1
            hotel_capacity -= 1

    else:
        result.append(f"All pets are accommodated! Available capacity: {hotel_capacity}.")

    result.append("Accommodated pets:")

    for pet, count in sorted(total_pets_count.items(), key=lambda x: x[0]):
        result.append(f"{pet}: {count}")

    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
