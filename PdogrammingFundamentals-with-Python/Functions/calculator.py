def addition(first_number, second_number):
    result = first_number + second_number
    return result


def subtract(first_number, second_number):
    result = first_number - second_number
    return result


def multiplication(first_number, second_number):
    result = first_number * second_number
    return result


def division(first_number, second_number):
    if first_number == 0 or second_number == 0:
        print('Error Value, Division to Zero.')
        print('Please enter correct number!')
    else:
        result = first_number / second_number
        return result


def main():
    while True:
        print()
        print('Menu:')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Quit')
        print()

        result = None

        operation = input("Please enter the operation you wish to perform: 1/2/3/4/5")
        print()
        first_number_input = float(input('Please enter the first number:'))
        second_number_input = float(input('Please enter the second number:'))
        if operation == "1":
            result = addition(first_number_input, second_number_input)
        elif operation == "2":
            result = subtract(first_number_input, second_number_input)
        elif operation == "3":
            result = multiplication(first_number_input, second_number_input)
        elif operation == "4":
            result = division(first_number_input, second_number_input)
        elif operation == "5":
            print("Goodbye!")
            break

        else:
            print('Invalid Operation!')
            continue
        print(f'Result: {result}')


if __name__ == '__main__':
    main()


