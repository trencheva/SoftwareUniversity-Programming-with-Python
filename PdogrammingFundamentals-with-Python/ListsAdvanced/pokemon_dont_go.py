pokemons = [int(number) for number in input().split()]

sum_of_removed = 0
while pokemons:
    removed_element = 0
    index = int(input())

    if index < 0:
        index = 0
        removed_element = pokemons[index]
        pokemons[index] = pokemons[-1]
    elif index > len(pokemons) - 1:
        index = len(pokemons) - 1
        removed_element = pokemons[index]
        pokemons[index] = pokemons[0]
    else:
        removed_element = pokemons[index]
        pokemons.remove(pokemons[index])

    for current_pokemon in range(len(pokemons)):
        if pokemons[current_pokemon] <= removed_element:
            pokemons[current_pokemon] += removed_element
        else:
            pokemons[current_pokemon] -= removed_element
    sum_of_removed += removed_element
result = sum_of_removed
print(result)