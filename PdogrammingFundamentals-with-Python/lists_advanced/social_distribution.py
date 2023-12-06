population = [int(i) for i in input().split(', ')]
minimum_wealth = int(input())


while True:
    max_num = max(population)
    index_max = population.index(max_num)
    min_num = min(population)
    index_min = population.index(min_num)
    needed = minimum_wealth - min_num

    if needed == 0:
        print(population)
        break
    if max_num - needed >= minimum_wealth:
        population[index_min] += needed
        population[index_max] -= needed

    else:
        print("No equal distribution possible")
        break
