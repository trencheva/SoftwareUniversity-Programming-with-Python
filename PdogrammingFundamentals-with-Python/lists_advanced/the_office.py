def employee_happiness(employees_happiness: list, factor: int) -> str:
    improved_happiness = [happiness * factor for happiness in employees_happiness]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = len([happiness for happiness in improved_happiness if happiness >= average_happiness])
    total_count = len(improved_happiness)
    are_happy = ''
    if happy_count < total_count // 2:
        are_happy = ' not'
    return f"Score: {happy_count}/{total_count}. Employees are{are_happy} happy!"


happiness_input = [int(happiness) for happiness in input().split()]
factor_input = int(input())
result = employee_happiness(happiness_input, factor_input)
print(result)