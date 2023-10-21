food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
food *= 1000
hay *= 1000
cover *= 1000
weight *= 1000
have_enough_products = True
for day in range(1, 31):
    food -= 300
    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= weight / 3
    if food <= 0 or hay <= 0 or cover <= 0:
        have_enough_products = False
        break
if have_enough_products:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
else:
    print("Merry must go to the pet store!")
