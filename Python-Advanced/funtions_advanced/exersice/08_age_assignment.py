def age_assignment(*names, **kwargs):
    result = []
    for letter, age in kwargs.items():
        for name in names:
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")

    return '\n'.join(sorted(result))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))