def loading_bar(number: int):
    if number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    else:
        number_of_percentage = number // 10
        number_of_dots = 10 - number_of_percentage
        return f"{number}% [{'%' * number_of_percentage}{'.' * number_of_dots}]\nStill loading..."


number_input = int(input())
print(loading_bar(number_input))
