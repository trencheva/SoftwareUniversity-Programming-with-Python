budget = float(input())
price_for_one_kg_flour = float(input())
pack_egg_price = price_for_one_kg_flour * 0.75
milk_for_one_loaf = (price_for_one_kg_flour + price_for_one_kg_flour * 0.25) / 4
price_for_one_bread = price_for_one_kg_flour + pack_egg_price + milk_for_one_loaf
current_bread_count = 0
egg_counter = 0
while budget > price_for_one_bread:
    budget -= price_for_one_bread
    current_bread_count += 1
    egg_counter += 3
    if current_bread_count % 3 == 0:
        egg_counter -= current_bread_count - 2
print(f"You made {current_bread_count} loaves of Easter bread! Now you have {egg_counter} eggs and {budget:.2f}BGN left.")